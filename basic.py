import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
import time
import mysql.connector

model=YOLO('yolov8s.pt')

# Connecting MySQL server

# host = "127.0.0.1"
port = "3306"
user_name = "root"
pwd = "root"
dbname = "park"
mydb = mysql.connector.connect(
#   host= host,
  user = user_name,
  password=pwd,
#   database= dbname
)
print(mydb.is_connected())

# Putting cursor in MySQL
cursorObject = mydb.cursor()

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        # print(colorsBGR)
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap=cv2.VideoCapture('parking1.mp4')

my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")
   




area9=[(511,327),(557,388),(603,383),(549,324)]
flag9 = 1



while True:    
    ret,frame = cap.read()
    if not ret:
        break
    
    frame=cv2.resize(frame,(1020,500))

    results=model.predict(frame)
    # print(results)
    a=results[0].boxes.boxes
    px=pd.DataFrame(a).astype("float")
    # print(px)
   
    list9=[]
   
    
    for index,row in px.iterrows():
        # print(row)
 
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        if 'car' in c:
            cx=int(x1+x2)//2
            cy=int(y1+y2)//2

       
      
            results9=cv2.pointPolygonTest(np.array(area9,np.int32),((cx,cy)),False)
            if results9>=0:
               cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
               list9.append(c)  
        
              
            
    
    a9=len(list9)
    print(f"Flag: {flag9}")
    print(f"a9: {a9}")
    if(a9 != flag9):
        if(a9 == 0):
                query = "UPDATE sys.slots SET avl= 'y' where slot_id = 9;"
                cursorObject.execute(query)
                print("a9 = 0")
                # display = "select * from sys.slots where slot_id = 9"
                # cursorObject.execute(display)
        else:
            query = "UPDATE sys.slots SET avl= 'n' where slot_id = 9;"
            cursorObject.execute(query)
            print("a9 = 1")
            # display = "select * from sys.slots where slot_id = 9"
            # cursorObject.execute(display)
    flag9 = a9
    
  
    if a9==1:
        cv2.polylines(frame,[np.array(area9,np.int32)],True,(0,0,255),2)
        cv2.putText(frame,str('9'),(591,398),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    else:
        cv2.polylines(frame,[np.array(area9,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,str('9'),(591,398),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
   
    # while True:
    # key = cv2.waitKey(1) & 0xFF
    # if key == ord('q'):
    #     break

    

    cv2.imshow("RGB", frame)

    if cv2.waitKey(0)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()
mydb.close()
print(mydb.is_connected())
#stream.stop()


    




