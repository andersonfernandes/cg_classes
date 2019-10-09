import cv2
import numpy as np

image = cv2.imread('./img/louvre.jpg')

kernel_sharpenning = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
filtered_image = cv2.filter2D(image, -1, kernel_sharpenning)

cv2.imshow("Original Image", image)
cv2.imshow("Filtered Image", filtered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
