import cv2
import numpy as np
from matplotlib import pyplot as plot

image = cv2.imread('./img/vale.png', 0)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
image_eq = clahe.apply(image)

cv2.imshow('Original', image)
cv2.imshow('Equalizada', image_eq)

cv2.waitKey(0)
cv2.destroyAllWindows()
