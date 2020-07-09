import random
from tkinter import *

def Generate_random():
    return random.randint(1,20)

def check(guess,output_string):
    if not guess.isnumeric():
        output_string.set("Guess is not numeric")
        return
    guess=int(guess)
    if guess==answer:
        output_string.set("Congratulations!! Correct Guess")
    elif guess<answer:
        output_string.set("Your guess is LOW!!")
    else:
        output_string.set("Your guess is HIGH!!")

def GUI():
    window=Tk()
    window.title('Guess Game')
    window.minsize(300,200)
    input_string=StringVar()
    inp=StringVar()
    out=StringVar()
    input_string.set('Guess a number between 1 and 20 ')
    Label(window,text=" ").grid(row=1)
    Label(window,text="                ").grid(row=2,column=3)
    Label(window,textvariable=input_string,justify=CENTER).grid(row=2,column=5)
    Label(window,text=" ").grid(row=3,column=3)
    Entry(window,textvariable=inp).grid(row=4,column=5)
    Label(window,textvariable=out,justify=CENTER).grid(row=5,column=5)
    Button(window,text="Check",command=lambda : check(inp.get(),out),justify=LEFT).grid(row=6,column=5)
    Button(window,text="Close",command=window.destroy,justify=RIGHT).grid(row=8,column=5)
    window.mainloop()
        
answer=Generate_random()
GUI()


