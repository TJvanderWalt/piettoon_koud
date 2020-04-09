""" TOPIC: function_decorators (Part2)

SUMMARY & CONTEXT: functions as first-class objects; closures, decorators, design patters 
and meta-programming

REFERENCE-1: "Python function decorators - a brief tutorial" by Mark A. Brennan in The Startup

reference-2: " ... a list comprehension in Python" by Jnr Programmer (mypython.com)

SO WHAT? We can use list comprehensions too much, though (making code harder to read)

FURTHER READING/LINKS: search realpython.com and Medium app

DEPENDENCIES: Python3, 

GITHUB: piettoon_koud_master
"""



def permutation(a_list): 
    """this outer function does the first part of the work e.g. produce permut_big_list of all possible ways to
    pick 3 numbers (which may be the same) from the numbers in a_list"""
    permut_small_list = [] #list of three numbers picked
    permut_big_list = []   #list of lists
    for first_number in a_list:
        for second_number in a_list:
            for third_number in a_list:
                permut_small_list.append(first_number)
                permut_small_list.append(second_number)
                permut_small_list.append(third_number)
                copy_list = permut_small_list.copy()
                permut_big_list.append(copy_list)
                permut_small_list.clear() #this would also clear out small_list within big_list if it were not
                #for a copy of small_list that had been appended to big_list
    def base_number(base): 
        """inner function defined within the outer function; this inner function (having access to the work done
        by the outer function) will then do additional work where the outer function left off""" 
        for small_list in permut_big_list:
            denary = 0
            for num in small_list:
                if num%10 >= base or num//10 >= base: #with base number = 8 (say) num=x or num=xx with x limited
                    #to the digits 0 through 7 (num=7 and num=15 are allowed, for example, but num=9 is not allowed)
                    break
                denary = denary + num%10 + base*(num//10)
            if denary == 30:
                return f"{small_list} {base}"
    return base_number #returns a function that will continue the work where the first function left off



my_list = [1, 3, 5, 7, 9, 11, 13, 15] #note: only numbers allowed, no letters are used

riddle = permutation(my_list) #calls outer function to do the first part of some work and to return a 
#further function that will then complete the rest of the work
for i in range(1, 11): #without the option to use letters, base 10 is the upper limit
    print(riddle(i)) #call on the further function to complete the rest of the work