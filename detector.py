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
k=0


import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os
from matplotlib import pyplot as plt 


num=1
video_capture=0

def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

def assistant_speaks(output):
 global num
 num +=1
 #print("Safety Assistant : ", output)
 toSpeak = gTTS(text=output, lang='en-US', slow=False)
 file = str(num)+".mp3"
 toSpeak.save(file)
 playsound.playsound(file, True)
 os.remove(file)

def pie_chart():
    from datetime import date
    today = date.today() 
    people = ['WITH MASK', 'WITHOUT MASK']
    data = [count_p_m,count_p_wm]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(data, labels = people, autopct='%1.1f%%')
    #plt.show()
    fig.savefig((str(today)+'_pie_plot.jpg'), bbox_inches='tight', dpi=150)

 
def camera():
    #assistant_speaks("Hi! I'm your face mask detector!")
    global video_capture, count_m, count_wm,count_p_m,count_p_wm
    cam=True
    count_wm=0
    count_m=0
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
                    assistant_speaks("Great! You have got your mask on! Kindly use the santizer! Have a safe day!")
                    cam=False
                    count_p_m+=1
            if max(mask,withoutMask)*100>95 and label=="No Mask":
                
                count_wm+=1
                if count_wm>25:
                    assistant_speaks("Kindly wear a mask! Your not allowed to enter!")
                    count_p_wm+=1
                    cam=False
            label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
            cv2.putText(frame, label, (x, y- 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h),color, 2)
            # Display the resulting frame
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(1)& 0xFF == ord('s'):
            global k
            k=1
            break
    video_capture.release()
    cv2.destroyAllWindows()
        

def start():
    global k
    k=0
    while(1):
        camera()
        count_m=0
        count_wm=0
        
        if(k==1):
            break


from tkinter import *
top = Tk()   
top.geometry("600x700")
top.configure(background="salmon")
but1 = Label(top, text = "CLICK ON THE BELOW BUTTON TO START THE DETECTOR").place(x = 150,y = 50)
photo = PhotoImage(file = "detect.png")
b1=Button(top, text="DETECT MASKS", command=start,image=photo,fg='black',bg='turquoise4',font=('times',15,'bold')).place(x=110,y=100)
but1 = Label(top, text = "CLICK ON THE BELOW BUTTON TO GENERATE PIE CHART").place(x = 150,y = 300)
photo1 = PhotoImage(file = "pie_chart.png")
b2=Button(top, text="GENERATE PIE CHART", command=pie_chart,image=photo1,fg='black',bg='turquoise4',font=('times',15,'bold')).place(x=150,y=350)
b3=Button(top, text="EXIT", command=sequence(top.destroy, sys.exit), fg='black',bg='turquoise4',font=('times',15,'bold')).place(x=270,y=550) 
top.mainloop()



     
 



