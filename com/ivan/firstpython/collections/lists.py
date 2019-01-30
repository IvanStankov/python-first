from math import pi

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[:3])  # sublist till the 3 element exclusive
print(nums[2:])  # sublist from the 2 element inclusive
print(nums[2:5])  # sublist from 2-5 elements
print(nums[-1])  # the last element
print(nums[:])  # returns a shallow copy of the list

concat_list = [1, 2, 3] + [4, 5, 6]
print(concat_list)

print(len(concat_list))  # length of the list

list1 = [1, 2]
list1.append(3)  # appends an element to the list
list1.insert(1, 8)  # isnerts elements into the given position and moves element to the right
print(list1)

print("Remove element")
list1.remove(8)  # removes the first element of the list which is equal to given
list1.extend([9, 10])  # appends all elements from the given list to the end of the current list
list1[3] = 35  # set an element to the given position
print(list1)

print(list1.pop())  # remove the item at the end of the list and return it
print(list1.pop(2))  # remove the item at the given position and return it
print(list1)
list1.clear()

list1 = [9, 8, 7, 6, 5, 4]
print(list1.index(6))  # return the index of the first element which is equal to given
# print(list1.index(61)) - throws ValueError if there is no such element

print("Sorting...")
list1.sort()
print(list1)

print(list1.copy())  # creates a shallow copy of the list, equivalent to list1[:]
print(list1.count(5))

list1 = [x ** 2 for x in range(10)]  # creates a list of square numbers from 0 - 9 inclusive
print(list1)
list1  = list(map(lambda x: x ** 2, range(10)))  # creates the same list
print(list1)

list2 = [round(pi, i) for i in range(10)]
print(list2)
del list2[3]  # remove element with index 3 from the list
print(list2)
del list2[1:7]  # remove from 1 to 7 indexes
print(list2)

print("list unpacking")
a, b, c = list2
print("a = %s; b = %s; c = %s" % (a, b, c))

for i, v in enumerate(list2):
    print("%s. %s" % (i, v))

