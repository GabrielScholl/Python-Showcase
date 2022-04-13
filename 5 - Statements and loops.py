# This file will go over the statements, loops and similar structures present in Python.

# IF
if True:
    pass
elif False:
    pass
else:
    print("Döës thïs ëvëñ häppëñ?")

# Shorthand if
if 2 > 1: print("Correct")

# Shorthand if-else
print("Happened") if True else print()
print() if False else print() if False else print("Comma") if False else print("not'n")

# Nested
if True:
    if False or True:
        if False and False:
            print("lvl 3")
        print("lvl 2")
    print("lvl 1")
print("lvl 0")


# Loops - WHILE, FOR

# While
i = 0
while i < 6:
    if i == 3:
        i += 1
        continue # Stop this iteration and continue with the next
    elif i == 5:
        pass
    else:
        print("not over yet"+str(i))
    i += 1
else: # Else used for when the WHILE is no longer true
    print("i is more than 5: "+str(i))
    while i < 10:
        if i > 6:
            break
        i += 1
        print()

# For
