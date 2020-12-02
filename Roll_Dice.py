import random
from tkinter import *

dice=Tk()
dice.title("Rolling_Dice")
dice.geometry("700x300")


l1=Label(dice,text="",font=("times",150),foreground='green')

def roll():
	number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
	l1.config(text=f'{random.choice(number)}{random.choice(number)}{random.choice(number)}')
	l1.pack()
b1=Button(dice,text="Roll",foreground='red',background='black', command=roll)
b1.place(anchor=CENTER)
b1.pack()

dice.mainloop()

