from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x700+0+0")
        self.root.title("Face Recognition System")

        #back-ground
        img = Image.open(r"Images_Project\Background.jpg")
        img = img.resize((1400,700),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image = self.photoimg)
        bg_img.place(x=0,y=0,width=1400,height=700)

        title_label = Label(self.root,text = "TRAIN DATA SET",font=("times new roman", 35, "bold"),bg="SkyBlue",fg="red")
        title_label.place(x=0,y=0,width=1300,height=45)

        top_img = Image.open(r"Images_Project\Train_Data.jpg")
        top_img = top_img.resize((280,180),Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(top_img)

        top_label = Label(self.root,image = self.photoimg_top)
        top_label.place(x=500,y=55,width=280,height=180)

        #Button
        btn = Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman", 25, "bold"),bg="red",fg="white")
        btn.place(x=510, y=240, width=260, height=45)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #Gray scale image
            imageNp=np.array(img,"uint8")
            id=int(os.path.split(image)[1].split(".")[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #====================Train the classifier===================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")


if __name__ ==  "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop() 