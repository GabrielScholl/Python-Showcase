# This file will cover data types in Python
# In Python, data can be one of 7 types:
# Text, numbers, sequences, mapping, sets, boolean or binary.
# Each one has different uses and constructions, as we'll see below.


# Numbers ------------------------------------------------------------------------------------------


a = 456 # Integer
b = 45.6 # Float
c = 45j+6 # Complex
s = 4.56e-3 # Scientific notation
print(s)

z = a+b*c # You can operate normally between types
print(z)

# Changing types
a_complex = complex(a) # This is also called casting (one type to another)
b_integer = int(b) # The int() constructor will remove any decimal information from other number formats.
# c_float = float(c) # This wont' work because complex numbers can't be shown as simple floats.

print(a_complex, b_integer)

# Random number 
import random # You can import mid-code in Python, but it's not pretty

rnd_num = random.randrange(-56,45) # Generates a random number within the given range
print(rnd_num)


# Text ----------------------------------------------------------------------------------------------
# AKA Strings


# Multi-line strings
multiline = '''This is the first line
the "enter" line break is considered too.
So this is the 3rd line.'''

# The array string nature
word = multiline[-12:] # Grab a slice of the array
char = word[2] # Grab a character which is a list item

# Looping through a string
counter = 0
for el in multiline:
    counter += 1
print("multiline has "+str(counter)+" characters.") # counter is of int type and has to be changed to string to concatenate

# Checking presence in string
is_is_in_it = "is" in multiline # Value is True.
print('is_is_in_it = '+str(is_is_in_it))

is_not_not_in_it = "not" not in multiline # Value is also True.
print('is_not_not_in_it = '+str(is_not_not_in_it))

# Length
print(len(multiline)) # Much easier

# Methods for modifying strings
print(word.upper()) # FULL STRING IN UPPER CASE
print(word.lower()) # full string in lower case
print(word.strip()) # Strip the whitespace off the BEGINNIG OR END of the string
print(word.replace('e','a')) # Replace first argument in string with second
print(word.split('.')) # Split the string in the argument to create a list

# Concatenation - just sum them
phrase = word + char + "notn" + str(8)

# Format method
# The curly brackets are the place holders, they receive inserts no matter their format
txt = "All the {} are in the {} {} which took {} minutes to make. That's a {} statement."
print(txt.format('bananas', 5, 'apple pies', 3.7, True))

# You can change the order by enumerating them
statement = '{1} is bigger than {0}'
print(statement.format(3, 4))

# Escape characters
escapes = '''The value \" is a double quote, \' inserts a quote mid-quotes,
\n creates a new line, \t is a tabulation, \f submits a form,
\b is a backspace, \\ inserts a backslash, 
this will be overwritten \r is a carriage return,
\ ooo makes an octal and \ xhh an hexadecimal.\n'''
print(escapes)

# String methods
print('gabriel'.capitalize()) # First char gets upper cased
print('GABrIEL'.casefold()) # Same as lower()
print('GABrIEL'.lower()) # Lower cases whole string
print('gaBRiel'.upper()) # Upper cases whole string
print('Gabriel'.center(20)) # Prints on total 20 chars, with string in the middle
print('Gabriel'.count('a')) # Occurencies in the string
print('Gåbrõül'.encode(encoding='ascii',errors='xmlcharrefreplace')) # Encodes replacing the unknown char
print('Gåbrõül'.encode(encoding='ascii',errors='namereplace')) # Encodes describing the strange char, more errors options
print('Gabriel'.endswith('el')) # True or false
print('Gabriel'.startswith('Gabe')) # True or false
print('Ga\tbri\tel'.expandtabs(10)) # Expands the tabs
print('Gabriel'.find('i')) # Returns position
print('Gabriel'.index('G')) # Returns index, same as .find()
print('Gabrielli'.rfind('i')) # Returns trailing position
print('Gabriel G.'.rindex('G')) # Returns trailing index, same as .rfind()
print('Gabriel {height:.2f}'.format(height=1.950)) # Has many options after the colon
print('Gabriel'.isalnum()) # Checks if all alphanumeric
print('Gabriel'.isalpha()) # Checks if all alphabetic
print('Gabriel'.isdecimal()) # Checks if all decimal
print('Gabriel'.isdigit()) # Checks if all digits
print('Gabriel'.isidentifier()) # Checks if the string is an identifier
print(isinstance('Gabriel', str)) # Checks if the input is of that instance/type
print('Gabriel'.islower()) # Checks if all lower case
print('Gabriel'.isnumeric()) # Checks if all numeric
print('Gabriel'.isprintable()) # Checks if all printable
print('Gabriel'.isspace()) # Checks if all spaces
print('Gabriel'.istitle()) # Checks if follows rules of a title - all words start and only start Uppercase
print('gabriel'.title()) # Makes it follow rules of a title - all words start and only start Uppercase
print('Gabriel'.isupper()) # Checks if all upper case
print('+'.join(("Carne","Queijo","Bacon"))) # Joins items of iterable gluing with string
print('Gabriel'.ljust(20)) # Returns left justified (by adding spaces right)
print('Gabriel'.rjust(20)) # Returns right justified (by adding spaces left)
print('Gabriel'.lstrip("G")) # Strips leading chars
print('Gabriel'.rstrip("l")) # Strips trailing chars
print('Gabriel'.strip()) # Strips leading and trailing chars (space is default)
table = 'Gabriel'.maketrans("G","J") # Defines translation
print('Gabriel'.translate(table)) # Translates
print('Gabriel is tall and handsome'.partition("is")) # Divides in 3: pre match, match, and post
print('Gabriel is tall and is handsome'.rpartition("is")) # Divides in 3: pre last match, last match, and post
print('Gabriel'.replace("a","4").replace("i","1").replace("e","3").replace("G","6").replace("b","9").replace("r","8").replace("l","7"))
print('Gabriel'.split("r")) # Split in char
print('Gabriellerson'.rsplit("r", 1)) # Split in last n char occurrencies
print('Gabriel\nBruno'.splitlines()) # Split lines
print('Gabriel'.swapcase()) # Swaps the cases
print('59.99'.zfill(5)) # Fills the start with zeroes until parameter length obtained
print('9.50'.zfill(5))


