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

# Sequences -----------------------------------------------------------------------------------------
# Mapping -------------------------------------------------------------------------------------------
# Sets ----------------------------------------------------------------------------------------------
# Booleans ------------------------------------------------------------------------------------------
# Binaries ------------------------------------------------------------------------------------------