__author__ = 'SS'
import cv2
import numpy as np

stream = cv2.VideoCapture(1)
stream.read()
ret, frame = stream.read()
brightness_prev = -1

while ret:
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    brightness = np.mean(hsv_img[:,:,2])
    if (brightness - brightness_prev > 50 and brightness_prev > 40):
        print "Flash!!!"
    brightness_prev = brightness
    cv2.imshow("frame", frame)
    cv2.waitKey(33)
    ret, frame = stream.read()


