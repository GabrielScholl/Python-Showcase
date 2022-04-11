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
import random
from xml.dom.pulldom import SAX2DOM # You can import mid-code in Python, but it's not pretty

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
# Mapping -------------------------------------------------------------------------------------------
# Sets ----------------------------------------------------------------------------------------------
# Binaries ------------------------------------------------------------------------------------------