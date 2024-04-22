import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8) #creates black background zeros are black 3 give it the ability to have colour
#print(img)

#img[:] = 255, 0, 0 #colours the while imahe [:] blue

cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
#makes a line (image, starting pointm end point, colour, thickness)

cv2.rectangle(img, (0,0), (250, 350), (0, 0, 255), 2)

cv2.circle(img, (400, 50), 30, (255,255,0), 5)

cv2.putText(img, "OPENCV ", (300, 200), cv2.FONT_ITALIC, 1, (0,150,0), 1)
#adds text

cv2.imshow("image", img)
cv2.waitKey(0)