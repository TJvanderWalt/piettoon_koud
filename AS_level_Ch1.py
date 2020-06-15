'''This module accompanies Cambridge International AS and A Level Computer Science Coursebook
by Sylvia Langfield and Dave Duddell'''

def bin_to_den(binary_code):
    '''takes as arg a whole byte(s) of binary code (i.e. a list of '0's and '1's as
    characters) and returns a (positive) denary number'''
    denary_number = 0
    binary_code.reverse()
    i = 0
    for bit in binary_code:
        denary_number += (2**i)*int(bit)
        i+=1
    return denary_number

def den_to_bin(denary_number):
    '''takes a (positive) denary number as arg and returns a whole byte(s) of binary code
    (i.e. a list of 0'1 and 1's as characters)'''
    binary_code = []
    if denary_number < 0:
        denary_number *= -1
    while denary_number > 0:
        binary_code.append(str(denary_number%2))
        denary_number //= 2
    code_len = len(binary_code)
    if code_len%8 > 0:
        for _ in range(8-code_len%8):
            binary_code.append('0')
    binary_code.reverse()
    return binary_code

def DtoB(denary_Num):  #ALTERNATE DENARY TO BINARY
    """Takes a positive denary in bounds of (1 - 1,048,576) number and returns the binary equivalent in a list form"""
    two_Powers = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576]
    binary_List = []

    den = denary_Num 

    for i in range(len(two_Powers)):
        if two_Powers[i] > denary_Num:
            i -= 1 
            break

    while int(i) >= 0:
        subtract = denary_Num - two_Powers[i]  
        if subtract >= 0:
            binary_List.append(1)
            denary_Num = subtract
        else:
            binary_List.append(0)
        i -= 1

    print(f"The Deciaml number {den} in binary is {binary_List}.")

    input("")
    return(binary_List)

def add(bin_code1, bin_code2):
    '''takes two binary codes (i.e. lists of 0's and 1's characters) as args and returns their sum
    as a binary number (list of 0'1 and 1's characters)'''
    carry = 0
    sum = []
    len_1 = len(bin_code1)
    len_2 = len(bin_code2)
    if len_1 >= len_2:
        bin_code1.reverse()
        bin_code2.reverse()
        for _ in range(len_1 - len_2):
            bin_code2.append('0')
    elif len_1 < len_2:
        bin_code1.reverse()
        bin_code2.reverse()
        for _ in range(len_2 - len_1):
            bin_code1.append('0')
    for i in range(max(len_1, len_2)):
        if carry + int(bin_code1[i]) + int(bin_code2[i]) == 0:
            sum.append('0')
            carry = 0
        elif carry + int(bin_code1[i]) + int(bin_code2[i]) == 1:
            sum.append('1')
            carry = 0
        elif carry + int(bin_code1[i]) + int(bin_code2[i]) == 2:
            sum.append('0')
            carry = 1
        else:
            sum.append('1')
            carry = 1
    sum.reverse()
    bin_code1.reverse()
    bin_code2.reverse()
    #print(bin_code1)
    #print(bin_code2)
    return(sum)

def add_twos(bin_Num1, bin_Num2): # ALTERNATE ADDING OF BINARY
    """Take two binary numbers (in list form) and adds them, (returns a single list)"""
    answer = []
    left_Over = 0

    for i in range(len(bin_Num2) - 1, -1, -1) :
        if bin_Num1[i] == 0 and bin_Num2[i] == 0: # 0 & 0
            if left_Over == 1:
                answer.insert(0, 1)
                left_Over = 0
            else:
                answer.insert(0, 0)
        elif (bin_Num1[i] == 1 and bin_Num2[i] == 0) or (bin_Num1[i] == 0 and bin_Num2[i] == 1): # 0 & 1
            if left_Over == 1:
                answer.insert(0, 0)
            else:
                answer.insert(0, 1)
        else: # 1 & 1
            if left_Over == 1:
                answer.insert(0, 1)
                left_Over == 1
            else:
                answer.insert(0, 0)
                left_Over = 1
    
    print(f"the addition of: {bin_Num1} and: \n\t\t {bin_Num2} = {answer}")
    return answer

def den_to_twos(denary_number):
    '''takes either a positive or a negative integer number as arg and returns the two's complement
    as a whole byte(s) of 0's and 1's characters'''
    twos_complement = []
    ones_complement = []
    if denary_number >= 0:
        twos_complement = den_to_bin(denary_number)
    else:
        binary_code = den_to_bin(denary_number)
        binary_code.reverse()
        for bit in binary_code:
            if bit == '0':
                ones_complement.append('1')
            else:
                ones_complement.append('0')
        ones_complement.reverse()
        twos_complement = add(ones_complement, ['1'])
    return twos_complement


