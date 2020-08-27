def func_add(base, codes_list): #list of four lists of uneven integers picked from [1, 3, 5, 7, 9, 11, 13, 15]
    '''Due to Covid19 South Africa also went into lockdown during Marh of 2020. 
    The following riddle was sent around between a few friends of mine:
    can you pick three integers (which may repeat) from this list of uneven integers
    [1, 3, 5, 7, 9, 11, 13, 15] such that the sum of these three uneven integers (x+y+z) comes
    to 30? If you view the numbers in the given list as denary numbers (i.e. base number = 10)
    then it is easy to prove that three uneven integer numbers, when added, can never result in
    an even integer number like 30. But could the equality x+y+z = 30 become true when numbers
    other than 10 are picked as base numbers? 
    ''' 
    den_list = []
    max_len = max([len(m) for m in codes_list])
    for code in codes_list:
        den = 0
        code.reverse()
        for i in range(max_len-len(code)):
            code.append('0')
        for i in range(max_len):
            den += (base**i)*int(code[i]) 
        den_list.append(den)
    print(f"The codes input, when viewed as base {base_number} numbers, lead to the equation \
{den_list[0]} + {den_list[1]} + {den_list[2]} == {den_list[3]} which evaluates to \
{den_list[0] + den_list[1] + den_list[2] == den_list[3]}")
    return den_list[0] + den_list[1] + den_list[2] == den_list[3] #returns True if equality x+y+z=30 becomes true
    
#uncomment the next seven lines to run func_add() as a script    
#base_number=int(input("Enter base: "))  #e.g. enter 5
#code_x = list(input("Enter the first code as a string of uneven integers: ")) #e.g. enter 1
#code_y = list(input("Enter the second code as a string of uneven integers: ")) #e.g. eneter 11
#code_z = list(input("Enter the third code as a string of uneven integers: ")) #e.g. enter 13
#code_sum = list(input("Enter the sum code as a string of uneven integers: ")) #e.g. enter 30
#list_of_codes = [code_x, code_y, code_z, code_sum]
#print(func_add(base_number, list_of_codes))