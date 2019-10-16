import cv2
import numpy as np

image = cv2.imread('./img/brasilia.png', 0)

rows, cols = image.shape

M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rotated_image = cv2.warpAffine(image, M, (cols, rows))

cv2.imshow('Rotation 90 degrees', rotated_image)

cv2.waitKey()
cv2.destroyAllWindows()

