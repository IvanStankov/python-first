try:
    raise Exception
except:
    print("Handled an exception")
finally:
    print("Inside finally")

# else is executed before finally
try:
    n = ""
except:
    print("Except")
else:
    print("1 - Else")
finally:
    print("2 - Finally")