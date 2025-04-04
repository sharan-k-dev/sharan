import cv2
import os

#readingv an image
img = cv2.imread(os.path.join('.','data','boards.jpg'))
print(img.shape)
#img = cv2.resize(img,(500,700))
#line
line = cv2.line(img,(100,200),(300,400),(0,0,0),3)

#rectangle
rect = cv2.rectangle(img,(250,350),(400,500),(255,0,0),-1)

#circle 
circle = cv2.circle(img,(650,500),100,(0,0,255),5)

#text
text = cv2.putText(img,'just explore',(500,400),cv2.FONT_HERSHEY_COMPLEX,3,(0,255,0),2)
#visualising the images
cv2.imshow('frame',img)
cv2.waitKey(0)