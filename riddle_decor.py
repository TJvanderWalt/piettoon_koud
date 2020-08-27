from riddle import func_add
from tkinter import *

def decorator(func):
    print("Hello")
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def my_func():
    base_number=int(e_base.get())
    code_1 = list(e_code1.get())
    code_2 = list(e_code2.get())
    code_3 = list(e_code3.get())
    code_sum = list(e_target.get())
    list_of_codes = [code_1, code_2, code_3, code_sum]
    boelie = decorator(func_add)(base_number, list_of_codes)
    print(boelie)


window = Tk()
window.geometry("750x400+40+50")

label_base = Label(
    window,
    text="base number",
    font="times 12 bold",
    foreground="white", # Set the text color
    bg="red",    # "orange" "yellow" "green" "blue" "purple" "black" or hexadecimal RGB values
    width=10,
    height=2
)
label_base.place(x=25, y=150)

e_base = Entry(fg="yellow", bg="blue", width=10) #allows only single line of text to be entered
e_base.place(x=25, y=200)
#the user can now input text, or it can be programmatically inserted
e_base.insert(0, "10") #text is inserted at position 0

label_code1 = Label(
    window,
    text="code1",
    font="times 12 bold",
    foreground="white", # Set the text color
    bg="red",    # "orange" "yellow" "green" "blue" "purple" "black" or hexadecimal RGB values
    width=10,
    height=2
)
label_code1.place(x=150, y=150)

e_code1 = Entry(fg="yellow", bg="blue", width=10) 
e_code1.place(x=150, y=200)
e_code1.insert(0, "1") 

label_code2 = Label(
    window,
    text="code2",
    font="times 12 bold",
    foreground="white", # Set the text color
    bg="red",    # "orange" "yellow" "green" "blue" "purple" "black" or hexadecimal RGB values
    width=10,
    height=2
)
label_code2.place(x=275, y=150)

e_code2 = Entry(fg="yellow", bg="blue", width=10) 
e_code2.place(x=275, y=200)
e_code2.insert(0, "11") 

label_code3 = Label(
    window,
    text="code3",
    font="times 12 bold",
    foreground="white", # Set the text color
    bg="red",    # "orange" "yellow" "green" "blue" "purple" "black" or hexadecimal RGB values
    width=10,
    height=2
)
label_code3.place(x=400, y=150)

e_code3 = Entry(fg="yellow", bg="blue", width=10) 
e_code3.place(x=400, y=200)
e_code3.insert(0, "13") 

label_target = Label(
    window,
    text="code target",
    font="times 12 bold",
    foreground="white", # Set the text color
    bg="red",    # "orange" "yellow" "green" "blue" "purple" "black" or hexadecimal RGB values
    width=10,
    height=2
)
label_target.place(x=525, y=150)

e_target = Entry(fg="yellow", bg="blue", width=10) 
e_target.place(x=525, y=200)
e_target.insert(0, "30") 


label6 = Label(
    window,
    text="1  3  5  7  9  11  13  15",
    font="times 12 bold",
    foreground="white", # Set the text color
    bg="red",    # "orange" "yellow" "green" "blue" "purple" "black" or hexadecimal RGB values
    width=30,
    height=2
)
label6.place(x=25, y=75)

b1 = Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=my_func
)
b1.place(x=525, y=250)

window.mainloop()