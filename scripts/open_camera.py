import cv2 as cv
import numpy as np



source=1

cap = cv.VideoCapture(source) 
if cap is None or not cap.isOpened():
    print('Warning: unable to open video source: ', source)
else:
    print('Opened camera: ',source)

while True:
    _, image = cap.read()
    image=cv.flip(image, 2)
    cv.imshow('Image', image)

    
    key=cv.waitKey(1)
    
    if key ==27:
        break

cap.release()
cv.destroyAllWindows()