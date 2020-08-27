"""title: GUIs in Python with Tkinter
topics: 
    window and sizing; 
    Label; 
    Button (clickable);
    Entry;
    Text;
    Frame;
    checkboxes, radio buttons, scroll bars, progress bars 
    events;
    positioning (geometry managers)
reference1: 
    "Python GUI programming with Tkinter" (realpython.com)
reference2:
    TkDocs https://tkdocs.com/tutorial/index.html 
reference3: 
    "" (realpython.com)
so what? 
    Python has a lot of GUI frameworks, but Tkinter is the only framework that's built into the Python
    standard library; Tkinter is cross-platform (works on Windows, macOS, Linux); Tkinter does not look 
    "modern and shiny" but it is lightwieght and relatively painless to use compared to other frameworks.
    Other frameworks include: wxPython, PyQT, PySimple GUI, easyGUI (does not allow for events) and the
    Kivy Python Framework for building mobile applications
further reading/links: 
    (piettoon_koud > master) > GUI_kivy.py
github: 
    piettoon_koud > master 
dependencies:
    tkinter comes pre-installed (no need to pip install)
    must still import the required library (from tkinter import *)
"""

#-----topic------------dependencies --------------------------------------------------------top-----
from tkinter import *
#-----topic------------dependencies -----------------------------------------------------bottom-----

def calculate():
    user_value = e1.get()
    print(type(user_value))
    result = int(user_value)*10
    label2 = Label(window, text = result, font = "times 18")
    label2.place(x=450, y=70)

#-----topic------------window/class instance of Tk------------------------------------------top-----
window = Tk() #windows are the containers (parent) in which all other widgets (GUI elements) live
#window (i.e. name of the parent) often becomes the first parameter when creating other widgets
#example:   label1 = Label(window, text="Menu")
window.geometry("700x500-50+40") 
#"widthxheight+x+y" with width, height in pixels and +x or -x the horizontal distance 
# from the screens's left or right edge, and +y or -y the vertical distance from screen's
# top or bottom edge 
#-----topic------------window/class instance of Tk---------------------------------------bottom-----



#-----topic------------label ---------------------------------------------------------------top-----
label1 = Label(
    window,
    text="Menu",
    font="times 28 bold",
    foreground="white", # Set the text color
    bg="red",    # "orange" "yellow" "green" "blue" "purple" "black" or hexadecimal RGB values
    width=20,
    height=4
)
label1.place(x=250, y=70)
#refer reference1 for a list of valid colors and tools to get hexadecimal color codes
#fg and bg can be used as shorthand for foreground and background
#-----topic------------label ------------------------------------------------------------bottom-----
'''


#-----topic------------Entry ---------------------------------------------------------------top-----
e1 = Entry(fg="yellow", bg="blue", width=50) #allows only single line of text to be entered
e1.place(x=550, y=50)
#the user can now input text, or it can be programmatically inserted
e1.insert(0, "Real Pytython") #text is inserted at position 0
e1.delete(7, 9) #delete a slice of text
usr_input = e1.get() #retrieving text
print(usr_input)
#deleting first character of the text with e1.delete(0)
#delete all text e1.delete(0, END)

#-----topic------------Entry ------------------------------------------------------------bottom-----



#-----topic------------Text ----------------------------------------------------------------top-----
#allows multiline text entry
#same .get(), .insert() and .delete() operations as with Entry
text_box = Text()
text_box.pack() #
usr_text = text_box.get("1.0", END) #get characters from line 1, position 0 up to the END
#get() also shows the \n characters, which can also be deleted to remove blank lines from the text_box
#if line 1 is filled, but line 2 is empty, then insert("2.0", "world") will not insert text in line 2, 
# but will simply append it to line 1. insert("2.0", "\nworld") will insert in new line 2  OR
#text_box.insert(END, "Put me at the end!")
#-----topic------------Text ----------------------------------------------------------------top-----



#-----topic------------Frame ---------------------------------------------------------------top-----
#a rectangular region to group related widgets or provide padding between widgets
#-----topic------------Frame ---------------------------------------------------------------top-----



#-----topic------------Button --------------------------------------------------------------top-----
b1 = Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=calculate
)
b1.place(x=550, y=120)
#-----topic------------Button -----------------------------------------------------------bottom-----

'''

#-----topic------------mainloop() --------------------------------------------------------top-----
window.mainloop() #runs the Tkinter event loop (listening for events) until this window is closed
#window is closed manually by clicking X in window, or programmatically by window.destroy()
#-----topic------------mainloop() -----------------------------------------------------bottom-----
