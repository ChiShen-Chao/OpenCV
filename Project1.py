import cv2
import numpy as np

# set the webcam
cap = cv2.VideoCapture(0)
# width
cap.set(3, 640)
# height
cap.set(4, 480)
# brightness
cap.set(10, 100)

# set the colors list that we want to detect
# we can set multiple colors
myColors = [[19, 25, 191, 30, 146, 255],    ##yellow
            [89, 35, 136, 104, 139, 255],    ##blue
            [101, 53, 136, 179, 106, 255]]     ##red
# if we want the pointing circle change to the specific color, we need to define colors
myColorValues = [[0,255,255],       ## BGR
                 [255, 0, 0],
                 [0, 0, 255]]
# draw the points create the point we want to draw
myPoints = [] #[x, y, colorId]



# find color
def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0   # initial count value
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        #lower = np.array([myColors[0][0:3]])
        #lower = np.array([h_min, s_min, v_min])
        upper = np.array(color[3:6])
        #upper = np.array([myColors[0][3:6]])
        #upper = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask) # get the return value from here
        cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED) # draw the circle to point our color
        #cv2.imshow(str(color[0]), mask) # window name will be the first number of the color
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
            

        count += 1 # everytime it count we need to know which color we count
    return newPoints

# make bounding box for our color
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0 #just in case if there is not detecting anything, we still need to return something
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            #cv2.drawContours(imgResult,cnt, -1, (255, 0, 0), 3) # after we get the point at our detecting color, we don't need the bounding box
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y # return the position of top(tip) centor of the color

# draw our points
def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()  # for the bounding box
    newPoints = findColor(img, myColors, myColorValues)
    
    # check if our new point is there or not
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)

    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

'''
yellow
min, max
19 30
25 146
191 255
'''

'''
blue
89 104
35 139
136 255
'''

'''
red
101 179
53 106
136 255
'''