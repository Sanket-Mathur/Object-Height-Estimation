from cv2 import cv2
import pickle
import numpy as np
from math import sqrt


save = open('Values/save.dat', 'rb')


# detecting the standard in the image and marking it
h = 1
def getContour(img, imgContour):
	contour, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	global h
	for cnt in contour:
		area = cv2.contourArea(cnt)
		peri = cv2.arcLength(cnt, True) # True shows that the shape is closed
		approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
		area = cv2.contourArea(cnt)
		if 4 <= len(approx) <= 7 and area > area_min:
			cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 3)
			x, y, w, h = cv2.boundingRect(approx)
			cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0), 3) # rectangle must match with the contour for knowing the standard in parallel


# Function for detecting mouse points and saving it into as numpy array
points = np.zeros((2,2), np.int)
counter = 0
def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        points[counter] = x,y
        counter += 1


db = pickle.load(save)
try:
    (h_min, h_max, s_min, s_max, v_min, v_max, threshold1, threshold2, area_min) = tuple(db.values())
except:
    print('Nope')
    exit(0)

path = 'User/'
fname = input('Enter the name of the file: ')
img = cv2.imread(path + fname)

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


while True:
    
	for i in range(counter):
		cv2.circle(img, (points[i][0], points[i][1]), 5, (0,0,255), cv2.FILLED)
	cv2.imshow('Image', img)

	if counter == 2:
		break

	cv2.setMouseCallback('Image', mousePoints)

	cv2.waitKey(1)
	

dist = abs(points[0,1] - points[1,1])
print('Height Estimate: {:.2f}m'.format(dist / h))

while not (cv2.waitKey(1) & 0xFF == ord('q')):
	pass
	
cv2.destroyAllWindows()