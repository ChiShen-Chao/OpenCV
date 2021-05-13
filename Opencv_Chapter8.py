# contours and shape detection
import cv2
import numpy as np
from numpy.core.numeric import _array_equal_dispatcher

# add the stacking function from chapter6
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

# define another function to find the contour
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        # defind the minimum to make sure it won't detect any noise 
        if area > 500:
            # -1 means print all
            cv2.drawContours(imgContour,cnt, -1, (255, 0, 0), 3)
            # calculate the curve length
            peri = cv2.arcLength(cnt, True)
            print(peri)
            # approximate how any corner point we have
            # (contours, resolution(multiply the arc length), True means we expect all the shapes are closed)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            # create the object corner
            objCor = len(approx)
            #########################################
            #Important!!!!!!!!!!!!!!!!!!!
            # generage the bounding box
            x, y, w, h = cv2.boundingRect(approx)

            # categorize the shape
            if objCor == 3 : 
                objectType = "Tri"
            # 2 condition in 4 points so we use the aspact ration to define
            elif objCor == 4:
                aspRatio = w / float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = "Square"
                else: objectType = "Rectangle"
            elif objCor > 4:
                objectType = "Circle"
                
            else: objectType = "Not yet"


            # plot the bunding box
            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 0, 0), 2)
            # plot the category (text, adn set the position)
            cv2.putText(imgContour, objectType, 
                        (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX,
                        0.7, (0, 0, 0), 2)


img = cv2.imread(".png")
# create a copy of original image
imgContour = img.copy()

# first of all we need to pre-process the image (transfer to grayscale, and add some blur)
imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),1)

# second we use canny to find the edge
imgCanny = cv2.Canny(imgBlur, 50, 50)

# then we plot the contours(see the defined function above)
getContours(imgCanny)


# this is for the blank
imgBlank = np.zeros_like(img)
imgStack = stackImages(0.7,([img, imgGray, imgBlur],
                            [imgCanny, imgContour, imgBlank]))

cv2.imshow("Image stuck", imgStack)
'''
cv2.imshow("Original", img)
cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
'''
cv2.waitKey(0)