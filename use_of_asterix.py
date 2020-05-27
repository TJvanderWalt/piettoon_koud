'''title: uses of the asterix (*)
topics: 
    use of * in multiplication (and exponentiation); 
    unpacking of iterables;
    *args and **kwargs; 
reference1: 
    "Change the way you write python code with one extra character"
    Dorel Masasa in: The Startup (Medium archive)
reference2:
    ""
reference3: 
    ""
so what? 
    ""
further reading/links: 
    piettoon_koud > master > functions_user_defined.py 
github: 
    piettoon_koud > master 
dependencies: 
    import math;
DONE:
    
TODO:
    wip wildcard (google for python wildcard)
'''

import math

#-----topic------------use of * in multiplication-------------------------------------top-----------
print(5*12)
print(5**3)
print(math.pow(5,3))

my_list = ['a' * 12]
print(my_list, '\n')
#-----topic------------use of * in multiplication----------------------------------bottom-----------



#-----topic------------use of * in unpacking iterables--------------------------------top-----------
#use * to unpack an iterable or to unpack a 2 way iterable, such as a dictionary
print([x for x in range(100)] == [*range(100)]) #prints True

my_dict = {'key1' : 'A'}
print(list(my_dict.keys()) == [*my_dict]) #prints True

print(my_dict == {**my_dict}) #prints True

dict_1 = {'key1' : 'hello', 'key2' : 'world'}
dict_2 = {'key3' : 'whats', 'key4' : 'up'}
combined_dict = {**dict_1, **dict_2}
print(combined_dict)
#-----topic------------use of * in unpacking iterables-----------------------------bottom-----------



#-----topic------------use of *args and **kwargs in functions-------------------------top-----------
#see functions_user_defined.py for more details
#-----topic------------use of *args and **kwargs in functions----------------------bottom-----------



#-----topic------------use of * as wildcard-------------------------------------------top-----------
# from math import *
#wildcard search in lists
#wildcard search in strings
#its use in regex (regular expressions)
#its use as wildcard with ?
#-----topic------------use of * as wildcard----------------------------------------bottom-----------