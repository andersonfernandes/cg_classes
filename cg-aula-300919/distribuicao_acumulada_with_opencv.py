import cv2
import numpy as np
from matplotlib import pyplot as plot

image = cv2.imread('./img/vale.png', 0)

image_eq = cv2.equalizeHist(image)
cv2.imshow("Original", image)
cv2.imshow("Equalized", image_eq)

cv2.waitKey(0)
cv2.destroyAllWindows()
