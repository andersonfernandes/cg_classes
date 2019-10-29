import cv2
import numpy as np
from matplotlib import pyplot as plot

image = cv2.imread('./img/babuino.jpg')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('./img/babuinoGray.jpg', grayImage)
cv2.imshow('Imagem Cinza', grayImage)

plot.hist(grayImage.ravel(), 256, [0,256])
#plot.savefig('./img/histogramGray.jpg')
plot.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
