import customtkinter as graphics
from tkinter import *
from PIL import Image, ImageTk

root = graphics.CTk()
root.title("Login Page")
graphics.set_appearance_mode("black")
graphics.set_default_color_theme("green ")
my_button = graphics.CTkButton(root,text="helloworld")
my_button.pack(pady=500)
root.mainloop()