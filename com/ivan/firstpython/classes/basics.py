class Student:
    age = 18  # class variable shared by all instances
    # constructor
    def __init__(self, name):
        self.__name = name
        self.age = 12  # class attributes can be referenced via self

    def get_name(self):
        return self.__name

    def get_upper_name(self):
        return self.get_name().upper()  # methods can invoke other class methods

student1 = Student("John")
# student1.__name - results in AttributeError because the actual name will be "_Student__name"
print(student1.get_name())
print(student1.get_upper_name())
print(student1)  # default String representation
print(student1.age)
print("Class variable:", Student.age)

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __str__(self): # custom String representation
        return "Car[model - %s; year - %s" % (self.model, self.year)

jetta = Car("VW Jetta", 1991)
print(jetta)

jetta.seats = 5  # fields can be added "on the fly"
print("Seats in Jetta:", jetta.seats)