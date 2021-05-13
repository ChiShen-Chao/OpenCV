import cv2
'''
#test opencv install success
print("Package Imported")
'''

'''
# picture load and print test
img = cv2.imread(".jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)
'''
'''
# load video and webcam is the same process the only different is the "path" "video.mp4" or 0
cap = cv2.VideoCapture(".mp4")

while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    # press 'q' to close    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''

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