import tkinter as tk
from PIL import Image, ImageTk

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def main():
    root = tk.Tk()
    root.title("Fullscreen Image")
    root.attributes('-fullscreen', True)

    # Load image
    image = Image.open("known_face.jpg")
    photo = ImageTk.PhotoImage(image)

    # Create a label with the image
    label = tk.Label(root, image=photo)
    label.image = photo
    label.grid(row=0, column=0, sticky="nsew")

    # Configure the grid to fill the window
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    center_window(root)
    root.mainloop()

if __name__ == "__main__":
    main()