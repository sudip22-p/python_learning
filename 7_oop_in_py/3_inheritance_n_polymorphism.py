# Inheritance and Polymorphism


# Base class (Parent class)
class Animal:
    def speak(self):
        print("Some sound")  # Generic method, will be overridden in child classes


# Derived class (inherits from Animal)
class Cat(Animal):
    def speak(self):
        print("Meow")  # Overrides Animal's speak method (method overriding)


# Another derived class
class Dog(Animal):
    def speak(self):
        print("Woof")  # Also overrides Animal's speak method


# Creating a list of animal objects
animals = [Cat(), Dog()]  # Both are treated as type Animal (base class)

# Polymorphism in action:
# Although all objects are of type Animal (base),
# each calls its own overridden version of `speak()`
for a in animals:
    a.speak()  # Output: Meow, then Woof

"""
Explanation:
- Inheritance allows Cat and Dog to reuse the Animal class structure.
- Polymorphism allows us to use the same method name (`speak`) but different behavior.
- Looping over a list of Animal-type objects and calling `speak()` lets each object respond in its own way.
"""
