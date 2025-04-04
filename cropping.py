import os
import cv2

#visualising the image
img = cv2.imread(os.path.join('.','data','dogs.jpg'))

cv2.imshow('frame',img)
cv2.waitKey(0)
print(img.shape)

#resisimng the image:
resised_image = cv2.resize(img,(720,490))

cv2.imshow('resised_frame',resised_image)
cv2.waitKey(0)
print('original image',resised_image.shape)

#cropping the image:

cropped_image = img[220:900,100:870]
cv2.imshow('frame',cropped_image)
cv2.waitKey(0)
print('cropped image',cropped_image.shape)