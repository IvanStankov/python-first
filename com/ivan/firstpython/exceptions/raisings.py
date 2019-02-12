# to throw an exception raise statement is used
try:
    raise Exception("Ooops")
except Exception as e:
    print(e.args[0])

# catch-and-rethrow
try:
    try:
        raise Exception("Smth went wrong")
    except Exception as e:
        print(e)
        raise
except:
    print("")