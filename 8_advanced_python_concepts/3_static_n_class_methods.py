class Student:
    # Class attribute (shared by all instances)
    school_name = "XYZ School"

    def __init__(self, name):
        # Instance attribute (unique to each object)
        self.name = name

    def show(self):
        """
        Regular instance method:
        - Takes 'self' (instance) as the first argument.
        - Can access both instance and class attributes.
        """
        print(f"👤 Student Name: {self.name}")

    @classmethod
    def change_school(cls, new_name):
        """
        Class method:
        - Takes 'cls' (class) as the first argument.
        - Can access and modify class-level data.
        - Useful for factory methods or managing class-wide state.
        """
        cls.school_name = new_name
        print(f"🏫 School changed to: {cls.school_name}")

    @staticmethod
    def greet():
        """
        Static method:
        - No access to instance (self) or class (cls).
        - Acts like a regular function but grouped logically within class.
        - Use for general utility functions.
        """
        print("👋 Welcome to the student portal!")


# Example usage:
student1 = Student("AK")
student1.show()  # Instance method

Student.greet()  # Static method (also accessible via object)
student1.greet()  # But recommended to use via class

Student.change_school("ABC Academy")  # Class method
print("✅ Current School:", Student.school_name)
