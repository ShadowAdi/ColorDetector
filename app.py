import cv2
from utils import get_limit
from PIL import Image



vid = cv2.VideoCapture(0)
color=[0,255,0] 
while True:
    ret, frame = vid.read() 

    hsvImage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerLimit,upperLimit=get_limit(color=color)
    mask=cv2.inRange(hsvImage,lowerLimit,upperLimit)

    mask_=Image.fromarray(mask)
    bbox=mask_.getbbox()

    if bbox is not None:
        x1,y1,x2,y2=bbox
        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),5)

    cv2.imshow('frame', frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break



vid.release() 
cv2.destroyAllWindows() 