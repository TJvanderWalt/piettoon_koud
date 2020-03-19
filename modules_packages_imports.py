"""Modules and packages ; imports (absolute and relative)

reference 1 : Absolute vs Relative Imports in Python (course at realpython.com)

summary:
module = Python file ending in .py
package = collection of modules in a folder
why import things?
    project split into several files and in first file you want to use functionality contained in a 
    second file; after pip install of something you didn't even write yourself; imports searched in a 
    specific order - sys.modules cache of everything that has already been imported, Python Standard 
    Library, sys.path - list of directories (including current directory)
how to use?
    import csv [imports everything in this module]  
    from flask import Flask [from package flask import class Flask]
    import pandas as pd [rename everything you import]
    Tip: look at the structure of a package/module you like to import 
import styling?
    """imports normally follow immediately after a module's docstring
    """
    #Standard Library Imports
    import datatime
    import os
    ... listed alphabetically

    #Third party imports
    from flask import Flask
    from flask_restful import Api
    from flask_sqlalchemy import SQLAlchemy
    
    #Local application imports
    from local_module import local_class
    from local_module import local_function

"""

