from tkinter import *
from PIL import Image, ImageTk
import validators
from pyshorteners import Shortener
import clipboard

def Clear():
    e.delete(0, "end")
    l.config(text="")

def Copy():
    clipboard.copy(l.cget("text"))
    c = Label(win, text="Copied", font=(20))
    c.pack()
    win.after(2000, c.destroy)

def Paste():
    e.delete(0, "end")
    e.insert(0, clipboard.paste())

def Shorten():
    link = e.get()
    valid = validators.url(link)
    if valid:
        short = Shortener().tinyurl.short(link)
        l.config(text=short)
    else:
        l.config(text="Invalid Address")

win = Tk()
win.title("Url Shortener")
win.geometry("700x200")

e = Entry(win, font=(20))
e.place(relwidth=.6, relx=.2, rely=.2)

paste = Image.open("paste.png")
resized_paste = paste.resize((20, 20), Image.LANCZOS)
new_paste = ImageTk.PhotoImage(resized_paste)

paste_b = Button(win, image=new_paste, command=Paste)
paste_b.place(relx=.16, rely=.2)

shorten_b = Button(win, text="Shorten", command=Shorten)
shorten_b.place(relx=.4, rely=.35)

clear_b = Button(win, text="Clear", command=Clear)
clear_b.place(relx=.5, rely=.35)

l = Label(win, bg="White", font=(20), relief="sunken")
l.place(relwidth=.6, relx=.2, rely=.55)

copy = Image.open("copy.png")
resized_copy = copy.resize((20, 20), Image.LANCZOS)
new_copy = ImageTk.PhotoImage(resized_copy)

copy_b = Button(win, image=new_copy, command=Copy)
copy_b.place(relx=.16, rely=.55)

win.mainloop()
