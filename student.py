from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x700+0+0")
        self.root.title("Face Recognition System")


        #==============variables===============
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_sec=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()

        #Background
        img = Image.open(r"C:\Users\shiva\OneDrive\Desktop\Face-Recognition-Attendance\Images_Project\Background.jpg")
        img = img.resize((1400,700),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image = self.photoimg)
        bg_img.place(x=0,y=0,width=1400,height=700)

        title_label = Label(bg_img,text = "STUDENT MANAGEMENT SYSTEM",font=("times new roman", 35, "bold"),bg="SkyBlue",fg="black")
        title_label.place(x=0,y=0,width=1300,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1250,height=620)

        #left side label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=5,width=500,height=600)

        left_img = Image.open(r"C:\Users\shiva\OneDrive\Desktop\Face-Recognition-Attendance\Images_Project\Student_details_left.jpg")
        left_img = left_img.resize((492,100),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(left_img)

        left_label = Label(Left_frame,image = self.photoimg_left)
        left_label.place(x=2,y=1,width=492,height=100)

        #current course information
        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        Current_course_frame.place(x=5,y=102,width=485,height=100)

        #department
        dept_label=Label(Current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dept_label.grid(row=0,column=0,padx=5,sticky=W)

        dept_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dept,font=("times new roman",12),state="readonly",width=14)
        dept_combo["values"]=("Select Department","Computer","Civil","Mechanical","Electical")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #course
        course_label=Label(Current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=5,sticky=W)

        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("times new roman",12),state="readonly",width=14)
        course_combo["values"]=("Select Course","Computer Science","AI & ML","Cyber Security","BCA","MCA","MBA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        #year
        year_label=Label(Current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=5,sticky=W)

        year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",12),state="readonly",width=9)
        year_combo["values"]=("Select Year","1st","2nd","3rd","4th")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        #semester
        semester_label=Label(Current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=5,sticky=W)

        semester_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_sem,font=("times new roman",12),state="readonly",width=13)
        semester_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)


        #class student information
        Class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        Class_student_frame.place(x=5,y=210,width=485,height=360)

        #student id
        studentID_label=Label(Class_student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentID_entry=ttk.Entry(Class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",11))
        studentID_entry.grid(row=0,column=1,sticky=W)

        #student name
        studentName_label=Label(Class_student_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=5,pady=8,sticky=W)

        studentName_entry=ttk.Entry(Class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",11))
        studentName_entry.grid(row=0,column=3,sticky=W)

        #class section
        class_div_label=Label(Class_student_frame,text="Section:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=5,pady=8,sticky=W)

        class_div_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_sec,font=("times new roman",11),state="readonly",width=12)
        class_div_combo["values"]=("Select Section","S-1","S-2","S-3","S-4","S-5")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,sticky=W)

        #Roll No
        roll_no_label=Label(Class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=5,pady=8,sticky=W)

        roll_no_entry=ttk.Entry(Class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",11))
        roll_no_entry.grid(row=1,column=3,sticky=W)

        #gender
        gender_label=Label(Class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=5,pady=8,sticky=W)

        gender_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_gender,font=("times new roman",11),state="readonly",width=12)
        gender_combo["values"]=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,sticky=W)

        #DOB
        dob_label=Label(Class_student_frame,text="D.O.B.:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=5,pady=8,sticky=W)

        dob_entry=ttk.Entry(Class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",11))
        dob_entry.grid(row=2,column=3,sticky=W)

        #email
        email_label=Label(Class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=5,pady=8,sticky=W)

        email_entry=ttk.Entry(Class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",11))
        email_entry.grid(row=3,column=1,sticky=W)

        #phone No
        pgone_no_label=Label(Class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        pgone_no_label.grid(row=3,column=2,padx=5,pady=8,sticky=W)

        pgone_no_entry=ttk.Entry(Class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",11))
        pgone_no_entry.grid(row=3,column=3,sticky=W)

        #Address
        address_label=Label(Class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=5,pady=8,sticky=W)

        address_entry=ttk.Entry(Class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",11))
        address_entry.grid(row=4,column=1,sticky=W)


        #radio buttons for photo sample
        photo_sample_label=Label(Class_student_frame,text="Sample:",font=("times new roman",12,"bold"),bg="white")
        photo_sample_label.grid(row=5,column=0,padx=5,pady=2,sticky=W)

        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_student_frame,text="Take a photo sample",value="Yes",variable=self.var_radio1)
        radiobtn1.grid(row=5,column=1,padx=2,pady=2)

        radiobtn2=ttk.Radiobutton(Class_student_frame,text="No photo sample",value="No",variable=self.var_radio1)
        radiobtn2.grid(row=6,column=1,padx=2,pady=2)

        #buttons frame
        btn_frame=Frame(Class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=3,y=262,width=475,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=12,font=("times new roman",12,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=12,font=("times new roman",12,"bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",comman=self.reset_data,width=12,font=("times new roman",12,"bold"),bg="orange",fg="white")
        reset_btn.grid(row=0,column=3)

        #sample photo frame
        sample_btn_frame=Frame(Class_student_frame,bd=2,relief=RIDGE,bg="white")
        sample_btn_frame.place(x=3,y=298,width=475,height=35)

        take_photo_btn=Button(sample_btn_frame,command=self.generate_dataset,text="Take Photo Sample",width=25,font=("times new roman",12,"bold"),bg="black",fg="white")
        take_photo_btn.grid(row=1,column=0,padx=1)

        update_photo_btn=Button(sample_btn_frame,text="Update Photo Sample",width=25,font=("times new roman",12,"bold"),bg="silver",fg="white")
        update_photo_btn.grid(row=1,column=2)





        #right side label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=520,y=5,width=720,height=600)

        right_img = Image.open(r"C:\Users\shiva\OneDrive\Desktop\Face-Recognition-Attendance\Images_Project\Student_details_right.jpg")
        right_img = right_img.resize((710,150),Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(right_img)

        right_label = Label(Right_frame,image = self.photoimg_right)
        right_label.place(x=2,y=1,width=710,height=150)


        #======Search System========
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=150,width=705,height=62)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="purple",fg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12),state="readonly",width=10)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=25,font=("times new roman",12))
        search_entry.grid(row=0,column=2,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",11,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=10)

        save_all_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",11,"bold"),bg="green",fg="white")
        save_all_btn.grid(row=0,column=4)

        #======Tabular Data========
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=215,width=705,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dept","course","year","sem","id","name","sec","roll","gender","birth_date","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dept",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("sec",text="Section")
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("birth_date",text="DOB")
        self.student_table.heading("email",text="E-Mail")
        self.student_table.heading("phone",text="PhoneNo")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dept",width=100)
        self.student_table.column("course",width=120)
        self.student_table.column("year",width=50)
        self.student_table.column("sem",width=60)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=130)
        self.student_table.column("sec",width=100)
        self.student_table.column("roll",width=110)
        self.student_table.column("gender",width=100)
        self.student_table.column("birth_date",width=100)
        self.student_table.column("email",width=200)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=200)
        self.student_table.column("photo",width=120)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #================function declaration================

    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@1",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dept.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_sem.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_sec.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_radio1.get()

                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #===================fetch data=========================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@1",database="face_recogniser")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #====================get cursor to update data=============================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dept.set(data[0])
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_sec.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_radio1.set(data[13])


    #=======================update function=====================
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update these Student details?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@1",database="face_recogniser")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Sem=%s,Student_name=%s,Sec=%s,Roll=%s,Gender=%s,DOB=%s,eMail=%s,Phone=%s,Address=%s,photo_sample=%s where Student_id=%s",(
                                                                                                                                                                                            self.var_dept.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                            self.var_sec.get(),
                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                            self.var_std_id.get(),
                                                                                                                                                                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #=============================delete function======================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required!!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this Student details??",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@1",database="face_recogniser")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Students details successfully deleted!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #=========================Reset function========================================
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_sec.set("Select Section"),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_radio1.set("")



    #===================Generate dataset or take photo samples====================
    def generate_dataset(self):
        if self.var_dept.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@1",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=self.var_std_id.get()
                my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Sem=%s,Student_name=%s,Sec=%s,Roll=%s,Gender=%s,DOB=%s,eMail=%s,Phone=%s,Address=%s,photo_sample=%s where Student_id=%s",(
                                                                                                                                                                                            self.var_dept.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                            self.var_sec.get(),
                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                            id
                                                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #====================Load predefined data on face frontals from openCv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if not ret:
                        break
                    if face_cropped(my_frame) is not None:
                        img_id+=1

                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path=f"data/user.{id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



                                        



if __name__ ==  "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop() 