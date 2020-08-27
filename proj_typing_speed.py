'''from: I know python on Youtube''' 
from tkinter import *
from timeit import default_timer as default_timer
import random

window = Tk()
window.geometry("450x200")


def game():
    global window
    window.destroy()
    def check_result():
        if entry.get() == words[word]:
            end = default_timer()
            print(end - start)
        else:
            print("wrong spelling")
    words = ["programming", "addresses", "passwords"]
    word = random.randint(0, len(words)-1) #alternatively use random.choice(words)
    start = default_timer()
    window = Tk()
    window.geometry("450x200")
    x2=Label(window, text=words[word], font="times 20")
    x2.place(x=150,y=10)
    x3=Label(window, text="lets see how fast you can type", font="times 20")
    x3.place(x=10,y=50)
    entry=Entry(window)
    entry.place(x=280,y=55)
    b2=Button(window, text="submit", command = check_result, width=12, bg="gray")
    b2.place(x=150,y=100)
    b3=Button(window, text="wanna try again", command = game, width=12, bg="gray")
    b3.place(x=250,y=100)
    window.mainloop()



x1 = Label(
    window,
    text="lets start this game ...",
    font="times 20"
)
x1.place(x=10,y=50)

b1 = Button(
    window, 
    text="go", 
    command=game, 
    width=12, 
    bg="gray"
)
b1.place(x=150,y=100)




window.mainloop()