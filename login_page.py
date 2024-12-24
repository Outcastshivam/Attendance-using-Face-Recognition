import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox
import requests

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1400x700+0+0")
        self.root.title("Face Recognition System")

        #Background
        img = Image.open(r"Images_Project\login.webp")
        img = img.resize((1400,700),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image = self.photoimg)
        bg_img.place(x=0,y=0,width=1400,height=700)

        # Username
        username_label = tk.Label(root, text="Username:", font=("times new roman", 25, "bold"),fg="black")
        username_label.place(x=180, y=160, width=160, height=30)

        self.username_entry = tk.Entry(root, font=("times new roman", 20), justify="center")
        self.username_entry.place(x=160, y=210, width=200, height=30)

        # Password
        password_label = tk.Label(root, text="Password:", font=("times new roman", 25, "bold"),fg="black")
        password_label.place(x=180, y=280, width=160, height=30)

        self.password_entry = tk.Entry(root, show="*", font=("times new roman", 20), justify="center")
        self.password_entry.place(x=160, y=330, width=200, height=30)

        # Login Button
        button1 = tk.Button(root, text="Login", font=("times new roman", 18),cursor='hand2', command=self.login)
        button1.place(x=210, y=420, width=90, height=40)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "" or password == "":
            tkinter.messagebox.showerror("Error", "All fields are required!")
            return

        try:
            response = requests.post("http://localhost/login_system/login.php", data={"username": username, "password": password})
            if response.status_code == 200 and response.json().get("status") == "success":
                self.root.destroy()
                
                import main
                root = tk.Tk()
                app = main.Face_Recognition_System(root)
                root.mainloop()
            else:
                tkinter.messagebox.showerror("Error", "Invalid username or password.")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Unable to connect to the server. {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()
