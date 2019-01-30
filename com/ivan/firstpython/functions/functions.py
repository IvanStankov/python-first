def fun1():
    print("Simle function")
fun1()

def fun2(arg1):
    print("Simple function with argument %s" % arg1)
fun2("123")

# function can have default parameters
def fun3(arg1, defArg1 = 11, defArg2 = "Hello"):
    print("Args: %s, %s, %s" % (arg1, defArg1, defArg2))
fun3("arg1", defArg2 = "defArg2", defArg1 = 33)

# function with arbitrary arguments
def fun4(arg1, *other_args):
    print(arg1, end="")
    for i in other_args:
        print(i, end="")
    print()
fun4(1, 2, 3, 6666)

# function with arbitrary named parameters
def fun5(**dict):
    for key in dict:
        print("%s:%s" % (key, dict[key]))
fun5(one="1", two="2", three=3)

def fun6(a, b):
    print("%s and %s" % (a, b))
params = [3, 6]
fun6(*params)  # unpacking argument list

def fun7():
    print("Function with return type")
fun7()