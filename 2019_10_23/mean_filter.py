import cv2
import numpy as np

image = cv2.imread('./img/shirt.jpg')
kernel = np.ones((5, 5), np.float32)/25

filtered_image = cv2.filter2D(image, -1, kernel)

cv2.imshow("Original Image", image)
cv2.imshow("Filtered Image", filtered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
