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

a_complex = complex(a)
b_integer = int(b)
# c_float = float(c) # This wont' work because complex numbers can't be shown as simple floats.

print(a_complex, b_integer)

# Random number 

import random # You can import mid-code in Python, but it's not pretty

rnd_num = random.randrange(-56,45) # Generates a random number within the given range
print(rnd_num)

# Sequences -----------------------------------------------------------------------------------------
# Text ----------------------------------------------------------------------------------------------
# Mapping -------------------------------------------------------------------------------------------
# Sets ----------------------------------------------------------------------------------------------
# Booleans ------------------------------------------------------------------------------------------
# Binaries ------------------------------------------------------------------------------------------