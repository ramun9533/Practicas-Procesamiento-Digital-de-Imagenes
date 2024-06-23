import cv2 
import numpy as np 

# reading image 
img = cv2.imread('shapes.png') 

# converting image into grayscale image 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# setting threshold of gray image 
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) 

# using a findContours() function 
contours, _ = cv2.findContours( 
	threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

# list for storing names of shapes 
for contour in contours: 
	# approximating the contour to a polygon 
	approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True) 

	# checking if the contour is a rectangle
	if len(approx) == 4:
		# Calculating the area of the contour
		area = cv2.contourArea(contour)
		# Defining the minimum and maximum area for rectangles (you can adjust these values according to your needs)
		min_area = 500
		max_area = 5000
		# Checking if the area of the contour is within the specified range
		if min_area < area < max_area:
			# using drawContours() function 
			cv2.drawContours(img, [contour], 0, (0, 255, 0), 2) 

# displaying the image after drawing contours 
cv2.imshow('Rectangles', img) 

cv2.waitKey(0) 
cv2.destroyAllWindows()
