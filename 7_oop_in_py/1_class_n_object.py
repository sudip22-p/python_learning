# ✅ Intro to OOP, Classes and Objects in Python


# Class defines blueprint
class Dog:
    def __init__(self, name):
        """Constructor method, __init_ is called when an object is created, _init_ is a special method that initializes the object in Python. self is a reference to the instance being created. name is a parameter passed to the constructor."""
        self.name = name  # instance attribute - this line assigns the name parameter to the instance attribute self.name.

    def bark(self):  # method of the class
        print(f"{self.name} says Woof!")


# Object is instance of class
dog1 = Dog("Buddy")
dog1.bark()  # Buddy says Woof!
