class Base1():
    def do1(self):
        print("do1() Base1 class")

    def do2(self):
        print("do2() Base1 class")


class Base2():
    def do1(self):
        print("do1() Base2 class")

    def do2(self):
        print("do2() Base2 class")


class DerivedClass(Base1, Base2):
    def do1(self):
        print("do1() Base3 class")


dc = DerivedClass()
dc.do1()
dc.do2()  # will be invoked from the first class that have the function with the name
