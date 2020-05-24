"""
TITLE: Cambridge International AS and A level computer science
DESCRIPTION: Part 1: Fundamental problem solving and programming skills; applying Python Turtle to
draw flow charts
REFERENCE1: Cambridge International AS and A level computer science, Sylvia Langfield and Dave 
Duddell downloaded from: http://www.gceguide.xyz/gce-e-books
REFERENCE2: The beginner's guide to Python Turtle, realpython.com
REFERENCE3: https://docs.python.org/3/library/turtle.html
DEPENDENCIES: Python 3; Turtle is a pre-installed Python library (thus no need to 
"pip install turtle" but you must still "import turtle")
TODO
    Add further structured English clauses (Philip)
    Also add the equivalent pseudocode (Philip)
    Lastly, develop a way to draw the equivalent flow charts, using turtle (Philip)
"""

import turtle
import time

def rect(pos=(0, 0), hor=300, vert=45):
    """create a rectangle"""
    #t.hideturtle()
    t.goto(pos)
    t.down()
    t.bk(hor/2)
    for i in range(2):
        t.fd(hor)
        t.rt(90)
        t.fd(vert)
        t.rt(90)
    print(t.pos())
    t.onclick(write_text)
        
def write_text(x, y):
    print(x, y)
    t.goto(x,y)
    t.write("hi", True, align="center")   

def flowchrt():
    t.reset()
    rect((-20, 20))

print("Chapter 11: Algoritm design and problem solving")

print("")
print("structured English - consists of command statements used to describe an algoritm")
print("SET A TO 34")
print("INCREMENT B")

print("")
print("pseudocode - using keywords and identifiers to describe an algoritm without \
following the syntax of a perticular language")
print("A \N{leftwards arrow} 34")
print("B \N{leftwards arrow} B + 1")

print("")
print("flowchart - shapes linked together to represent the sequential steps of an algorithm")
print("flowchart drawn by making use of Python turtle")
print("Now ... creating a separate window (called 'screen') to draw in")
#remember the 'keep_screen_open = input()' statement at the bottom of the code
s = turtle.getscreen()
print("turtle ... it is the arrow you see on the screen!")
t = turtle.Turtle() #easier to refer to 't' in code instead of using 'turtle'
print("next ... we put the pen down")
t.down()
print("now ... tell the turtle to move 250 pixels forward (in the direction which the arrow points)")
t.forward(250)
print("now ... 100 pixels backward")
t.backward(100)
print("and ... turn 90 degrees right (clockwise) followed by 50 pixels forward")
t.right(90)
t.forward(50)
print("make a 90 right ...take 150 forward... 90 right...50 forward")
t.right(90)    #or t.rt(90) t.lt()
t.forward(150) #or t.fd(150) t.bk()
t.right(90)    
t.forward(50)
print("pen up ... let's take the turtle home at position (0,0) ... pen down ... and draw a \
line to (x,y) at (-20,20)")
t.up()
t.home()
t.down()
t.goto(-20, 20)
t.up()
print("clear the screen ... goto position (20,20) and draw a rectangle of size 140 x 80")
keep_screen_open = input("press Enter")
flowchrt()
print("Rectangle\\Set A to 34")
print("Rectangle\\Increment B")
keep_screen_open = input()
#time.sleep(3) alternative to keep screen open for a short while to read output