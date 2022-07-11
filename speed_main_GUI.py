
from english_words import english_words_set
from tkinter import *
import tkinter.font as font
import random
from PIL import ImageTk, Image
import logging

score = 0
missed_word = 0
time = 0
count_words = 0
words = list(english_words_set)

logging.basicConfig(filename='typing_test.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def new_game() -> None:
    win = Tk()  
    win.geometry("700x500")
    win.title("Let's start the test!")
    win.config(bg="dark blue")
    

    def game_time() -> None:
        global time, score, missed_word, count_words
    
        if(count_words <= 10): # jei count_words maziau uz 10 atnaujina laika
            time += 1
            clock.configure(text=time)
            clock.after(1000, game_time)
        
        else:
            result = Label(win, text="Test results:", font=("Arial", 24, "bold"), fg="dark blue")
            result.place(x=230, y=150)
            result.configure(text="Time taken = {} \n Your score = {} \n Missed words = {}"
                            .format(time, score, count_words-score))
            
            # exit_btn = Button(win, text="Exit", bg="azure", fg="green", width=15, height=2, command=win.destroy)
            # exit_btn['font'] = font.Font(size=20)
            # exit_btn.place(x=330, y=350)
            
            # restart_btn = Button(win, text="Restart", bg="azure", fg="red", width=15, height=2, command=new_game)
            # restart_btn['font'] = font.Font(size=20)
            # restart_btn.place(x=130, y=350)
        

            score = 0
            missed_word = 0
            time = 0
            count_words = 0

            next_word.destroy()
            user_input.destroy()
            score_label.destroy()
            score_board.destroy()
            clock_label.destroy()
            clock.destroy()    


    
    def start_game(event):
        logging.info(f"User input word: {user_input.get()} ") # loginimas
        global score, missed_word, count_words
        if time == 0:
            random.shuffle(words)
            next_word.configure(text=words[0]) #pirmas words listo elementas "next_word" lable
            user_input.delete(0, END)
            game_time()
        
        if user_input.get() == next_word["text"]: #tikrina zodis ar ivestas teisingas
            score += 1
            score_board.configure(text=score)
            
        count_words +=1 # bendra zodziu ivedimas
        if (count_words <= 10):
            random.shuffle(words)
            next_word.configure(text=words[0]) #pirmas words listo elementas "next_word" lable
            user_input.delete(0, END)
    
  

    label=Label(win, bg="dark blue", text="Test your typing skills!", font=("azure", 25, "bold",), fg="white", width=40)
    label.place(x=10, y=10)

    next_word=Label(win, text="Welcome! \n Press enter button to start and after you type the word.",
                    font=("azure", 20, "bold"), fg="black", justify="center")
    next_word.place(x=60, y=240)

    score_label=Label(win, text="Your score: ", font=("azure", 25, "italic bold"), fg="red")
    score_label.place(x=10, y=100)

    score_board=Label(win, text=score, font=("azure",  25, "italic bold"), fg="blue")
    score_board.place(x=100, y=180)

    clock_label=Label(win,text="Time Passed:", font=("azure", 25, "italic bold"), fg="red")
    clock_label.place(x=500, y=100)

    clock=Label(win, text=time, font=("azure", 25, "italic bold"), fg="blue")
    clock.place(x=560, y=180)

    user_input=Entry(win, font=("azure", 25, "italic bold"), border=10, justify="center", relief=GROOVE)
    user_input.place(x=150, y=330)
    user_input.focus_set()
    
    
    
    win.bind("<Return>", start_game)
    win.mainloop()

 
    
win = Tk()  # pagarindinis langas su start ir exit mygtukais
win.geometry("700x500")
win.title("Speed Typing Test")
new_image = Image.open("/Users/valkri/Documents/kursinis/kursinis/pictures/picture1.jpg") # background
new_bg = ImageTk.PhotoImage(new_image)

lbl = Label(win,image=new_bg)
lbl.place(x=-230, y=-150)

frame1 = Frame(win,bg="#F5ECE1", relief=RAISED)
frame1.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.15)# laukelio dydis

label1 = Label(frame1, text="Welcome to \n Speed Typing Test!", font=("Arial", 24, "bold"))
label1.place(relx=0,rely=0, relwidth=1, relheight=1)

start_btn = Button(win, text="Start test", bg="azure", fg="black", width=15, height=2, command=new_game)
start_btn['font'] = font.Font(size=20)
start_btn.place(x=230, y=240)

exit_btn = Button(win, text="Exit", bg="azure", fg="green", width=15, height=2, command=win.destroy)
exit_btn['font'] = font.Font(size=20)
exit_btn.place(x=230, y=340)


win.mainloop()



          


