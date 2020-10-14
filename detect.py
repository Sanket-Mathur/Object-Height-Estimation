from cv2 import cv2
import numpy as np
import pickle
import time


save = open('Values/save.dat', 'rb')

cap = cv2.VideoCapture(0)
cap.set(3, 600)
cap.set(4, 300)


# detecting the standard in the image and marking it
def getContour(img, imgContour):
	contour, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	found = False
	for cnt in contour:
		area = cv2.contourArea(cnt)
		peri = cv2.arcLength(cnt, True) # True shows that the shape is closed
		approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
		area = cv2.contourArea(cnt)
		if 4 <= len(approx) <= 7 and area > area_min:
			found = True
			cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
			x, y, w, h = cv2.boundingRect(approx)
			cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0), 5)
	return found


def empty(a):
	pass

# spawns a Window for changing the parameters
def takeVal():

	img = cv2.imread('SysImages/Parameters.png')[:160, :, :]
	img = cv2.resize(img, (340, 120))
	
	cv2.namedWindow('Parameters')
	cv2.imshow('Parameters', img)
	cv2.resizeWindow('Parameters', 640, 240)
	cv2.createTrackbar('HUE Min', 'Parameters', 150, 255, empty)
	cv2.createTrackbar('HUE Max', 'Parameters', 190, 255, empty)
	cv2.createTrackbar('SAT Min', 'Parameters', 195, 255, empty)
	cv2.createTrackbar('SAT Max', 'Parameters', 255, 255, empty)
	cv2.createTrackbar('VALUE Min', 'Parameters', 195, 255, empty)
	cv2.createTrackbar('VALUE Max', 'Parameters', 255, 255, empty)
	cv2.createTrackbar('Thresh1', 'Parameters', 0, 255, empty)
	cv2.createTrackbar('Thresh2', 'Parameters', 225, 255, empty)
	cv2.createTrackbar('Area Min', 'Parameters', 100, 1000, empty)


read_temp = False
db = pickle.load(save)
try:
	(h_min, h_max, s_min, s_max, v_min, v_max, threshold1, threshold2, area_min) = tuple(db.values())
except:
	read_temp = True 
	takeVal()

while True:
	
	_, img = cap.read()
	img_copy = img.copy()

	if read_temp:
		h_min = cv2.getTrackbarPos('HUE Min', 'Parameters')
		h_max = cv2.getTrackbarPos('HUE Max', 'Parameters')
		s_min = cv2.getTrackbarPos('SAT Min', 'Parameters')
		s_max = cv2.getTrackbarPos('SAT Max', 'Parameters')
		v_min = cv2.getTrackbarPos('VALUE Min', 'Parameters')
		v_max = cv2.getTrackbarPos('VALUE Max', 'Parameters')
		threshold1 = cv2.getTrackbarPos('Thresh1', 'Parameters') 
		threshold2 = cv2.getTrackbarPos('Thresh2', 'Parameters')
		area_min = cv2.getTrackbarPos('Area Min', 'Parameters')
		db['h_min'], db['h_max'], db['s_min'], db['s_max'], db['v_min'], db['v_max'], db['threshold1'], db['threshold2'], db['area_min'] = h_min, h_max, s_min, s_max, v_min, v_max, threshold1, threshold2, area_min

	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	lower = np.array([h_min, s_min, v_min])
	upper = np.array([h_max, s_max, v_max])

	mask = cv2.inRange(imgHSV, lower, upper)
	result = cv2.bitwise_and(img, img, mask = mask)
	
	mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

	# converting images required in order to call getContour()
	imgCanny = cv2.Canny(mask, threshold1, threshold2)
	kernel = np.ones((5,5))
	imgDil = cv2.dilate(imgCanny, kernel, iterations=1)
	found = getContour(imgDil, img)

	hstack = np.hstack([img, result, mask])

	cv2.imshow('Stacked', hstack)


	if cv2.waitKey(1) &0xFF == ord('q'):
		if read_temp:
			cv2.destroyWindow('Parameters')
			read_temp = False 
		else:
			break
	elif cv2.waitKey(1) &0xFF == ord('p'):
		db = {}
		takeVal()
		read_temp = True
	elif (cv2.waitKey(1) &0xFF == ord('s')) and read_temp:
		# writing the current values into save.dat
		write = open('Values/save.dat', 'wb')
		pickle.dump(db, write)
		print('Saved')
		write.close()
		cv2.destroyWindow('Parameters')
		read_temp = False
	elif cv2.waitKey(1) &0xFF == ord('c'):
		blur = cv2.Laplacian(img_copy, cv2.CV_64F).var()
		if found and blur > 500:
			nowTime = time.time()
			cv2.imwrite('User'+'/'+str(int(blur))+"_"+str(nowTime)+".png", img_copy)
			print('Captured')
			break


save.close()
cap.release()
cv2.destroyAllWindows()
