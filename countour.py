import cv2
import os

img = cv2.imread(os.path.join('.','data','birds.jpg'))

#finding counters
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
countours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#mapping counters:
i = 0
for cnt in countours:
    if(cv2.contourArea(cnt)>=200):
        '''
        i = i+1
        print('counter number:',i,'area :',cv2.contourArea(cnt))
        cv2.drawContours(img,cnt,-1,(0,255,0),3)
'''
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

#visualize
cv2.imshow('original image',img)
cv2.imshow('gray image',gray)
cv2.imshow('inverse threshold image',thresh)


cv2.waitKey(0)