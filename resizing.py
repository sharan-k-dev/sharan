import os
import cv2

image_path = os.path.join('.','data','dog.png')

#reading an image and getting its info:
img = cv2.imread(image_path)
print(type(img))
print('original image',img.shape)  


#resisimng the image:
resised_image = cv2.resize(img,(720,490))
print('resized image',resised_image.shape)

cv2.imshow('resised_frame',img)
cv2.waitKey(0)

cv2.imshow('resised_frame',resised_image)
cv2.waitKey(0)
print('resized image',resised_image.shape)

