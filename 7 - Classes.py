# Classes are like the blueprint for creating objects in Python

# Fixed property class
class MyEyeClass:
    color = "blue" # This is a property of this class

myEye = MyEyeClass() # Creates the object with the class properties
print(myEye.color)

# Class with assignable property values
class Car:
    def __init__(self, color, country, name): # Parameters to be arguments when creating the object with Car class
        self.color = color # Assigns the arguments entered to "object.properties"
        self.country = country
        self.name = name

    def drive(self): # Unlike the __init__(), others don't auto-call themselves. "self" grants access to the class properties and variables
        print("{} car from {} goes VROOOM".format(self.color, self.country)) # .format() is likely a method of the string class
    
    def wash(pipipupu): # "Self" is always the first parameter, no matter the name you use
        print("Bling bling! {} is clean. Look at that {}!".format(pipipupu.name, pipipupu.color))

supra = Car("Red", "Japan", "Supra")
supra.drive() # Not drive(supra) because the method is a function of the object and not a global method using the object
supra.wash()

# Modifying object properties
def paint(car, newColor):
    car.color = newColor # Modify the object property

paint(supra, "Faint Sky Blue Metallic")
supra.drive()

del supra.color # Oh no, the supra is now colorless, invisible, no color exists anymore, no such property, not'n!
del supra # You could've at least sold it to a happy new owner! The class is still there to create new cars tho...

class Plane:
    pass # Just so it's not empty

# Child class / Inheritance