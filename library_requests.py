"""title: requests for interacting with the web
topics: 
    requests for interacting with the web; 
reference1: 
    "Python ..."
    Yong Cui in: Better Programming (Medium.com archive)
reference2:
    "The top ..."
    Yong Cui in: Better Programming (Medium.com archive)
reference3: 
    Martin Breuss in "Python packages: five Real Python favorites" (realpython.com)
so what? 
    programmatic interactions with the internet (e.g. posting your writing through a web API;
     or fetching data via web scraping); 
further reading/links: 
    realpython.com > tutorials > topics > Python API Tutorials (API design and interacting with APIs using python)
    (piettoon_koud > master) 
github: 
    piettoon_koud > master 
dependencies:
    not part of the Python standard library; pip install requests
"""

import requests
response = requests.get("http://www.example.com")
print(response.text)