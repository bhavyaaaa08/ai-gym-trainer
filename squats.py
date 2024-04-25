import cv2
import numpy as np
import time
import PoseModule as pm

cap= cv2.VideoCapture("3.mp4")
detector= pm.poseDetector()
count=0
dir=0
pTime =0

while True:
    success, img= cap.read()
    img=cv2.resize(img,(432,768))

    # img = cv2.imread("img3.webp")
    # img= cv2.resize(img,(540,360))
    # img=cv2.flip(img,1)
    img= detector.findPose (img, False)
    lmList= detector.getPosition(img, False)
    # print(lmList)
    if len(lmList)!=0:
        angle= detector.findAngle(img, 23,25,27) #Right
        # detector.findAngle(img, 24, 26, 28) #Left

        per= np.interp(angle, (60, 160), (100, 0))
        bar= np.interp(angle, (40, 130), (100, 500))
        #print(angle, per)

        if per ==100:
            if dir==0:
                count+= 0.5
                dir=1
        if per==0:
            if dir ==1:
                count+= 0.5
                dir= 0
        print(count)

        if per < 100 and per>0:
            feedback_text = "Go deeper"
        else:
            feedback_text = ""

        cv2.rectangle(img, (350,100), (500, 500), (0,0,0), 3)
        cv2.rectangle(img, (350, int(bar)), (500, 500), (0,0,0), cv2.FILLED)
        cv2.putText(img, f'{int(per)}%', (300, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0),5)
        cv2.putText(img, feedback_text, (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 3)



        cv2.rectangle(img, (0,600), (100, 700), (0,0,0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45,670), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0),5)
    cTime= time.time()
    fps= 1/(cTime-pTime)
    pTime= cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)