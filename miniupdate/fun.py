from tkinter import *
app = Tk()
app.geometry("500x500")
def page2():
    app2 = Tk()
    app2.geometry("500x500")

Button(app, text="button", command=page2).pack()

app.mainloop()