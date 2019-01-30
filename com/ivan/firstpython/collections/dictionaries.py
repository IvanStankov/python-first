d1 = {1: "one", 2: "two"}
print(d1)
d2 = {"one": 1, "two": 2, "three": 3}
print(d2)
d3 = {}  # creates an empty dictionary
print(d3)
d4 = dict([("ten", 10), ("nine", 9)])
print(d4)
d5 = {x: x ** 2 for x in range(10) if x > 1}
print(d5)

print(d2["two"])

del d2["three"]  # throws KeyError if the key is not found
print(d2)
print("one" in d2)
print(list(d2))

for k, v in d5.items():
    print("Square of %s is %s" % (k, v))

for k in d5.keys():
    print(k, end="")
print()

print("Contains: " + str(3 in d5))
