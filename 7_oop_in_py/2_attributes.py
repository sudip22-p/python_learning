# ✅ Constructors, Instance and Class Attributes


class Car:
    wheels = 4  # class attribute (shared by all)

    def __init__(self, brand):
        self.brand = brand  # instance attribute (unique per object)


car1 = Car("Toyota")
car2 = Car("Tesla")

print(car1.brand, car1.wheels)  # Toyota 4
print(car2.brand, car2.wheels)  # Tesla 4
