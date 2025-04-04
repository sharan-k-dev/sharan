import os
import cv2
#reading image
#reading the image
image_path = os.path.join('.','data','parrot.jpg')
image_org = cv2.imread(image_path)
image_org = cv2.resize(image_org,(400,600))

#blurring
k_size = 7
classic = cv2.blur(image_org,(k_size,k_size))
guassian = cv2.GaussianBlur(image_org,(k_size,k_size),5)
median = cv2.medianBlur(image_org,k_size)

#visualising
cv2.imshow('classic_blur',classic)
cv2.imshow('guassian_blur',guassian)
cv2.imshow('median_blur',median)

cv2.waitKey(0)

#removing noise in an image
img = cv2.imread(os.path.join('.','data','noise_sample.jpg'))
median = cv2.medianBlur(img,7)

cv2.imshow('original image',img)
cv2.imshow('noise removed image',median)
cv2.waitKey(0)