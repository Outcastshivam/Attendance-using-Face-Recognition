from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x700+0+0")
        self.root.title("Face Recognition System")

        #Background
        img = Image.open(r"Images_Project\Background.jpg")
        img = img.resize((1400,700),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image = self.photoimg)
        bg_img.place(x=0,y=0,width=1400,height=700)

        title_label = Label(bg_img,text = "FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman", 35, "bold"),bg="SkyBlue",fg="black")
        title_label.place(x=0,y=0,width=1300,height=45)


        #Student button
        img1 = Image.open(r"Images_Project\Student.jpg")
        img1 = img1.resize((180,180),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1 = Button(bg_img,image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x=30, y=60, width=180, height=180)

        b1_1 = Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",12,"bold"),bg="lightblue",fg="black")
        b1_1.place(x=30,y=240,width=180,height=30)

        #face recognition button
        img2 = Image.open(r"Images_Project\Face_Recognition.jpg")
        img2 = img2.resize((180,180),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b2 = Button(bg_img,image=self.photoimg2,cursor="hand2",command=self.face_data)
        b2.place(x=230, y=60, width=180, height=180)

        b2_2 = Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.face_data,font=("times new roman",12,"bold"),bg="lightblue",fg="black")
        b2_2.place(x=230,y=240,width=180,height=30)


        #attendance button
        img3 = Image.open(r"Images_Project\Attendance.jpg")
        img3 = img3.resize((180,180),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b3 = Button(bg_img,image=self.photoimg3,cursor="hand2",command=self.attendance_data)
        b3.place(x=430, y=60, width=180, height=180)

        b3_3 = Button(bg_img,text="ATTENDANCE",cursor="hand2",command=self.attendance_data,font=("times new roman",12,"bold"),bg="lightblue",fg="black")
        b3_3.place(x=430,y=240,width=180,height=30)


        #help button
        img4 = Image.open(r"Images_Project\Help.jpg")
        img4 = img4.resize((180,180),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b4 = Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.help_desk)
        b4.place(x=630, y=60, width=180, height=180)

        b4_4 = Button(bg_img,text="HELP DESK",cursor="hand2",command=self.help_desk,font=("times new roman",12,"bold"),bg="lightblue",fg="black")
        b4_4.place(x=630,y=240,width=180,height=30)


        #train data button
        img5 = Image.open(r"Images_Project\Train_Data.jpg")
        img5 = img5.resize((180,180),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b5 = Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.train_data)
        b5.place(x=830, y=60, width=180, height=180)

        b5_5 = Button(bg_img,text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("times new roman",12,"bold"),bg="lightblue",fg="black")
        b5_5.place(x=830,y=240,width=180,height=30)

        #photos button
        img6 = Image.open(r"Images_Project\Photos.jpg")
        img6 = img6.resize((180,180),Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b6 = Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.open_img)
        b6.place(x=1030, y=60, width=180, height=180)

        b6_6 = Button(bg_img,text="PHOTOS GALLERY",cursor="hand2",command=self.open_img,font=("times new roman",12,"bold"),bg="lightblue",fg="black")
        b6_6.place(x=1030,y=240,width=180,height=30)


        #About us button
        # img7 = Image.open(r"Images_Project\About_Us.jpg")
        # img7 = img7.resize((120,120),Image.LANCZOS)
        # self.photoimg7 = ImageTk.PhotoImage(img7)

        # b7 = Button(bg_img,image=self.photoimg7,cursor="hand2")
        # b7.place(x=30, y=550, width=100, height=100)

        # b7_7 = Button(bg_img,text="ABOUT US",cursor="hand2",font=("times new roman",12,"bold"),bg="lightblue",fg="black")
        # b7_7.place(x=30,y=650,width=100,height=30)


        #exit button
        img8 = Image.open(r"Images_Project\Exit.jpg")
        img8 = img8.resize((120,120),Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b8 = Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.iExit)
        b8.place(x=1120, y=550, width=100, height=100)

        b8_8 = Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",12,"bold"),bg="lightblue",fg="black")
        b8_8.place(x=1120,y=650,width=100,height=30)



    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to Exit!!",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return


# ==========Function buttons============/

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)



if __name__ ==  "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()     