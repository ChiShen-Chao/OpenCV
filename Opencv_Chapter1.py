# load images, videos or webcam
import cv2

#print("Package Imported")   #test opencv install success

#=====load image==========
'''
img = cv2.imread(".jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)
'''

#=====load video==========
'''
cap = cv2.VideoCapture(".mp4")


while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    # press 'q' to close    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''

#=====webcam==========
# 0 means the default webcam;
# 3 = width, 4 = height
cap = cv2.VideoCapture(0)
# width
cap.set(3, 640)
# height
cap.set(4, 480)
# brightness
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break