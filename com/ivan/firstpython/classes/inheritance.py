class Vehicle:
    def __init__(self, year):
        print("Parent constructor called")
        self.year = year

    def f0(self):
        self.f1()

    def f1(self):
        print("F1 of Vehicle")

    def f2(self):
        print("F2 of Vehicle")

class Car(Vehicle):
    def __init__(self, year):
        super(Car, self).__init__(year)
        print("Child constructor called")
        pass

    def f1(self):
        print("F1 of Car")

    def f2(self):
        Vehicle.f2(self)
        print("F2 of Car")

car = Car(12)
print(car.year)

print("Is a Car instance of Vehicle?", "Yes" if isinstance(car, Vehicle) else "No")
print("Is Car subclass of Vehicle?", issubclass(Car, Vehicle))
print("Is Vehicle subclass of Car?", issubclass(Vehicle, Car))

print("Calling car.f0(): ", end="")
car.f0()

print("Calling car.f1() which is overriden")
car.f1()

print("Calling car.f2() which is overriden but invokes overriden function inside")
car.f2()