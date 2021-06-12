"""******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************"""
from tkinter import *  # used for developing GUI in python
import time

root = Tk(className="digital clock")  # initializing main window
root.geometry('800x500')  # Setting width an height of root-main window
root.configure(bg="#86D3FF")
root.resizable(0, 0)  # prohibits resizing of main window

Label(root, text="Digital Clock", fg="White", bg="#FF495F", font="Courier 50 bold").pack(fill="both")


time_lbl = Label(root, font="Courier 60 bold", fg="White", bg="Black")
time_lbl.place(x=150,y=150)

def display():
    time_display = time.strftime("%r")
    time_lbl.configure(text=time_display)
    time_lbl.after(200, display)
    current_time= int (time.strftime("%H"))
    if current_time <12:
        Label(root, text="Good Morning!", fg="#0040FF",
              bg="#86D3FF", font="Courier 50 bold").place(x=150,y=250)
    elif 12 <= current_time < 18:
        Label(root, text="Good Afternoon!", fg="#0040FF",
              bg="#86D3FF", font="Courier 50 bold").place(x=150,y=250)
    else:
        Label(root, text="Good Evening!", fg="#0040FF",
              bg="#86D3FF", font="Courier 50 bold").place(x=150,y=250)

display()




root.mainloop()  # keep the main window open until we manually close it


