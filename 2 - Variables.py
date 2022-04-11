# This file will cover variables

x = 5 # x receives 5
print(type(x)) # x is an int
x = 'text' # x is now a string

# Casting is changing the value type. Here we'll assign it to a variable
a = str(5) # a is now "5" as in the string with those contents
b = int(5.1) # b receives 5, an int
c = float(5) # c's value is 5.0, a float

# Capital letters
A = "I'm capitalized" # Both constructions are correct and different variables.
a = 'I\'m not' # Single or double quotes are the same thing, though now we have to use back slash to mean ' literally

print(a)

# Variables are case sensitive, can't start with a number and must start with a letter or "_"
# They may only contain numbers, letters and underscores

# Multiple variables
a, b, c, d = "Adam", 'Bobby', 44, False

# Same value
x = y = 78

# Unpacking
lista = ['Gabriel', 22, True]
name, age, is_tall = lista
print(name, age, is_tall)

# Globals
inicio = 'this is a global' # Variable available everywhere
fim = ' variable'

def juntar(): # inicio not passed as argument
    fim = ' variable' # Local variable
    print(inicio+fim)

def juntar2():
    inicio = 'this is a local' # Same name as global, but now it's a local variable and the global is untoutched
    print(inicio+fim) # Uses the global 'fim'

def juntar3():
    global inicio # This brings the global inside
    inicio = 'this global is now an edited' # Now the global variable is edited
    print(inicio+fim)