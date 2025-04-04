import numpy as np
import os
import cv2

org = cv2.imread(os.path.join('.','data','dogs.jpg'))
org = cv2.resize(org,(700,900))
edge = cv2.Canny(org,50,150)
edge_d = cv2.dilate(edge,np.ones((5,5),dtype = np.int8))
edge_e = cv2.erode(edge,np.ones((1,1),dtype = np.int8))

cv2.imshow('original',org)
cv2.imshow('edge detected',edge)
cv2.waitKey(0)
cv2.imshow('edge detected',edge_d)
cv2.waitKey(0)
cv2.imshow('edge detected',edge_e)