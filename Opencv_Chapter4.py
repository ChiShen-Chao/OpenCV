# this chapter will learn how to draw shape on image
import cv2
import numpy as np

# create a image with all zero, zero in opencv means block
#img = np.zeros((512,512))

#create a image with color 
img = np.zeros((512,512,3), np.uint8)

# set the color as blue
#img[:] = 255,0 ,0

# draw a line on the image
#((start), (end), (color), thickness)
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

# draw rectangle. Set the thickness with number or use "cv2.FILLED" to fill the rectangle
cv2.rectangle(img, (0, 0), (150, 300), (255,0 ,0), 2)

# draw circle.
cv2.circle(img, (400, 200), 50, (0, 0, 255), 3)

# write some text
cv2.putText(img, "I am Jason", (120,250), cv2.FONT_HERSHEY_COMPLEX, 2, (255,255,255), 1)


# check the dimensionality of our image
#print(img.shape)



cv2.imshow("Image", img)

cv2.waitKey(0)