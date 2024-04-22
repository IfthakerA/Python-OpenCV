import cv2
import numpy as np

#Gets the lines around the shapes
def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True) #finds edges
            print(len(approx))
            objCor = len(approx)
            x, y, w ,h = cv2.boundingRect(approx)

            if objCor == 3: objectType = 'Tri'
            elif objCor == 4:
                aspectRatio = w/float(h)
                if aspectRatio > 0.95 and aspectRatio < 1.05 : objectType ='Square'
                else: objectType = 'Reactangle'
            elif objCor > 4 : objectType = "Circles"
            else: objectType ='None'

            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(imgContour, objectType,
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_ITALIC, 0.8, (0,0,0), 2)
path = 'resources/shapes.png'
img = cv2.imread(path)
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50,50)
imgBlank = np.zeros_like(img)

getContours(imgCanny)

cv2.imshow("Original", img)
cv2.imshow('Gray', imgGray)
cv2.imshow('Blur', imgBlur)
cv2.imshow('Canny', imgCanny)
cv2.imshow('blank', imgBlank)
cv2.imshow('contour', imgContour)
cv2.waitKey(0)