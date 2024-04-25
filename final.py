import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import cv2
import numpy as np
import time
import PoseModule as pm

def start_exercise(exercise):
    if exercise == "Bicep Curl":
        cap = cv2.VideoCapture("me.mp4")
        detector = pm.poseDetector()
        count = 0
        dir = 0
        pTime = 0

        while True:
            success, img = cap.read()
            img = cv2.resize(img, (540, 960))

            # img = cv2.imread("img3.webp")
            # img= cv2.resize(img,(540,360))
            # img=cv2.flip(img,1)
            img = detector.findPose(img, False)
            lmList = detector.getPosition(img, False)
            # print(lmList)
            if len(lmList) != 0:
                angle = detector.findAngle(img, 12, 14, 16)  # Right
                # detector.findAngle(img, 11, 13, 15) #Left

                per = np.interp(angle, (30, 130), (100, 0))
                bar = np.interp(angle, (40, 130), (100, 500))
                # print(angle, per)

                if per == 100:
                    if dir == 0:
                        count += 0.5
                        dir = 1
                if per == 0:
                    if dir == 1:
                        count += 0.5
                        dir = 0
                print(count)

                if per < 100 and per > 0:
                    feedback_text = "Curl more"
                else:
                    feedback_text = ""

                cv2.rectangle(img, (450, 100), (500, 500), (0, 0, 0), 3)
                cv2.rectangle(img, (450, int(bar)), (500, 500), (0, 0, 0), cv2.FILLED)
                cv2.putText(img, f'{int(per)}%', (380, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
                cv2.putText(img, feedback_text, (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 3)

                cv2.rectangle(img, (0, 600), (130, 700), (0, 0, 0), cv2.FILLED)
                cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)

            cv2.imshow("Image", img)
            cv2.waitKey(1)

    elif exercise == "Squats":
        cap = cv2.VideoCapture("4.mp4")
        detector = pm.poseDetector()
        count = 0
        dir = 0
        pTime = 0

        while True:
            success, img = cap.read()
            img = cv2.resize(img, (432, 768))

            # img = cv2.imread("img3.webp")
            # img= cv2.resize(img,(540,360))
            img=cv2.flip(img,1)
            img = detector.findPose(img, False)
            lmList = detector.getPosition(img, False)
            # print(lmList)
            if len(lmList) != 0:
                angle = detector.findAngle(img, 23, 25, 27)  # Right
                # detector.findAngle(img, 24, 26, 28) #Left

                per = np.interp(angle, (75, 175), (100, 0))
                bar = np.interp(angle, (40, 130), (100, 500))
                # print(angle, per)

                if per == 100:
                    if dir == 0:
                        count += 0.5
                        dir = 1
                if per == 0:
                    if dir == 1:
                        count += 0.5
                        dir = 0
                print(count)

                if per < 100 and per > 0:
                    feedback_text = "Go deeper"
                else:
                    feedback_text = ""

                cv2.rectangle(img, (350, 100), (500, 500), (0, 0, 0), 3)
                cv2.rectangle(img, (350, int(bar)), (500, 500), (0, 0, 0), cv2.FILLED)
                cv2.putText(img, f'{int(per)}%', (300, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
                cv2.putText(img, feedback_text, (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 3)

                cv2.rectangle(img, (0, 600), (100, 700), (0, 0, 0), cv2.FILLED)
                cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)

            cv2.imshow("Image", img)
            cv2.waitKey(1)

def start_selected_exercise():
    exercise = exercise_var.get()
    if exercise:
        start_exercise(exercise)
    else:
        messagebox.showerror("Error", "Please select an exercise.")

root = tk.Tk()
root.title("Exercise Tracker")

root.geometry("400x300")

root.configure(bg="#f0f0f0")

root.padding = 10


exercise_var = tk.StringVar()
exercise_var.set("Bicep Curl")

exercise_label = ttk.Label(root, text="Select Exercise:", foreground="black")
exercise_label.pack(pady=(root.padding, 0))

bicep_curl_radio = ttk.Radiobutton(root, text="Bicep Curl", variable=exercise_var, value="Bicep Curl")
bicep_curl_radio.pack(pady=(0, root.padding))

squats_radio = ttk.Radiobutton(root, text="Squats", variable=exercise_var, value="Squats")
squats_radio.pack(pady=(0, root.padding))

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=(0, root.padding))

start_button = ttk.Button(button_frame, text="Start Exercise", command=start_selected_exercise)
start_button.pack(pady=10, padx=20, ipadx=10, ipady=5)

root.mainloop()
