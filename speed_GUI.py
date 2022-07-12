from english_words import english_words_set
from tkinter import *
import tkinter.font as font
import random
from PIL import ImageTk, Image
import logging
from speed_func import new_game


win = Tk()  # pagrindinis langas su start ir exit mygtukais
win.geometry("700x500")
win.title("Speed Typing Test")
new_image = Image.open("./pictures/picture1.jpg")
new_bg = ImageTk.PhotoImage(new_image)

lbl = Label(win,image=new_bg)
lbl.place(x=-230, y=-150)

frame1 = Frame(win,bg="#F5ECE1", relief=RAISED)
frame1.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.15)# laukelio dydis

label1 = Label(frame1, text="Welcome to \n Speed Typing Test!", font=("Arial", 24, "bold"), relief=RAISED)
label1.place(relx=0,rely=0, relwidth=1, relheight=1)

# username=Entry(win, font=("azure", 25, "italic bold"), border=10, justify="center", relief=GROOVE)
# username.place(x=160, y=180)

start_btn = Button(win, text="Start test", bg="azure", fg="black", width=15, height=2, command=new_game)
start_btn['font'] = font.Font(size=20, weight="bold", underline=True)
start_btn.place(x=230, y=260)

exit_btn = Button(win, text="Exit", bg="azure", fg="green", width=15, height=2, command=win.destroy)
exit_btn['font'] = font.Font(size=20, weight="bold", underline=True)
exit_btn.place(x=230, y=360)

win.mainloop()



          


