import cv2
import numpy as np
import math
from object_detection import ObjectDetection

ObjDet = ObjectDetection()

cap = cv2.VideoCapture("Resources\highway_footage.mp4")
count = 0
cp_frame2 = []

tracked_objects = {}
track_id = 0


while True:
    success, frame = cap.read()
    count+=1
    if not success:
        break
    cp_frame = []
    text_frame = []
    
    (obj_id, score, boxes) = ObjDet.detect(frame)
    for box in boxes:
        x,y,w,h = box
        cx = int((x + x+w)/2)
        cy = int((y + y+h)/2)
        cp_frame.append((cx, cy, x, y)) 
        #print("frame", count, " ", x,y,w,h)
        cv2.rectangle(frame,(x,y), (x+w, y+h), (0,0,255), 2)       
                
    if count>0:
        tracked_objects_c = tracked_objects.copy()
        cp_frame_c = cp_frame.copy()

        for obj_id, point2 in tracked_objects_c.items():
            exist = False
            for point in cp_frame_c:
                dist = math.hypot(point2[0] - point[0], point2[1] - point[1])

                if dist < 30:
                    tracked_objects[obj_id] = point
                    exist = True
                    if point in cp_frame:
                        cp_frame.remove(point)
                    continue
            if not exist:
                tracked_objects.pop(obj_id)
                
        for point in cp_frame:
            tracked_objects[track_id] = point
            track_id += 1
    for obj_id, point in tracked_objects.items():
        cv2.circle(frame, (point[0], point[1]), 2, (0,0,255), -1)
        cv2.putText(frame, str(obj_id), (point[2], point[3] -7), 1, 1, (108,179,110), 2)
        
    cv2.putText(frame, str("Press esc key to exit"), (20,20), 1, 2, (0,0,0))
    
    cv2.imshow("Frame", frame)
    cp_frame2 = cp_frame.copy()
    
    if cv2.waitKey(1) & 0xFF == 27:
    
        break
cap.release()
cv2.destroyAllWindows()