# Booleans ------------------------------------------------------------------------------------------


# Any expression will return a True or False.
print(9 > 5)

# More often than not, simple values or objects will return True.
# That will occur when it's not empty, not zero, not None and not False.
# Boolean False examples:
if not (bool("") or bool({}) or bool(()) or bool([]) or bool(0) or bool(False) or bool(None)):
    print('All False')

# Special situation where the class is read as False: if it's __len__ returns 0
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) # This returns False

# Pretty much the rest of everything returns true


# Sequences -----------------------------------------------------------------------------------------
# AKA Collections or Arrays, they can be:
# Lists []   -   Ordered ,   changeable ,    duplicates,   indexed
# Tuple ()   -   Ordered , unchangeable ,    duplicates,   indexed
# Sets  {}   - Unordered , unchangeable*, no duplicates, unindexed *items can't change, but you can add or remove
# Dict {":"} -   Ordered*,   changeable , no duplicates,   indexed *as of Python 3.7+


# Lists - O C AD I
myList = ['car', 5, True]
otherList = list(('car', 5, True)) # You can use the list() constructor
print(len(myList))

# Indexes
cars = ['Bentley', 'Bugatti', 'Beetle', 'Bora', 'Burgman']
fastest = cars[1]
brazilian = cars[2:4] # Same as [2,4[ (first parameter included, second not included)
print(cars[-4:-1]) # Always runs the list left to right

# Changing lists
newCars = ['UP', 'Gol', 'Voyage', 'Virtus']
cars[2:3] = newCars # By inserting more items than the slice specified, substitution followed by insertion will happen
print(cars)
newCars.insert(2, 'T-Cross') # Insert into index position, without substitution
print(newCars)
cars.append('Variant')
print(cars)
cars.extend(['Golf','Jetta']) # Appends any iterable (list, tuple, set, dict) without creating another dimension
print(cars)

# Removing
newCars.remove('UP') # Removes by match
newCars.pop(0) # Removes by index or last one if no index
del newCars[0] # Same as pop
print(newCars)
newCars.clear() # Empties the list
del newCars

# Looping
for el in cars:
    print(el)
# It can also be done by iterating indexes until len(list), using a while and counter, or using list comprehension
# Comprehension
[print(el) for el in cars]
# List comprehension syntax: newlist = [expression (optional manipulate output: if condition else expression) for el in iterable (optional manipulate input: if condition == True)]
# Example:
newCars = ['Taos']
otherCars = [car if car != 'Voyage' else 'Bon Voyage!' for car in cars if car not in newCars]
print(otherCars)

# Sorting
cars.sort() # Case sensitive, so not alphabetic order (all Uppercase before all lowercase)
print(cars)
cars.sort(key=str.lower) # Case insensitive
print(cars)
cars.sort(reverse=True)
print(cars)
def rule(el):
    return abs(len(el)**2-len(el))
cars.sort(key=rule, reverse=False) # The key will be the input for sorting
print(cars)
cars.reverse() # Reverse the current order
print(cars)

# Copying
vehicles_list = cars # vehicles_list will reference cars and changes will carry over
vehicles_list = cars.copy() # vehicles_list is now a different list with same values
vehicles_list = list(cars) # same as copy()

# Joining lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b # c is not linked to a or b
print(c)
a.extend(b) # extend() appends a list at the end
print(a)

# List methods
print(cars.count('Jetta')) # Number of times that value appears in the list
print(cars.index('Golf'))  # Like with strings, returns the index of first occurency
# The rest has already been used before




# Tuples - O UC AD I
# Unchangeable means no adding, removing or editing values

mytuple = ('John', 'Cena', 35, False)
print(len(mytuple))
singeItemTuple = ('Uno',) # Use a comma at the end to create a one-item tuple
otherTuple = tuple(('Uno','Duo')) # The tuple constructor
print(otherTuple)

# Indexing - same as lists

