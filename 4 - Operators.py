# This file will explore all operators in Python
# They're grouped by their nature:
# Arithmetic operators, Assignment op., Comparison, Logical, Identity, Membership and Bitwise.

x = 11
y = 5

# Arithmetic -----------------------------------------------------------------------------------------


print("Arithmetic")
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y) # Exponentiation
print(x // y) # Floor division - Rounds the result down to the nearest whole number
print(x % y)  # Modulus


# Assignment -----------------------------------------------------------------------------------------


print("Assignment")
x = 2;   print(x)
x += 6;  print(x)
x -= 5;  print(x)
x *= 77; print(x)
x /= 3;  print(x)
x %= 8;  print(x)
x //= 2; print(x)
x **= 9; print(x)
x = int(x)

# The following are BITWISE operations between operands and then assign to first operand.
x &= y;  print(x) # AND
x |= y;  print(x) # OR
x ^= y;  print(x) # xOR
x >>= y; print(x) # Bit Shift Right
x <<= y; print(x) # Bit Shift Left


# Comparison -----------------------------------------------------------------------------------------


x == y
x != y
x > y
x < y
x >= y
x <= y


# Logical --------------------------------------------------------------------------------------------


x and y
x or y
not y


# Identity -------------------------------------------------------------------------------------------


x is y # True if both are the same object
x is not y # True if not the same object


# Membership -----------------------------------------------------------------------------------------


x in y # True if the sequence is present in object
x not in y # True if the sequence is NOT present in object


# Bitwise --------------------------------------------------------------------------------------------


x & y # AND - Sets both to 1 if both are 1
x | y # OR - Sets both to 1 if either is 1
x ^ y # xOR - Sets both to 1 if only one is 1
~ y # NOT - Inverts all the bits
x << y # Zero fill left shift
x >> y # Signed right shift - Shifts content right, fills left with left digit