def bin_to_two(binary_Num): #ALTERNATE CONVERTING BINARY TO TWOS
    """Takes a binary number (as a list) of any length and converts it to twos complement (returns a list)."""
    length = len(binary_Num)
    j = 0
    i = -1

    while length % 8 != 0:
        binary_Num.insert(0, 0)
        length = len(binary_Num)

    while j != 1:
        if binary_Num[i] == 0:
            i -= 1
        else:
            j = 1
            i -= 1

    for index in range(i, -len(binary_Num) - 1, -1):
        if binary_Num[index] == 0:
            binary_Num[index] = 1
        else:
            binary_Num[index] = 0
    return binary_Num

def twos_to_den(twos_compl):
    '''takes a twos complement (a list being a whole byte(s) of 0's and 1's characters) 
    and returns the denary number'''
    binary_code=[]
    if twos_compl[0] == '0':
        return bin_to_den(twos_compl)
    else:
        twos_compl.reverse()
        for bit in twos_compl:
            if bit == '0':
                binary_code.append('1')
            else:
                binary_code.append('0')
        binary_code.reverse()
        binary_code = add(binary_code, ['1'])
        return -bin_to_den(binary_code)

def byte_maker(binary_Num):
    """takes a binary number of any size and creates a full byte out of it (returns a list)."""
    length = len(binary_Num)
    while length % 8 != 0:
        binary_Num.insert(0, 0)
        length = len(binary_Num)
    return binary_Num

def len_Checker(bin_Num1, bin_Num2):
    """checks if two binary lists and checks if they are the same length,
     if not it makes then the same length and returns both nums in list form"""
    if len(bin_Num1) > len(bin_Num2):
        while len(bin_Num2) < len(bin_Num1):
            bin_Num2.insert(0, 0)
    else:
        while len(bin_Num1) < len(bin_Num2):
            bin_Num1.insert(0, 0)
    return bin_Num1, bin_Num2

def sum_of_ints(int_1, int_2):
    '''takes two integer numbers as args and returns their integer sum by making use of
    twos complements'''
    compl_1 = den_to_twos(int_1)
    compl_2 = den_to_twos(int_2)
    compl_sum = add(compl_1, compl_2)
    return twos_to_den(compl_sum)



#uncomment the three lines below to run bin_to_den() as a script
#bin_number = list(input("Enter a binary code as a string of 0's and 1's: "))
#den_number = bin_to_den(bin_number)
#print(den_number)

#uncomment the three lines below to run den_to_bin() as a script
#den_number = int(input("Enter a denary number: "))
#bin_number = den_to_bin(den_number)
#print(bin_number)

#uncomment the three lines below to run DtoB() as a script
#denary_Num = int(input("Enter a Denary number: "))
#bin_number = DtoB(denary_Num)
#print(bin_number)

#uncomment the four lines below to run add() as a script
#bincode_1 = list(input("Please enter a binary code as a string of 0's and 1's: "))
#bincode_2 = list(input("Please enter a binary code as a string of 0's and 1's: "))
#added_bincode = add(bincode_1, bincode_2)
#print(added_bincode)

#uncomment the four lines below to run add_twos() as a script
#bin_Num1 = [1,0,0,1,1,0,1,1]
#bin_Num2 = [0,1,1,1,0,0,1,0]
#added_bincode = add_twos(bin_Num1, bin_Num2)

#uncomment the two lines below to run den_to_twos() as a script
#den_num = int(input("Please enter a positive or negative number : "))
#print(den_to_twos(den_num))

#uncomment the two lines below to run bin_to_two() as a script
#bin_List = [0,0,1,1,0,1,0,0]
#twos_Bin = bin_to_two(bin_List)
#print(twos_Bin)

#uncomment the two lines below to run twos_to_den() as a script
#twos_complement = list(input("Enter the twos complement as a string of 0's and 1's: "))
#print(twos_to_den(twos_complement))

#uncomment the three lines below to run len_Checker() as a script
#bin_Num1 = [1,0,0,1,1,0,1,1,0,1]
#bin_Num2 = [0,1,1,1,0,0]
#answer = len_Checker(bin_Num1, bin_Num2)
#print(answer)

#uncomment the three lines below to run byte_maker() as a script
#bin_Num1 = [1,0,0,1,0,1,0]
#byte = byte_maker(bin_Num1)
#print(byte)

#uncomment the three lines below to run sum_of_ints() as a script
#int_first = int(input("Enter a first positive or negative integer: "))
#int_second = int(input("Enter a second positive or negative integer: "))
#print(sum_of_ints(int_first, int_second))