# Mutability hack - convert to List, edit and back to Tuple
mylist = list(mytuple)
mylist[2] = 36
mytuple = tuple(mylist)
print(mytuple)

# Adding tuples is allowed
tuple2 = ('6foot3',)
mytuple += tuple2
print(mytuple)
del tuple2

# Unpacking a tuple
name, surname, age, reality, height = mytuple
print(height)
*fullname, age, reality, height = mytuple # Less output variables than items in tuple, use * and Python will dump stuff in a list there accordingly
print(fullname)

# Loop you can

# Join
joined = mytuple + otherTuple

# Repeat
repeating = otherTuple * 5
print(repeating)

# Tuple methods
repeating.count('Uno') # Counts how many occurencies
repeating.index('Duo') # Returns the position




# Sets ----------------------------------------------------------------------------------------------


# Sets - UO UC* ND UI *no edit, just add and remove
mygarage = {458, 'Lambo', 'Prius', 'Cadillac', 'Bentley', 'Rolls'}
ihave = len(mygarage)
print("I own "+str(ihave)+" cars.")
keyBowl = set(mygarage) # The set constructor

def go_for_a_ride():
    return
if 'Lambo' in keyBowl:
    go_for_a_ride()
print(keyBowl)

def bought_new_car(carName):
    mygarage.add(carName)
    keyBowl.add(carName)

beach_house = list(('Buggy', 'Land Rover', 'Africa Twin'))
keyBowl.update(beach_house) # Same as union below
keyBowl.union(set(beach_house+['Jetta', 'Buggy'])) # Same as update, both delete duplicates
print(keyBowl)
def got_a_lawsuit():
    mygarage.remove(458) # Will raise error if the item isn't in the list
    mygarage.discard('Plane') # WON'T raise error

def lost_key():
    keyBowl.pop() # Removes last item, which is RANDOM
lost_key()
print(keyBowl)

def feds_coming():
    beach_house.clear()
    del beach_house

# Can loop sets

# Venn Diagrams, Intesections and Bentleys
farm = {'Bentley', 'Land Rover', 'Plane'}
common_cars = mygarage.intersection(farm) # Could end in _update()
print(common_cars)
mygarage.symmetric_difference_update(farm) # All but intersection
print(mygarage)
mygarage.difference_update(farm) # A.dif(B) -> A - B (shows just B exclusives)
print(mygarage)


# Set Methods
farm_key_bowl = farm # Dependent
future_farm = farm.copy() # Independent
A, B = set(beach_house), farm
A.isdisjoint(B) # True if no intersection between A and B
A.issubset(B) # True if A is contained in B
A.issuperset(B) # True if B is contained in A




# Mapping -------------------------------------------------------------------------------------------


# Dictionaries - O* C ND I *as of Python 3.7
carDict = {
    "make": "Mazda",
    "model": "Rx-7",
    "year": "1998",
    "year": "1997", # Repetitions will overwrite the previous data and won't be counted in len()
    "VIN": "JP762NA25-13B",
    "Mileage": 86000,
    "unit": "km",
    "condition": "pristine",
    "rotary": True,
    "colors": ["black", "orange"]
}

print(carDict["year"])
print(len(carDict))
print(carDict.get("condition"))
print(list(carDict.keys())) # List keys

def addColors(colors):
    carDict["colors"] += colors # Operating values inside a dictionary

addColors(["white", "red", "blue", "yellow"])
print(carDict)
print(carDict.values()) # List the values
carDict["drive side"] = "right hand drive"
print(carDict.items()) # Keys and values as tuples

[print('Y') if "model" in carDict else print('N')] # Checking presence only works for keys
[print('Y') if "Mazda" in carDict else print('N')]

carDict.update({"unit": "miles"}) # Can use the update() method inputting a dict or key-value pair to change the dict

# Removing
carDict.pop("rotary") # Pops the key-value
carDict.popitem() # Pops last key-value in *3.7+, random in 3.6-
del carDict["VIN"]

# Can loop
for el in carDict: # Loops keys
    pass
for el in carDict.values(): # Loops values
    pass
for el in carDict.items(): # Loops key-values as tuples
    print(el)

# Copying
cars2 = carDict # Both are now linked
cars2 = carDict.copy() # Different entities
cars2 = dict(carDict) # Different entities

carDict.clear() # Not needed if del is used
del carDict

# Dict Nesting
car3 = {
    "make": "Supreme",
    "model": 911
}
garage = {
    "Bimmer": {
        "make": "BMW",
        "model": "325i"
    },
    "Hummer": {
        "make": "Hummer",
        "model": "H1"
    },
    "Surprise": car3
}

from pprint import pprint # For pretty printing dictionaries

pprint(garage)

# Methods for dicts
pprint(dict.fromkeys(("name", "surname", "age"), ("Colin", None, 5))) # dict.fromkeys() creates a dict using keys, optional: values
print(garage.setdefault("Bimmer",None)) # If key doesn't exist, create with and return value, else return its value
print(garage.setdefault("FIAT","Fix It Again, Tony"))

