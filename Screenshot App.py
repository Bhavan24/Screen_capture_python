import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import PIL.ImageGrab as img
from tkinter.filedialog import asksaveasfile 

root = Tk()
root.title("Screen Capture")
root.geometry("266x100")
root.resizable(width=False, height=False)

def screenshot():
	files = [('Jpg Files', '*.jpg')] 
	file = asksaveasfile(filetypes = files, defaultextension = files)
	ss = img.grab()
	ss.save(file, 'JPEG')
	ss.show()

ssBtn = tk.Button(root)
ssBtn["bg"] = "#efefef"
ft = tkFont.Font(family='Arial',size=10)
ssBtn["font"] = ft
ssBtn["fg"] = "#000000"
ssBtn["justify"] = "center"
ssBtn["text"] = "Take Screenshot"
ssBtn["relief"] = "groove"
ssBtn.place(x=30,y=30,width=200,height=41)
ssBtn["command"] = screenshot

root.mainloop()
