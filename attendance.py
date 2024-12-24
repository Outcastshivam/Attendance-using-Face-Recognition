from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata = []

class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x700+0+0")
        self.root.title("Face Recognition System")

        # ================= variables ==============
        self.var_attend_id=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dept=StringVar()
        self.var_attend_year=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()

        title_label = Label(root,text = "ATTENDANCE RECORD",font=("times new roman", 35, "bold"),bg="SkyBlue",fg="brown")
        title_label.place(x=0,y=0,width=1300,height=45)

        main_frame=Frame(root,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1250,height=620)

        #left side label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Detail",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=5,width=500,height=600)

        left_img = Image.open(r"Images_Project\AttendanceHome.jpeg")
        left_img = left_img.resize((492,150),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(left_img)

        left_label = Label(Left_frame,image = self.photoimg_left)
        left_label.place(x=2,y=1,width=492,height=150)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=3,y=155,width=490,height=420)

        #labels and entry

        #attendance id
        attendanceID_label=Label(left_inside_frame,text="Std ID:",font=("times new roman",12,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_attend_id,font=("times new roman",11))
        attendanceID_entry.grid(row=0,column=1,sticky=W)

        #name
        name_label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_name,width=18,font=("times new roman",11))
        name_entry.grid(row=0,column=3,sticky=W)

        #department
        department_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        department_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        department_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_dept,width=20,font=("times new roman",11))
        department_entry.grid(row=1,column=1,sticky=W)

        
        #year
        year_label=Label(left_inside_frame,text="Year:",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        year_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_year,width=20,font=("times new roman",11))
        year_entry.grid(row=1,column=3,sticky=W)

        #time
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_time,width=18,font=("times new roman",11))
        time_entry.grid(row=2,column=1,sticky=W)

        #date
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_date,width=20,font=("times new roman",11))
        date_entry.grid(row=2,column=3,sticky=W)

        #attendance_status
        attendance_status_label=Label(left_inside_frame,text="Attd Status:",font=("times new roman",12,"bold"),bg="white")
        attendance_status_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        attendance_status_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_attend_attendance,font=("times new roman",12),state="readonly",width=13)
        attendance_status_combo["values"]=("Present","Absent")
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=3,column=1,padx=2,pady=5,sticky=W)


         #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=3,y=262,width=475,height=35)

        save_btn=Button(btn_frame,text="Import CSV",command=self.importCSV,width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=12,font=("times new roman",12,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=12,font=("times new roman",12,"bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=12,font=("times new roman",12,"bold"),bg="orange",fg="white")
        reset_btn.grid(row=0,column=3)



        #right side label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=520,y=5,width=720,height=600)

        right_img = Image.open(r"Images_Project\Student_details_right.jpg")
        right_img = right_img.resize((710,150),Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(right_img)

        right_label = Label(Right_frame,image = self.photoimg_right)
        right_label.place(x=2,y=1,width=710,height=150)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=3,y=155,width=708,height=420)

        #======================scroll bar of table================================
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","name","department","year","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Student ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("year",text="Year")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=80)
        self.AttendanceReportTable.column("department",width=80)
        self.AttendanceReportTable.column("year",width=80)
        self.AttendanceReportTable.column("time",width=80)
        self.AttendanceReportTable.column("date",width=80)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    # ========================== fetch data ===================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv
    def importCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    
    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data is Exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_name.set(rows[1])
        self.var_attend_dept.set(rows[2])
        self.var_attend_year.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_name.set("")
        self.var_attend_dept.set("")
        self.var_attend_year.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")



if __name__ ==  "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()