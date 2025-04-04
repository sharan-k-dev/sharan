import os
import cv2
org = cv2.imread(os.path.join('.','data','penguins.jpg'))
org = cv2.resize(org,(400,600))
gray = cv2.cvtColor(org,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,80,255,cv2.THRESH_BINARY)
#adaptive threshold

adapt = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,30)


k_size = 7
blur = cv2.blur(thresh,(k_size,k_size))
ret,thresh2 = cv2.threshold(blur,80,255,cv2.THRESH_BINARY)

cv2.imshow('original image',org)
cv2.imshow('first thresh',thresh)
cv2.imshow('blur image',blur)
cv2.imshow('thresh2 image',thresh2)
cv2.imshow('adaptive threshold',adapt)


cv2.waitKey(0)


