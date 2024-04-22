import cv2

import numpy as np
print("Package Imported")
#image displaying
#img = cv2.imread("resources/Lena.png")  #imports image from resource folder

#cv2.imshow("Output", img)#displays image

#cv2.waitKey(0) #delays the image so its displayed longer 0 IS INFINTE

#END


# DISPLAYS VIDEO

#cap = cv2.VideoCapture("resources/test.mp4")#

#while True:
    #success, img = cap.read() #loop while there is a vidoe save to var img
    #cv2.imshow("Video", img) # displays video

    #if cv2.waitKey(1) & 0xDD ==ord('q') : # add delays and looks for q to break
        #break

        #END

#SHOWS WEBCAM

#cap = cv2.VideoCapture(0) # uses webcam 0 is default one 1.2,3 can be used for many webcams

#cap.set(3, 640) # set parameters width id is 3
#cap.set(4,480) #set height id is 4
#cap.set(10, 100) #set brightness id is 10

#while True:
    #success, img = cap.read() #loop while there is a vidoe save to var img
    #cv2.imshow("Video", img) # displays video

    #if cv2.waitKey(1) & 0xDD ==ord('q') : # add delays and looks for q to break
        #break

#img = cv2.imread("resources/Lena.png")
#kernel = np.ones((5,5), np.uint8)

#imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #makes image gray

#imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0) #ksize is the amount o blur odd number only

#imgCanny = cv2.Canny(img, 150, 200) # can see edges of images

#imgDialation = cv2.dilate(imgCanny, kernel, iterations=1) #dialations is like edges b

#imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

#cv2.imshow("Gray image", imgGray)
#cv2.imshow("Blur image", imgBlur)
#cv2.imshow("Canny image", imgCanny)
#cv2.imshow("Dialtion image", imgDialation)
#cv2.imshow('Eroded image', imgEroded)
#cv2.waitKey(0)

img = cv2.imread("resources/Lena.png")
print(img.shape) #shows image size

imgResize = cv2.resize(img, (500, 400)) #resizes image (w, h)
print(imgResize.shape)

imgCropped = img[0:400, 200:500] #crops image (h,w)

cv2.imshow("image", img)
cv2.imshow("resized image", imgResize)
cv2.imshow("cropped image", imgCropped)
cv2.waitKey(0)