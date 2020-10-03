import cv2
import pickle
import numpy as np

save = open('Values/save.dat', 'rb')

# detecting the standard in the image and marking it
def getContour(img, imgContour):
	contour, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	
	for cnt in contour:
		area = cv2.contourArea(cnt)
		peri = cv2.arcLength(cnt, True) # True shows that the shape is closed
		approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
		area = cv2.contourArea(cnt)
		if 4 <= len(approx) <= 7 and area > area_min:
			cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
			x, y, w, h = cv2.boundingRect(approx)
			cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0), 5)

db = pickle.load(save)
try:
    (h_min, h_max, s_min, s_max, v_min, v_max, threshold1, threshold2, area_min) = tuple(db.values())
except:
    print('Nope')
    exit(0)

# path = input('Enter the path: ')
path = 'User/Testing.jpg'
img = cv2.imread(path)

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
getContour(imgDil, img)

hstack = np.hstack([img, result, mask])
hstack = cv2.resize(hstack, (1020, 240))

cv2.imshow('Stacked', hstack)

cv2.waitKey(5000)