import cv2
import numpy as np
cap = cv2.VideoCapture("C:\\Users\\Gunavathi\\Downloads\\ms video.mp4") # 0- live streaming or we can add the path 
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(gray,50, 150)
    cv2.imshow("Face Detection",frame)
    cv2.imshow("edges",edges)
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
