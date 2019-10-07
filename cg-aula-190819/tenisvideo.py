import cv2
import numpy as np

cap = cv2.VideoCapture('./vid/videotenis.avi')

while(cap.grab()):
    _, frame = cap.retrieve()
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([107,177,194])
    upper_yellow = np.array([179,255, 255])
    mask = cv2.inRange(frame, lower_yellow, upper_yellow)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('res',res)

    # Press ESC to close windows
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows

