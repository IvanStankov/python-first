x = [1, 3, 5]

try:
    x[4]
except IndexError:
    print("Uh oh, Index error")

# several exception can be caught in one block
try:
    x[4]
except (IndexError, TypeError):
    print("Several exceptions catch block")

# there could be several catch blocks
try:
    x[4]
except IndexError:
    print("Index error")
except TypeError:
    print("Type error")

# the last catch block can omit exception declaration
try:
    x[4]
except:
    print("All exceptions catch")

# instance of the exception can be assigned
try:
    x[6]
except IndexError as e:
    print("Wrong index '%s' of an array" % e)

# try clause can have else block which is invoked when no exceptions happened
try:
    x[1]
except IndexError as e:
    print(e)
else:
    print("There was no any exceptions!")

# empty catch block
try:
    x[7]
except:
    pass