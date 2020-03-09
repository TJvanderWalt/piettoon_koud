"""
title: list_comprehensions 
summary and context: lists comprehensions are a concise way to create lists; alternatives include the 
use of for loops over an iterable and also using the map() function
reference-1: "9 Things to know to master list comprehensions in Python" by Yong Cui in Better Programming
reference-2: "When to use a list comprehension in Python" by James Timmins (realpython.com)
so what? can use list comprehensions to create powerful functionality within a single line of code; they can be
used too much, though (making code harder to read)
further reading/links: search realpython.com and Medium app
dependencies: Python3
github: piettoon_koud_master

"""

#First thing: 
# list comprehensions has the form [expression for item in iterable]
#expanded form is ... for item in iterable:
#                         expression

#Second thing: Create a list more conveniently
pets = ("bird", "snake", "dog", "turtle", "cat", "hamster") #a tuple
uppercase_pets = [] #an empty list
for pet in pets: #a tuple is iterable
    uppercase_pets.append(pet.upper())
print(uppercase_pets) 

print("")

#the for loop statement can be compressed into one line - using the list comprehension with just one 
# line of code, we can conveniently create a list by iterating the original list
uppercased_pets = [pet.upper() for pet in pets]
print(uppercased_pets)

print("")

#Third thing: conditional statement for filtering items in original iterable
# [expression for item in iterable if some_condition]
#expanded form:
#for item in iterable:
#   if some_condition:
#       expression
primes = [2,3,5,7,11,13,17,19,23,29]
squared_primes = [x*x for x in primes if x%10 == 3]
print(squared_primes)

#for a more complicated evaluation of condition, one can even use a function
def has_four_legs(pet):
    return pet in ("pig", "dog", "turtle", "hamster", "cat") #equivalent to ... if pet in tuple:  return pet
four_legs_pets = [pet.capitalize() for pet in pets if has_four_legs(pet)]
print(four_legs_pets)

print("")

#Fourth thing: sometimes we do't want to filter out items from the original list. Instead, we want tp 
# evaluate the condition to determine which expression is used
#basic syntax
#[expression0 if some_condition else expression1 for item in iterable]
max_value = 10
numbers = (7, 9, 11, 4, 3, 2, 12)
ceiling_numbers = [number if number <= max_value else max_value for number in numbers]
print(ceiling_numbers)

print("")

#Fifth thing: replace map() function, when used to create a lsit, by the list comprehension
#see reference1 for more

#Sixth thing: nested list comprehension
#expanded form
nested_numbers = ((1, 4, 7, 8), (2, 3, 5))
#   squares = []
#   for sublist in nested_numbers:
#        for item in sublist:
#           squares.append(item**2)
#   print(squares)
#basic syntax of the nested list comprehensions
#[expression for sublist in outer_list for item in sublist]
squares = [x**2 for sublist in nested_numbers for x in sublist]
print(squares)

print("")

#Seventh thing: use Walrus (:=) operator (Python 3.8)
#see reference1 for more

#Eighth thing: set comprehension
#use curly braces instead of square brackets; sets (unlike lists) wont have duplicate elements
# syntax for set comprehension
# {expression for item in iterable} 
numbers = (1, 34, 5, 8, 10, 12, 3, 90, 70, 70, 90)
unique_even_numbers = {number for number in numbers if number%2 == 0}
print(unique_even_numbers)

print("")

#Ninth thing: dict comprehension
#syntax for dict comprehension
#{key expression : value expression for item in iterable}
words = ("python", "is", "a", "big", "snake")
len_words = {word : len(word) for word in words}
print(len_words)
len_words_p = {word : len(word) for word in words if word.startswith('p')}
print(len_words_p)