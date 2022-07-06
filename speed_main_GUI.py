
from english_words import english_words_set
from tkinter import *
import tkinter.font as font
import random
from PIL import ImageTk, Image

score = 0
missed_word = 0
time = 0
count_words = 0
words = list(english_words_set)


win = Tk()
win.geometry("700x500")
win.title("Speed Typing Test")
new_image = Image.open("/Users/valkri/Documents/kursinis/kursinis/pictures/picture1.jpg") # background
new_bg = ImageTk.PhotoImage(new_image)

lbl = Label(win,image=new_bg)
lbl.place(x=-230, y=-150)

frame1 = Frame(win,bg="#F5ECE1", relief=RAISED)
frame1.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.15)# laukelio dydis

label1 = Label(frame1, text="Welcome to \n Speed Typing Test!", bg="#F5ECE1", font=("Arial", 24, "bold"))
label1.place(relx=0,rely=0, relwidth=1, relheight=1)

start_btn = Button(win, text="Start test", bg="azure", fg="black", width=15, height=2, command=start_game())
start_btn['font'] = font.Font(size=14)
start_btn.place(x=140, y=240)

exit_btn = Button(win, text="Exit", bg="azure", fg="green", width=15, height=2,)
exit_btn['font'] = font.Font(size=14)
exit_btn.place(x=390, y=240)

win.mainloop()

# pridedame global variables

# score = 0
# missed_word = 0
# time = 0
# count_words = 0
# words = list(english_words_set)

#testo laiko funkcija

def game_time() -> int:
    global time, score, missed_word, count_words
    
    if (count_words <= 10): # jei count_words maziau uz 10 atnaujina laika
        time += 1
        clock.configure(text=time)
        clock.after(1000, game_time)
        
    else:
        
        result = Label(win, text="", font=("Arial", 24, "bold"), fg="#F5D254")
        result.place(x=230, y=250)
        result.configure(text="Time taken = {} \n Your score = {} \n Missed = {}"
                         .format(time, score, count_words-score-1))
        

score = 0
missed_word = 0
time = 0
count_words = 0

# next_word.destroy()
# user_input.destroy()
# score_label.destroy()
# score_board.destroy()
# clock_label.destory()
# clock.destroy()       
        
# fukcija control game

def start_game(event):
    global score, missed_word, count_words
    if time == 0:
        random.shuffle(words)
        next_word.configure(text=words[0]) #pirmas words listo elementas "next_word" lable
        user_input.delete(0, END)
        game_time()
        
    if  user_input.get()== next_word["text"]: #tikrina zodis ar ivestas teisingas
        score += 1
        score_board.configure(text=score)
        count_words +=1
    if(count_words <= 10):
        random.shuffle(words)
        next_word.configure(text=words[0]) #pirmas words listo elementas "next_word" lable
        user_input.delete(0, END)
        
# valdikliu pridejimas i window

label=Label(win, text="Test your typing skills!", font=("azure", 25, "bold",), fg="gray", width=40)
label.place(x=10, y=10)

next_word=Label(win, text="Welcome! Press enter button start and after you type the word",
                font=("azure", 20, "bold"), fg="black")
next_word.place(x=30, y=240)

score_label=Label(win, text="Your score: ", font=("azure", 25, "italic bold"), fg="red")
score_label.place(x=10, y=100)

score_board=Label(win, text=score, font=("azure",  25, "italic bold"), fg="blue")
score_board.place(x=100, y=180)

clock_label=Label(win,text="Time Passed:", font=("azure", 25, "italic bold"), fg="red")
clock_label.place(x=500, y=100)

clock=Label(win, text=time, font=("azure", 25, "italic bold"), fg="blue")
clock.place(x=560, y=180)

user_input=Entry(win, font=("azure", 25, "italic bold"), border=10, justify="center")
user_input.place(x=150, y=330)
user_input.focus_set()   

next_word.destroy()
user_input.destroy()
score_label.destroy()
score_board.destroy()
clock_label.destroy()
clock.destroy()    

win.bind("<Return>", start_game)
win.mainloop()
        
          


