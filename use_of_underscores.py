'''title: uses of the underscore (_)
topics: 
    as an anonymous variable in loops; 
    in dunder methods;
    in snake_case naming of identifiers; 
reference1: 
    "write python code with one extra character"
    Dorel Masasa in: The Startup (Medium archive)
reference2:
    ""
reference3: 
    ""
so what? 
    ""
further reading/links: 
    piettoon_koud > master > functions_dunder_methods.py 
github: 
    piettoon_koud > master 
dependencies: 
    import ; 
'''



#-----topic------------use of _ in loops----------------------------------------------top-----------
for i in range(4):
    print(f"Copy {i} now printing!")

for _ in range(4): 
    # underscore _ is an anonymous variable in this loop since its actual value
    # is not needed further on in the program
    print("Another copy is now printing")
#-----topic------------use of _ in loops-------------------------------------------bottom-----------



#-----topic------------use of _ in dunder methods-------------------------------------top-----------
#refer to functions_dunder_methods.py for more details
#-----topic------------use of _ in dunder methods----------------------------------bottom-----------



#-----topic------------use of _ in snake_case naming----------------------------------top-----------
# snake_case (usr_first_name) compared to camelCase (useFirst_name) to name identifiers
#-----topic------------use of *args and **kwargs in functions----------------------bottom-----------