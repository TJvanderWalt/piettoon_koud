'''This module accompanies Cambridge International AS and A Level Computer Science Coursebook
by Sylvia Langfield and Dave Duddell'''

def bin_to_den(binary_code):
    '''takes as arg a binary code (as a list of 0's and 1's characters) and returns a (positive)
    denary number'''
    denary_number = 0
    binary_code.reverse()
    i = 0
    for bit in binary_code:
        denary_number += (2**i)*int(bit)
        i+=1
    return denary_number

def den_to_bin(denary_number):
    '''takes a (positive) denary number as arg and returns a full byte of binary code
    (as a list of 0'1 and 1's characters)'''
    binary_code = []
    while denary_number > 0:
        binary_code.append(denary_number%2)
        denary_number //= 2
    code_len = len(binary_code)
    if code_len%8 > 0:
        for _ in range(8-code_len%8):
            binary_code.append('0')
    binary_code.reverse()
    return binary_code

def add(bin_code1, bin_code2):
    '''takes two binary codes (i.e. lists of 0's and 1's) as args and returns their sum
    as a binary number (list of 0'1 and 1's characters)'''
    carry = 0
    sum = []
    len_1 = len(bin_code1)
    len_2 = len(bin_code2)
    if len_1 > len_2:
        bin_code1.reverse()
        bin_code2.reverse()
        for _ in range(len_1 - len_2):
            bin_code2.append('0')
    elif len_1 < len_2:
        bin_code1.reverse()
        bin_code2.reverse()
        for _ in range(len_2 - len_1):
            bin_code1.append('0')
    for i in range(len_1):
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
    '''takes either a positive or a negative integer number as arg and returns the two's complement'''
    twos_complement = []
    if denary_number >= 0:
        binary_code = den_to_bin(denary_number)
        binary_code.reverse()
        len_twos = len(binary_code)
        if len_twos%8 > 0:
            for _ in range(8-len_twos%8):
                binary_code.append('0')
        twos_complement = binary_code            
    else:
        binary_code = den_to_bin(-denary_number)
        binary_code.reverse()
        len_twos = len(binary_code)
        if len_twos%8 > 0:
            for _ in range(8-len_twos%8):
                binary_code.append('0')
        for bit in binary_code:
            if bit == '0':
                twos_complement.append('1')
            else:
                twos_complement.append('0')
        twos_complement.reverse()
        return(add(twos_complement, '1'))



#uncomment the three lines below to run bin_to_den() as a script
#bin_number = list(input("Enter a binary code as a string of 0'1 and 1's: "))
#den_number = bin_to_den(bin_number)
#print(den_number)

#uncomment the three lines below to run den_to_bin() as a script
#den_number = int(input("Enter a denary number: "))
#bin_number = den_to_bin(den_number)
#print(bin_number)

#uncomment the four lines below to run add() as a script
#bincode_1 = list(input("Please enter a binary code as a string of 0's and 1's"))
#bincode_2 = list(input("Please enter a binary code as a string of 0's and 1's"))
#added_bincode = add(bincode_1, bincode_2)
#print(added_bincode)

#uncomment the lines below to run den_to_twos() as a script
den_num = int(input("Please enter a positive or negative : "))
print(den_to_twos(den_num))