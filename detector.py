import cv2
import os
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
import sys
 
cascPath = "haarcascade_frontalface_alt2.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
model = load_model("mask_detection.h5")
count_m=0
count_wm=0
count_p_m=0
count_p_wm=0

import speech_recognition as sr # importing speech recognition package from google api
# from pygame import mixer
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os
num=1
video_capture=0
def assistant_speaks(output):
 global num
 num +=1
 print("Safety Assistant : ", output)
 toSpeak = gTTS(text=output, lang='en-US', slow=False)
 file = str(num)+".mp3"
 toSpeak.save(file)
 playsound.playsound(file, True)
 os.remove(file)

def get_audio():
 r = sr.Recognizer()
 audio = ''
 with sr.Microphone() as source:
     print("Speak...")
     audio = r.listen(source, phrase_time_limit=5)
     print("Stop.")
 try:
     text = r.recognize_google(audio)
     print("You : ", text)
     return text
 except:
     assistant_speaks("Kindly repeat!")
     return ""

 
def camera():
    global video_capture, count_m, count_wm,count_p_w,count_p_wm
    cam=True
    count_wm=0
    count_m=0
    count_p_wm=0
    count_p_m=0
    video_capture = cv2.VideoCapture(0)
    while (cam):
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(60, 60),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
        faces_list=[]
        preds=[]
        for (x, y, w, h) in faces:
            face_frame = frame[y:y+h,x:x+w]
            face_frame = cv2.cvtColor(face_frame, cv2.COLOR_BGR2RGB)
            face_frame = cv2.resize(face_frame, (224, 224))
            face_frame = img_to_array(face_frame)
            face_frame = np.expand_dims(face_frame, axis=0)
            face_frame =  preprocess_input(face_frame)
            faces_list.append(face_frame)
            if len(faces_list)>0:
                preds = model.predict(faces_list)
            for pred in preds:
                (mask, withoutMask) = pred
            label = "Mask" if mask > withoutMask else "No Mask"
            color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
            if max(mask,withoutMask)*100>95 and label=="Mask":
                
                count_m+=1
                if count_m>25:
                    assistant_speaks("Great! You have got your mask on! Kindly use the santizer!")
                    cam=False
                    count_p_m+=1
            if max(mask,withoutMask)*100>95 and label=="No Mask":
                
                count_wm+=1
                if count_wm>25:
                    assistant_speaks("Kindly wear a mask! Your not allowed to enter the premesis!")
                    count_p_wm+=1
                    cam=False
            label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
            cv2.putText(frame, label, (x, y- 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h),color, 2)
            # Display the resulting frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break

def voice():
    while(1):
        text = get_audio().lower()
        if text == 0:
            continue
        if "hi" in str(text) or "hai" in str(text):
            camera()
            count_m=0
            count_wm=0
            video_capture.release()
            cv2.destroyAllWindows()
            break




from tkinter import *
top = Tk()   
top.geometry("600x800")
top.configure(background="salmon")
name = Label(top, text = "ARE YOU WEARING A MASK? CLICK ON THE BUTTON AND SAY HI!").place(x = 120,y = 50)
photo = PhotoImage(file = "speak.png")
b1=Button(top, text="DETECT MASKS", command=voice,image=photo,fg='black',bg='turquoise4',font=('times',15,'bold')).place(x=50,y=100)
b2=Button(top, text="EXIT", command=top.destroy, fg='black',bg='turquoise4',font=('times',15,'bold')).place(x=250,y=650) 
top.mainloop()



     
 



