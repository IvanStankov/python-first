class Student:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

student1 = Student("John")
# student1.__name - result in AttributeError

print(student1.get_name())
print(student1) # default String representation

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __str__(self): # custom String representation
        return "Car[model - %s; year - %s" % (self.model, self.year)

jetta = Car("VW Jetta", 1991)
print(jetta)