from customtkinter import * 
import threading
import facemain
import database
import os 
import time
import alertsys
global counter
def gui():
    def filesave():
        a=entryt21.get()
        b=entryt22.get()
        c=entryt23.get()
        d=entryt24.get()
        e=entryt25.get()
        entryt21.delete(0,END)
        entryt22.delete(0,END)
        entryt23.delete(0,END)
        entryt24.delete(0,END)
        entryt25.delete(0,END)
        if database.checker(b)==True:
            label5.configure(text="user exist and cannot be registered")
            print("not pushed")
        elif  ".com" not in c or  "@" not in c:
            label5.configure(text="mpmail not in format registered")
            print("not pushed")
        elif os.path.exists(d)==False or d.endswith(".jpg")==False:
            label5.configure(text="path doesnot exist")
            print("not pushed")
        elif database.checker(b)!=True:
            database.pusher(a,b,c,d,e)
            label5.configure(text="register is done") 
    def locker():
        username=entryt11.get()
        if database.checker(username)==True:
            entryt12.configure(state="normal",placeholder_text="enter the password")
            btn.configure(state="normal")
            label3.configure(text="userfound")
            facemain.facer=False
            time.sleep(2)
            facemain.facer=True
            path=database.imagepath(username)
            x2=threading.Thread(target=facemain.facerecon,args=(path,))
            x2.start()
        else:
            entryt11.delete(0,END)
            entryt12.delete(0,END)
            entryt12.configure(state="disable",placeholder_text="")
            btn.configure(state="disable",text_color_disabled="yellow")
            label3.configure(text="usernotfound")
            facemain.facer=False


    def loginchecker():
        x=entryt12.get()
        entryt12.delete(0,END)
        print(x)
        username=entryt11.get()
        password=database.password(username)
        if password==x and facemain.failornot==True and bool(password)==True:
           label2.configure(text="Login was an Success")
           topview=CTkToplevel(tab1,fg_color="white")
           label4=CTkLabel(topview,text="Here is the safe data")
           label4.place(relx=0.5,rely=0.5)
        else: 
            label2.configure(text= "Suspicion detected")
            mail=database.usermail(username)
            alertsys.alert(mail)
            print("failure ocuured")
    app = CTk()
    set_appearance_mode("light")
    app.geometry("1920x1080")
    mytab=CTkTabview(master=app,height=700,width=700,)
    mytab.pack(padx=20, pady=20)
    tab1=mytab.add("      Login       ")
    tab2=mytab.add("      Signup    ")
    #tab1 elements
    label2=CTkLabel(tab1,text="",anchor="center")
    label2.pack(pady=20)
    entryt11= CTkEntry(tab1, corner_radius=32, placeholder_text="enter your username",width=175)
    entryt11.pack(pady=20)
    btn2= CTkButton(tab1, text="Check",fg_color="#098080",corner_radius=32, hover_color="#C850C0",command=locker)
    btn2.pack(pady=20)
    label3=CTkLabel(tab1,text="",anchor="center")
    label3.pack(pady=20)
    entryt12= CTkEntry(tab1, corner_radius=32,show="*", placeholder_text="enter your password",width=175,state="disabled")
    entryt12.pack(pady=20)
    btn = CTkButton(tab1, text="Login",fg_color="#098080",corner_radius=32, hover_color="#C850C0",command=loginchecker,state="disabled",text_color_disabled="yellow")
    btn.pack(pady=20)
    label=CTkLabel(tab1,text="Login",anchor="center")
    label.pack(pady=20)
    #tab2 elements
    entryt21= CTkEntry(tab2, corner_radius=32, placeholder_text="enter your name ",width=200)
    entryt21.pack(pady=20)
    entryt22= CTkEntry(tab2, corner_radius=32, placeholder_text="enter your username",width=200)
    entryt22.pack(pady=20)
    entryt25= CTkEntry(tab2, corner_radius=32, placeholder_text="enter your password",width=200)
    entryt25.pack(pady=20)
    entryt23= CTkEntry(tab2, corner_radius=32, placeholder_text="enter your email",width=200)
    entryt23.pack(pady=20)
    entryt24= CTkEntry(tab2,corner_radius=32, placeholder_text="path of your image for authentication",width=200)
    entryt24.pack(pady=20)
    btnt2 = CTkButton(tab2, text="register",fg_color="#C850C0",corner_radius=32, hover_color="#ffffff",command=filesave)
    btnt2.pack(pady=20)
    label5=CTkLabel(tab2,text="Welcome to Register in facey",anchor="center")
    label5.pack(pady=20)
    label6=CTkLabel(tab2,text="enter your details",anchor="center")
    label6.place(relx=0.5,rely=0.8,anchor="center")
    app.mainloop()
x1=threading.Thread(target=gui)

x1.start()

