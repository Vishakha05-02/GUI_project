from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
windows=Tk()


class Login():
    def __init__(self, windows):
        self.windows=windows
        self.windows.title("Login System")
        self.windows.geometry('1017x500+100+50')
        self.windows.resizable(0,0)
        self.load = Image.open("images\w1.jpg")

        # Background frame
        self.bg = ImageTk.PhotoImage(self.load)
        self.bg_image = Label(self.windows,image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)

        #Login frame
        Frame_login = Frame(self.windows, bg="white")
        Frame_login.place(x=150, y=150, height=340, width=400)

        #creating lable inside login_frame
        title = Label(Frame_login,text="Login here", font=("Impact",30, "bold"), fg="#d77337", bg="white").place(x=70, y=30)
        description = Label(Frame_login, text="Employee login area", font=("Goudy old style", 15, "bold"), fg="#d25d17", bg="white").place(x=70,y=100)

        #creating a lable and entry for username
        lbl = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=70,y=140)
        self.text_user = Entry(Frame_login,font=("Arial",15),bg="lightgrey")
        self.text_user.place(x=70, y=170,width=250, height=35)

        #creating a label and entry for password
        lbl = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=70,y=210)
        self.text_pass = Entry(Frame_login, font=("Arial", 15), bg="lightgrey")
        self.text_pass.place(x=70, y=240, width=250, height=35)

        #creating login and forget_passsword button
        forget_btn = Button(Frame_login, text="forget password?", cursor="hand2", fg="#d77337",bd=0, bg="white", font=("Arial",12)).place(x=150, y=280)
        login_btn = Button(Frame_login, command=self.login_function, cursor="hand2", text="Login", bg="#d77337", fg="white", font=("Arial", 12)).place(x=70, y=280)

    def login_function(self):
        if self.text_pass.get()=="" or self.text_user.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.windows)
        elif self.text_pass.get()!="12345" or self.text_user.get()!="Vishakha":
            messagebox.showerror("Error","Invalid Username/Password", parent=self.windows)
        else:
            messagebox.showinfo("Welcome",f"Welcome {self.text_user.get()}\nYour Password: {self.text_pass.get()}", parent=self.windows)

obj=Login(windows)
windows.mainloop()
