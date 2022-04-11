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

# The following are BITWISE operations between operands and assign to first operand.
x &= 2;  print(x) # AND
x |= 2;  print(x) # OR
x ^= 2;  print(x) # xOR
x >>= 2; print(x) # Bit Shift Right
x <<= 2; print(x) # Bit Shift Left


# Comparison -----------------------------------------------------------------------------------------
# Logical --------------------------------------------------------------------------------------------
# Identity -------------------------------------------------------------------------------------------
# Membership -----------------------------------------------------------------------------------------
# Bitwise --------------------------------------------------------------------------------------------