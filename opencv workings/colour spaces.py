import os
import cv2

#reading the image
image_path = os.path.join('.','data','parrot.jpg')
image_org = cv2.imread(image_path)
image_org = cv2.resize(image_org,(500,600))
#visualizing the original image
cv2.imshow('frame_original',image_org)
cv2.waitKey(0)

#image conversion
image_rgb = cv2.cvtColor(image_org,cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image_org,cv2.COLOR_BGR2GRAY)
image_hsv = cv2.cvtColor(image_org,cv2.COLOR_BGR2HSV)

#visualizing the rgb converted image
cv2.imshow('frame_rgb',image_rgb)
cv2.waitKey(0)


#visualizing the grayscale converted image
cv2.imshow('frame_gray',image_gray)
cv2.waitKey(0)


#visualizing the rgb converted image
cv2.imshow('frame_hsv',image_hsv)
cv2.waitKey(0)
