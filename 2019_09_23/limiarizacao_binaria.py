import cv2
import numpy as np

image = cv2.imread('./img/Origin_of_Species.jpg', 0)
cv2.imshow('Original', image)

ret, tresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Limiarizacao Binaria', tresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
