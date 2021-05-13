# basic image processing 
import cv2
import numpy as np

img = cv2.imread(".jpg")
kernel = np.ones((5,5), np.uint8)

# set the image to the grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# use the  ossian blur function to blur the image
imgBlur = cv2.GaussianBlur(imgGray,(7,7), 0)

# edge detector(canny edge detector) set the thresholds to change the edge
imgCanny = cv2.Canny(img, 150, 200)

# increase the thickness of the edge
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

# opposite to dialation, Eroded make the edge thinner
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(0)