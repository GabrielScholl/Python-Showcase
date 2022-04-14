# Functions

def myfunc(arg): # <- parameter
    arg = 1
    return arg

myfunc("dope") # <- argument (args in the documentation)

# Arbitrary Arguments (*args)
def parker(*cars): # *arg allows passing of many 1+ arguments, will enter as tuple
    garage = list(cars)
    return garage

print(parker(['NSX', 'Civic'])) # One argument, a list that became the only el. in tuple
print(parker('NSX', 'Civic')) # Two arguments, making a tuple with 2 entries

# Keyword Arguments - (key = value syntax)
def multivaried(x,y,z):
    return x+y*z

print(multivaried(y=5, x=12, z=2)) # Arguments passed as key-value pairs in no particular order

# Arbitrary Keyword Arguments (**kwargs)
def printer(**records):
    print("Patient name: "+str(records["name"]))
    pass

john_records = {
    "name": "John",
    "age": 35
}

try:
    printer(john_records)
except:
    print("Passing a dict won't work")

printer(name="July", age=24, sex="F") # Only works with individual entries

# Default argument
def race(ready=False):
    if ready:
        print("Go!")
    else:
        print("Not ready!")

ready = True
race(ready)

# Pass
def useless():
    pass
useless()

# Recursion
def factorial(n):
    if n in {0, 1}: # Trivial case
        return 1
    elif n > 0:
        return n*factorial(n-1) # Walk towards it, calling the function
    else: # Input is negative
        raise Exception("Input a positive number!")

print(factorial(0))
print(factorial(1))
print(factorial(5))
print(factorial(33))
try:
    print(factorial(-1))
except:
    print("Too bad")

# Lambda functions
x = lambda a, b : a + b # Variable is gonna be the function, lambda defines it, arguments in, ":", expression
print(x(5, 11))
print(x("I luv ", "U"))

def makerFunc(val): # Builds the lambda function
    return lambda a : val*a # Returns the lambda function

doubler = makerFunc(val=2) # Assign function to "doubler"

print(doubler(6)) # Uses the assigned function with input value as lambda argument


# Iterators pt.1 *pt.2 in Classes.py

foodList = ["croissant", "baguette", "caffee"]

foodIterator = iter(foodList)
print(next(foodIterator))
print(next(foodIterator))

# Scope

var = 500
def f1():
    print(var)
    def f2():
        var = 400 # This will be a different var, available only inside the func
        print(var)
        def f3():
            global var # You can create or modify the global like this
            var = 350
            print(var)
        f3()
    f2()
f1()
print(var) # var was changed inside f3()