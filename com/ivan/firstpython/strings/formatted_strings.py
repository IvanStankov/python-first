name = "John"
age = 54
phrase = f"Hello, my name is {name}. I am {age + 3} old."
print(phrase)

phrase = "Age is {:} - Name is {:}".format(age, name)
print(phrase)

phrase = "first - {1}; zeroth - {0}".format(0, 1)
print(phrase)

d1 = {'name': "John", 'age': 43}
phrase = "Age is {0[age]} - Name is {0[name]:10}".format(d1)
print(phrase)

phrase = "Age is {name} - Name is {age}".format(name="John", age=23)
print(phrase)
