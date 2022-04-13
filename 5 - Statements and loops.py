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
fruits = ["caju", "do conde", "cajá", "romã"]
for f in fruits:
    for c in f:
        print(c)
    if f is "caju":
        continue
    if f is "romã":
        break
    for i in range(len(fruits)): print(str(i)+" done")

for i in range(5, 55, 10):
    print(i)
else:
    print("I am printed once the loop is finished, but only if not by means of a BREAK")

# Nesting
for i in range(5):
    print("Ext loop: "+str(i))
    for i in range(5):
        print("Int loop: "+str(i))
        for i in range(5):
            pass
print("The looping variable is created inside that context (only for that loop).")

# Try...exept structure
 
try: # Tries something that may generate an exception
    print(x) # This triggers the exception as "x" is not defined previously
except: # Handles it in case of an exception
    print("The variable is not defined") # With this action
else: # Happens if there was no exception
    print(x**2)
finally: # Always happens, regardless of the occurrence of an exception
    print("This was a bumpy road!")