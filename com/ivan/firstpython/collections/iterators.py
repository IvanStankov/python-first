# most container objects can be looped over using a for statement:
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("../../../../resource/test.txt"):
    print(line, end='')

# for statement calls iter() with the container object as a param.
# It internally calls __iter__() on the passed object, which
# should return and object that defines the method __next__()
# which accesses elements in the container one at a time.
# When there are no elements __next__() should raise StopIteration exception