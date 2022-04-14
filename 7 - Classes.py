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
        print("{} car from {} goes VROOOM...".format(self.color, self.country)) # .format() is likely a method of the string class
    
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

# Child class / Inheritance
class KeiCar(Car): # The child class will inherit the properties of the input class
    def __init__(self, color, country, name, shape, size): # If we declare the __init__ function, it will lose the parent __init__
        Car.__init__(self, color, country, name) # This includes Car's __init__ back in
        super().__init__(color, country, name) # Includes all parent's methods plus __init__ (doesn't it do that automatically?)
        self.shape = shape # We can add more properties
        self.size = size
    
    def state(self):
        print("I am a {} {}.".format(self.size, self.shape))
        try:
            print("I am {} and I will get a wash:".format(super().color)) # super() returns the super class (the parent)
        except: # But super() doesn't seem to allow access to properties, just methods, so an error is raised
            print("Also, I'm {} and I will get a wash:".format(self.color)) # Luckily we inherited the color property
        else:
            pass
        finally:
            super().wash() # From the super() returned class, we call it's method

fit = KeiCar("Silver", "Japan", "Honda Fit", "Box", "Small")
fit.state()
fit.drive()

class MuscleCar(Car):
    pass # Just so it's not empty

# Creating an iterator (Iterators pt.2)
class IteratorMultiplicator:
    def __init__(self, start, step, stop):
        self.it = start # Sets initial value
        self.step = step
        self.stop = stop

    def __iter__(self): # Defines the starting value for the iterator
        return self.it # Returns the iterator, or the current iteration

    def __next__(self): # Defines the rule of iteration
        if self.it < self.stop:
            current = self.it # Saves the current before generating the next
            self.it *= self.step # Creates the next when the function next() is called.
            return current # You have to return the first value when next() is first called.
        else:
            raise StopIteration

power2 = IteratorMultiplicator(1,2,9999999)
while True:
    print(next(power2))