import cv2
import numpy as np

image = cv2.imread('./img/Origin_of_Species.jpg', 0)
cv2.imshow('Original', image)

image = cv2.GaussianBlur(image, (3,3), 0)
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)

cv2.imshow("Adaptative Mean Threshold", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
