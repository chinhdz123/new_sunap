from calib import *
import cv2
import imutils
img = cv2.imread()
frame = imutils.resize(calib(r'D:\Robot\Sunap\new_sunap\tmp\check_sunap\6.jpg'),width=800)

frame = cv2.imshow('calib',frame)
cv2.waitKey(0)