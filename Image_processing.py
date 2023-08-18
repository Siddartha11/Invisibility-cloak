import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
time.sleep(3)
background=0
for i in range(30):
	ret,background = cap.read()


while(cap.isOpened()):
	ret, img = cap.read()
	
	
	
	# Converting image to HSV color space.
	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	
	
	# Defining lower range for red color detection.
	lower_red = np.array([0,120,70])
	upper_red = np.array([10,255,255])
	mask1 =cv2.inRange(hsv,lower_red,upper_red)
	
	# Defining upper range for red color detection
	lower_red = np.array([170,120,70])
	upper_red = np.array([180,255,255])
	mask2 = cv2.inRange(hsv,lower_red,upper_red)

	
	# Addition of the two masks to generate the final mask.
	mask = mask1+ mask2

	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
	
	# Replacing pixels corresponding to cloak with the background pixels.
	img[np.where(mask==255)] = background[np.where(mask==255)]
	cv2.imshow('fill as you want',img)
	k = cv2.waitKey(10)
	if k == 27 :#fill in the blank (fill the ascii value of key you like :0 ex->27 for escape key)
		break
