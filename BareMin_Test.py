'''
   -- ClassID: 1
   -- Confidence: 0.981095
   -- Left:    0
   -- Top:     39.8322
   -- Right:   338.71
   -- Bottom:  637.397
   -- Width:   338.71
   -- Height:  597.565
   -- Area:    202401
   -- Center:  (169.355, 338.614)
'''


import jetson.inference
import jetson.utils
import cv2

net = jetson.inference.detectNet("ssd-mobilenet-v2",threshold = 0.5)

cap = cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=400, height=400, format=(string)NV12, framerate=(fraction)20/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink' , cv2.CAP_GSTREAMER) 
#cap.set(3,640)
#cap.set(4,480)

while True:
    success, img = cap.read()
    imgCuda = jetson.utils.cudaFromNumpy(img)

    detections = net.Detect(imgCuda)
    
    for d in detections:
        #print(d)                           #prints the details of the detection like region and so on.
        x1,y1,x2,y2 = int(d.Left),int(d.Top),int(d.Right),int(d.Bottom)    
        className = net.GetClassDesc(d.ClassID)
        cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),2)
        cv2.putText(img,className,(x1+5,y1+15),cv2.FONT_HERSHEY_DUPLEX,0.75,(255,0,255),2)
	

    #img = jetson.utils.cudaToNumpy(imgCuda)
    
    

    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

