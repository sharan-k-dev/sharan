import os
import cv2

image_path = os.path.join('.','data','dog.png')

#reading an image and getting its info:

img = cv2.imread(image_path)

print(type(img))

print(img.shape)

#write an image:

cv2.imwrite(os.path.join('.','data','image_outs.png'),img)

#visualize the image
cv2.imshow('image_frame',img)
cv2.waitKey(2000)

#video
#reading the video from the file system
video = cv2.VideoCapture(os.path.join('.','data','video.mp4'))
#visualising the video
ret = True

while ret == True:
    
    ret,frame = video.read()
    cv2.imshow('frames',frame)
    cv2.waitKey(33)#frame rate = 30 (i'e:1000%30 =33)
video.release()
cv2.destroyAllWindows