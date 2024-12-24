from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x700+0+0")
        self.root.title("Face Recognition System")

        #Background
        img = Image.open(r"C:\Users\shiva\OneDrive\Desktop\Face-Recognition-Attendance\Images_Project\Help.jpg")
        img = img.resize((400,400),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image = self.photoimg)
        bg_img.place(x=0,y=0,width=1300,height=700)

        title_label = Label(bg_img,text = "HELP DESK",font=("times new roman", 35, "bold"),bg="SkyBlue",fg="black")
        title_label.place(x=0,y=0,width=1300,height=45)

        email_label=Label(bg_img,text="E-mail : shivamkr9303695@gmail.com ",font=("times new roman",13,"bold"),fg="black",bg="white")
        email_label.place(x=500,y=560)

        mobile_label=Label(bg_img,text="Mobile No. : 9308184631 ",font=("times new roman",13,"bold"),fg="black",bg="white")
        mobile_label.place(x=540,y=590)




if __name__ ==  "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop() 