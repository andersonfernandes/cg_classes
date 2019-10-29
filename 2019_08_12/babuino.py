import cv2
import numpy as np

image = cv2.imread('./img/colors.png')

B, G, R = cv2.split(image)
cv2.imshow('Original', image)
cv2.imshow('Red', R)
cv2.imshow('Green', G)
cv2.imshow('Blue', B)
cv2.waitKey(0)
cv2.destroyAllWindows()

#B, G, R = image[150, 174]
#print(B, G, R)
#print(image.shape)

#cv2.imshow('Figura', image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
