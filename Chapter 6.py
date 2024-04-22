import cv2
import numpy as np

img = cv2.imread("resources/Lena.png")

#imgHor = np.hstack((img, img)) # stack images next to each other

#imgVer = np.vstack((img, img)) # stack vertical

#cv2.imshow("Horizontal", imgHor)
#cv2.imshow("Vertical", imgVer)

cv2.waitKey(0)