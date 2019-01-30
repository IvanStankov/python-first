t = 12, 4, "Hello"
print(t)
# t[1] = 5 - throws TypeError: 'tuple' object does not support item assignment

empty_tuple = ()
print(empty_tuple)
tuple_with_one_elem = 1,  # (1) will not be a tuple
print(tuple_with_one_elem)

a, b, c = t  # tuple unpacking
print(a)
print(b)
print(c)