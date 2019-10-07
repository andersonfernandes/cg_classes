import cv2
import numpy as np
from matplotlib import pyplot as plot

image = cv2.imread('./img/vale.png', 0)
cv2.imshow("Original", image)

hist, bins = np.histogram(image.flatten(), 256, [0, 256])

cdf = hist.cumsum()
cdf_norm = cdf * hist.max()/cdf.max()

cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
image_eq = cdf[image]
cv2.imshow("Image Equalized", image_eq)

plot.plot(cdf_norm, color = 'b')
plot.hist(image_eq.flatten(), 256, [0,256], color = 'r')
plot.xlim([0,256])
plot.legend(('cdf. histogram'), loc = 'upper left')
plot.savefig('./img/cumhist.png')
plot.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
