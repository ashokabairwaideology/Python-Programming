import cv2
import numpy as np
url = "Your IP Address/video"
cp = cv2.VideoCapture(url)
while(True):
    camera, frame = cp.read()
    if frame is not NoneISO 8601 weekday (1-7)	1	:
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()

#install ipwebcam  in mobile and connect same network
