import cv2
import numpy as np

# importing user defined python file
import parameters


cap = cv2.VideoCapture(0)
cap.set(3, 400)
cap.set(4, 200)

# Hard coded values
h_min = 150
h_max = 190
s_min = 195
s_max = 255
v_min = 195
v_max = 255
threshold1 = 0
threshold2 = 225


# detecting the standard in the image and marking it
def getContour(img, imgContour):
	contour, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	
	for cnt in contour:
		area = cv2.contourArea(cnt)
		peri = cv2.arcLength(cnt, True) # True shows that the shape is closed
		approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
		if 4 <= len(approx) <= 7:
			cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
			x, y, w, h = cv2.boundingRect(approx)
			cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0), 5)


while True:
	
	_, img = cap.read()

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

	cv2.imshow('Stacked', hstack)


	if cv2.waitKey(1) &0xFF == ord('q'):
		cv2.destroyAllWindows()
		break
	elif cv2.waitKey(1) &0xFF == ord('p'):
		(h_min, h_max, s_min, s_max, v_min, v_max, threshold1, threshold2) = parameters.takeVal()

cap.release()
cv2.destroyAllWindows()
