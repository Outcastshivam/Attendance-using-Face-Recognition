from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x700+0+0")
        self.root.title("Face Recognition System")

        title_label = Label(self.root,text = "FACE RECOGNITION",font=("times new roman", 35, "bold"),bg="white",fg="green")
        title_label.place(x=0,y=0,width=1300,height=45)

        left_img = Image.open(r"Images_Project\FaceRecognition_bg.jpeg")
        left_img = left_img.resize((1280,650),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(left_img)

        left_label = Label(self.root,image = self.photoimg_left)
        left_label.place(x=0,y=46,width=1280,height=650)

        #Button
        btn = Button(self.root,text="FACE DETECTOR",cursor="hand2",command=self.face_recog,font=("times new roman", 18, "bold"),bg="red",fg="white")
        btn.place(x=230, y=480, width=235, height=40)
    #============================attendance==================================================
    def mark_attendance(self,n,yr,i,dep):
        with open("FaceRecognisedAttendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (yr not in name_list) and (dep not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d-%m-%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{dep},{yr},{dtString},{d1},Present")

    #========================face recognition====================================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            if img is None:
                print("Failed to capture image.")
                return []
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                x, y, w, h = int(x), int(y), int(w), int(h)
                if w <= 0 or h <= 0:
                    print(f"Invalid dimensions: w={w}, h={h}")
                    continue
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@1",database="face_recogniser")
                my_cursor=conn.cursor()

                my_cursor.execute("select Student_name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n) if n else "Unknown"

                my_cursor.execute("select Year from student where Student_id="+str(id))
                yr=my_cursor.fetchone()
                yr="+".join(yr) if yr else "Unknown"

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(map(str, i)) if i else "Unknown"

                my_cursor.execute("select dept from student where Student_id="+str(id))
                dep=my_cursor.fetchone()
                dep="+".join(map(str, dep)) if dep else "Unknown"

                
                x, y, w, h = int(x), int(y), int(w), int(h)

                if confidence>77:
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    cv2.putText(img,f"ID:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    cv2.putText(img,f"Year:{yr}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    self.mark_attendance(n,yr,i,dep)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),3)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        if faceCascade.empty():
            print("Failed to load Haarcascade XML file.")
            exit()
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        if not video_cap.isOpened():
            print("Error: Could not open the camera.")

        else:
            while True:
                ret,img=video_cap.read()
                if not ret or img is None or img.size == 0:
                    print("Failed to capture image.")
                    break
                image=recognize(img,clf,faceCascade)
                cv2.imshow("Welcome to Face Recognition",image)

                if cv2.waitKey(1)==13:
                    break
            video_cap.release()
            cv2.destroyAllWindows()
            






if __name__ ==  "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()