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

#uncomment the four lines below to run add() as a script
#bincode_1 = list(input("Please enter a binary code as a string of 0's and 1's: "))
#bincode_2 = list(input("Please enter a binary code as a string of 0's and 1's: "))
#added_bincode = add(bincode_1, bincode_2)
#print(added_bincode)

#uncomment the two lines below to run den_to_twos() as a script
#den_num = int(input("Please enter a positive or negative number : "))
#print(den_to_twos(den_num))

#uncomment the two lines below to run twos_to_den() as a script
#twos_complement = list(input("Enter the twos complement as a string of 0's and 1's: "))
#print(twos_to_den(twos_complement))

#uncomment the three lines below to run sum_of_ints() as a script
#int_first = int(input("Enter a first positive or negative integer: "))
#int_second = int(input("Enter a second positive or negative integer: "))
#print(sum_of_ints(int_first, int_second))