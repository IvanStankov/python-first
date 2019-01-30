s1 = {"one", "two", "three", "one"}
s2 = set(["two", "three", "four", "five", "six", "four"])
print(s1)
print(s2)

empty_set = set()
# empty_set = {} - it is not an empty set, it is empty dictionary
print(empty_set)

s3 = s1 | s2  # concat the sets
print(s3)

s4 = s1 & s2  # intersect the sets
print(s4)

s5 = s1 ^ s2  # elements in s1 and s2 but not in both
print(s5)

