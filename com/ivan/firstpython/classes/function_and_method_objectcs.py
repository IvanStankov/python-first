class Printer:
    def printMsg(self, msg):
        print(msg)

pr = Printer()

fun = pr.printMsg  # method object
fun.__func__(pr, "1 - Hello")  # __func__ is the function object corresponding to the method
fun("2 - Hello")
fun(pr == fun.__self__)  # __self__ is the instance object with the method 

pr1 = Printer.printMsg  # function object
pr1(pr, "3 - Hi")