import cv2
import numpy as np

img = cv2.imread("resources/cards.png")
#this isolates a part of the image and makes it flat try diff img
width, height = 250,350
pts = np.float32([[111, 219],[287,188],[154, 482],[352,440]])
#point 1
pts2 = np.float32([[0,0],[width, 0],[height, 0],[width, height]])
#point 2
matrix = cv2.getPerspectiveTransform(pts, pts2)

imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Image", img)

cv2.imshow("Image2", imgOutput)

cv2.waitKey(0)