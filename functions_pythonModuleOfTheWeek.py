"""title: functions_pythonModuleOfTheWeek (not in standard library)
topics: 
    random numbers; 
    date and time; 
    (text) file i/o; 
    ; 
    ;
reference1: 
    "Python3 Module of the week" (pymotw.com)
    
reference2:
    ""
    Yong Cui in: Better Programming (Medium.com archive)
reference3: 
    "" (realpython.com)
so what? 
    ; 
    ; 
    
further reading/links: 
    (piettoon_koud > master) built_in_functions.py ; function_decorators.py
github: 
    piettoon_koud > master 
dependencies:
    import these modules before use, since they are not part of the python standard library
"""


#-----topic------------pseudo random numbers------------------------------------------top-----------
#remove next two '''
'''
import random
sequence = ['a', 'b', 'c', 'd', 'e']
for _ in range(20):
    random_int = random.randint(1,20) #random int between 1 and 20, both 1 and 20 included
    random_choice = random.choice(sequence)
    print(random_choice, random_int)
'''
#-----topic------------pseudo random numbers---------------------------------------bottom-----------


#-----topic------------date and time--------------------------------------------------top-----------
#delete next two '''
'''
import datetime, time
today = datetime.date.today() #get today's date from the system clock
now = time.time()
print("time now is",now) #system time now, since epoch
print(f"today's date is: {today}")
past_date = datetime.date(2019, 12, 23) #yyyy, mm, dd
print("a day in the past is {0}".format(past_date))
future_date = today + datetime.timedelta(3) #3 days from today
print("three days from today will be:", future_date)
'''
#-----topic------------date and time-----------------------------------------------bottom-----------

#-----topic------------(text)file I/O-------------------------------------------------top-----------
#A text file consists of a sequence of characters for matted into lines. Each line is terminated by
#an end-of-line marker. The text file is terminated by an end-of-file marker. You can check the
#contents of a text file (or even create a text file required by a program) by using a text editor
#such as NotePad.
#delete next two '''

lines_of_text = ["First line written to file.\n", "Second line written to file.\n"] #\n needed between lines
file_handle = open("C:\\users\\administrator\\practiceFile.txt", "w") #open current file for writing 
                                                               #(create if it does not exist already)
for write_string in lines_of_text:
    file_handle.write(write_string) #write will overwrite existing file contents
file_handle.close()
#use Notepad to change file and save it
file_handle = open("C:\\users\\administrator\\practiceFile.txt", "r") #open current file for reading 
line_of_text = file_handle.readline() #read single line of text
print(line_of_text, end='')
while len(line_of_text) != 0:
    line_of_text = file_handle.readline() #read single line of text
    print(line_of_text, end='')
file_handle.close()
file_handle = open("C:\\users\\administrator\\practiceFile.txt", "a") #append date to end of file rather
                                                                    #than creating a new file
append_string="Line appended at end of file\n"
file_handle.write(append_string)
file_handle.close()                                                                    
#-----topic------------(text)file I/O----------------------------------------------bottom-----------

