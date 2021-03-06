import mymodule as mm
from mymodule import merger as mg # Importing just a function

print(mm.pi) # Values/variables from the module
print(mm.merger(str(mm.pi), mm.favCar)) # Functions from module

print(dir(mm)) # dir() lists all funcions and variable names in a module
[print(func) for func in dir(mm)]

print(mg(1,2)) # Using the named function

# Datetime MODULE
import datetime as dt
print(dir(dt))
now = dt.datetime.now()
print(now.year)
print(now.strftime("%A"))
date = dt.datetime(2025,12,25)
print(date.strftime("%b %d, %Y"))

# Math MODULE
print( # Some are built-in
    min(2,3),
    max(5,1),
    abs(round(-66/7,2)),
    pow(3,6)
)
import math
print(
    math.ceil(
        math.sqrt(
            math.floor(
                math.pi
            )
        )
    )
)

# JSON Module - JavaScript Object Notation
import json

egg_json = '{"white":"has", "yolk":"has", "shell":"not present"}' # Some json
egg_dict = json.loads(egg_json) # Loads it into Python dict
print(egg_dict)
egg_ben_e_dict = json.dumps(egg_dict, indent=4, separators=(". "," = "), sort_keys=True) # Dumps it back into JSON
print(egg_ben_e_dict)

# RegEx MODULE
import re

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ante."

# RegEx functions
first = re.findall('it', lorem) # Returns a list of all matches
second = re.search('[a-g]', lorem) # Returns a Match Object if at least one match
third = re.split("it", lorem) # Splits in the matches, returns list
fourth = re.sub("a.*", "NEY", lorem) # Substitutes matches

print(first, second, third, fourth)

# The website https://regexr.com/ is a great tool for learning and working with RegEx.
# Although it only works with JavaScript and PHP regex flavors, they have a lot in common with Python's flavor of RegEx.