import cv2
import numpy as np

image = cv2.imread('./img/shirt.jpg')

filtered_image = cv2.medianBlur(image, 5)

cv2.imshow("Original Image", image)
cv2.imshow("Filtered Image", filtered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
