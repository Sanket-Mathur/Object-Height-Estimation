import base64
import pickle
import numpy as np
from cv2 import cv2

# Loading the saved values
save = open('Values/save.dat', 'rb')
db = pickle.load(save)
(h_min, h_max, s_min, s_max, v_min, v_max, threshold1, threshold2, area_min) = tuple(db.values())

# Draw Contour (Used internally)
def getContour(img, imgContour):
	contour, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	global h
	found = False
	for cnt in contour:
		area = cv2.contourArea(cnt)
		peri = cv2.arcLength(cnt, True) # True shows that the shape is closed
		approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
		area = cv2.contourArea(cnt)
		if 4 <= len(approx) <= 7 and area > area_min:
			found = True
			cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 3)
			x, y, w, h = cv2.boundingRect(approx)
			cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0), 3)
	return found

# Mark the images if standard detected
def identifyMark(base64Image):
	img_str = base64.b64decode(base64Image)

	nparr = np.fromstring(img_str, np.uint8)
	image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
	imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	lower = np.array([h_min, s_min, v_min])
	upper = np.array([h_max, s_max, v_max])
	mask = cv2.inRange(imgHSV, lower, upper)
	mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
	imgCanny = cv2.Canny(mask, threshold1, threshold2)
	kernel = np.ones((5,5))
	imgDil = cv2.dilate(imgCanny, kernel, iterations=1)
	found = getContour(imgDil, image)

	img_str = cv2.imencode('.jpg', image)[1].tobytes()
	base64ImageReturn = base64.b64encode(img_str) 
	return ('yes' if found else 'no'), base64ImageReturn