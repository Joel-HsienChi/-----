from tkinter import *

root = Tk()
root.title("title")
root.geometry("500x150")

def window1():
    # adding .grid(row=a, column=b) after button can mod the position of button
    a = Button(text="Click This", command=window2)
    # a.pack() will automatically align the button
    a.pack()
    root.mainloop()

def window2():
    root.destroy()
    window2_main = Tk()
    window2_main.title("title")
    window2_main.geometry("500x150")
    Label(window2_main, text="Bye Bye").pack()
    window2_main.mainloop()

window1()
