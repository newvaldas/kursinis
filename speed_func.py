from english_words import english_words_set
from tkinter import Tk, Label, Button, Entry, END, GROOVE
import tkinter.font as font
import random
import logging


score = 0
time = 0
count_words = 0
words = list(english_words_set)

logging.basicConfig(filename='speed_typing.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def new_game() -> None:
    win = Tk()  
    win.geometry("700x500")
    win.title("Have fun!")
    win.config(bg="#007ACC")
   
    def game_time() -> None: # game time function update time every second.
        global time
        time += 1
        clock.configure(text=time)
        clock.after(1000, game_time)
        
    def restart_game() -> None: #restart button function
        global time, score, count_words
        score = 0
        time = 0
        count_words = 0
        win.destroy()    
        new_game()
          
    def start_game(event) -> None: #start typing test window 
        logging.info(f"User input word: {user_input.get()} ")
        global score, count_words
        if time == 0:
            random.shuffle(words)
            next_word.configure(text=words[0]) 
            user_input.delete(0, END)
            game_time()
            
        #If the enter button is pressed and it is not the start of the game
        if user_input.get() == next_word["text"]: #checking if entered word is correct
            score += 1
            score_board.configure(text=score)
            
        count_words +=1 # counting words
        if (count_words <10):
            random.shuffle(words)
            next_word.configure(text=words[0]) #first element in "next_word" label
            user_input.delete(0, END)
            
        else: # add widgets and show results
            result = Label(win, text="Test results:", font=("Arial", 24, "bold"), fg="dark blue", bg="#007ACC") 
            result.place(x=230, y=150)
            result.configure(text="Time taken = {} \n Your score = {} \n Missed words = {}"
                            .format(time, score, count_words-score))
            
            exit_btn = Button(win, text="Exit", bg="azure", fg="green", width=15, height=2, command=win.destroy)
            exit_btn['font'] = font.Font(size=28)
            exit_btn.place(x=330, y=350)
            
            restart_btn = Button(win, text="Restart", bg="azure", fg="red", width=15, height=2, command=restart_game)
            restart_btn['font'] = font.Font(size=28)
            restart_btn.place(x=130, y=350)
        
            next_word.destroy()
            user_input.destroy()
            score_label.destroy()
            score_board.destroy()
            clock_label.destroy()
            clock.destroy() 
    
    label=Label(win, bg="dark blue", text="Show your typing skills!", font=("azure", 25, "bold",), fg="white", width=40)
    label.place(x=10, y=10)

    next_word=Label(win, text="Press enter button to start and after you type the word!",
                    font=("azure", 20, "bold"), fg="white", justify="center", bg="#007ACC")
    next_word.place(x=100, y=240)

    score_label=Label(win, text="Your score: ", font=("azure", 28, "italic bold"), fg="red", bg="#007ACC")
    score_label.place(x=20, y=100)

    score_board=Label(win, text=score, font=("azure",  28, "italic bold"), fg="blue", bg="#007ACC")
    score_board.place(x=100, y=180)

    clock_label=Label(win,text="Time Passed:", font=("azure", 28, "italic bold"), fg="red", bg="#007ACC")
    clock_label.place(x=500, y=100)

    clock=Label(win, text=time, font=("azure", 28, "italic bold"), fg="blue", bg="#007ACC")
    clock.place(x=560, y=180)

    user_input=Entry(win, font=("azure", 25, "italic bold"), border=10, justify="center", relief=GROOVE)
    user_input.place(x=150, y=330)
    user_input.focus_set()
    
    win.bind("<Return>", start_game)
    win.mainloop()