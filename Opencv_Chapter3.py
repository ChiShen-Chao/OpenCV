# learn how to crop the image

import cv2
import numpy

img = cv2.imread(".jpg")
print(img.shape)
# ("height", "width", "channels(BGR)")

# resize the image("width", "heigh")
imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)

# cropped the image 
# notice the axis is different in opencv system
#[0:300] => y axis and from top to low
#[300:500] => x axis and go right
imgCropped = img[0:300, 300:500]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)