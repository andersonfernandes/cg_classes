import cv2
import numpy as np

image = cv2.imread('./img/brasilia.png', 0)

flipped_image = cv2.flip(image, 0)

cv2.imshow('Vertical Flip', flipped_image)

cv2.waitKey()
cv2.destroyAllWindows()

