import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./img/green_background.jpg')

lower_green = (0, 140, 0)
upper_green = (130, 255, 130)
mask = cv2.inRange(image, lower_green, upper_green)
segmented_image = cv2.bitwise_and(image, image, mask=255-mask)

cv2.imshow("Segmented Image", segmented_image)
cv2.imwrite("./img/segmented_green_background_image.png", segmented_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
