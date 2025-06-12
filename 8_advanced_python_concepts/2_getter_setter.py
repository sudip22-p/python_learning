class Student:
    def __init__(self, name):
        # Initialize student name and protected marks attribute
        self.name = name
        self._marks = 0  # The underscore means "protected" (shouldn't access directly)

    @property
    def marks(self):
        """
        Getter method:
        Called when you access student.marks
        Returns the current marks.
        """
        return self._marks

    @marks.setter
    def marks(self, value):
        """
        Setter method:
        Called when you assign to student.marks
        Validates marks must be between 0 and 100.
        """
        if 0 <= value <= 100:
            self._marks = value
            print("✅ Marks updated successfully.")
        else:
            print("❌ Error: Marks must be between 0 and 100.")


# --------- Usage Example ---------

# Create a student instance
student1 = Student("Sud")

# Set marks using the setter
student1.marks = 85  # Internally calls the marks.setter method
# Output: ✅ Marks updated successfully.

# Get marks using the getter
print(f"{student1.name}'s marks: {student1.marks}")  # Calls marks getter
# Output: Sud's marks: 85

# Try setting invalid marks
student1.marks = 150
# Output: ❌ Error: Marks must be between 0 and 100.
