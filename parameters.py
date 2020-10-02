import cv2

def empty(a):
	pass

img = cv2.imread('Parameters.png')[:160, :, :]
img = cv2.resize(img, (340, 120))

def takeVal():

    cv2.namedWindow('Parameters')
    cv2.imshow('Parameters', img)
    cv2.resizeWindow('Parameters', 640, 240)
    cv2.createTrackbar('HUE Min', 'Parameters', 0, 255, empty)
    cv2.createTrackbar('HUE Max', 'Parameters', 255, 255, empty)
    cv2.createTrackbar('SAT Min', 'Parameters', 0, 255, empty)
    cv2.createTrackbar('SAT Max', 'Parameters', 255, 255, empty)
    cv2.createTrackbar('VALUE Min', 'Parameters', 0, 255, empty)
    cv2.createTrackbar('VALUE Max', 'Parameters', 255, 255, empty)
    cv2.createTrackbar('Thresh1', 'Parameters', 150, 255, empty)
    cv2.createTrackbar('Thresh2', 'Parameters', 225, 255, empty)

    while True:

        h_min = cv2.getTrackbarPos('HUE Min', 'Parameters')
        h_max = cv2.getTrackbarPos('HUE Max', 'Parameters')
        s_min = cv2.getTrackbarPos('SAT Min', 'Parameters')
        s_max = cv2.getTrackbarPos('SAT Max', 'Parameters')
        v_min = cv2.getTrackbarPos('VALUE Min', 'Parameters')
        v_max = cv2.getTrackbarPos('VALUE Max', 'Parameters')
        threshold1 = cv2.getTrackbarPos('Thresh1', 'Parameters') 
        threshold2 = cv2.getTrackbarPos('Thresh2', 'Parameters')

        if cv2.waitKey(1) &0xFF == ord('q'):
            cv2.destroyWindow('Parameters')
            break

    return (h_min, h_max, s_min, s_max, v_min, v_max, threshold1, threshold2) 