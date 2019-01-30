str1 = "It is string with 'double' \" quotes"
str2 = 'It is string with "single" \' quotes'
print(str1 + " " + str2)

multiline1 = """First line
Second line"""
print(multiline1)

multiline2 = '''First line
Second line'''
print(multiline2)

multiline3 = """First line\
 And this is still the first line"""
print(multiline3)

phrase = "You shall not pass!"
print(phrase[-1])  # the last symbol in the string
print(phrase[:3])  # substring form the start to the 3 symbol exclusive
print(phrase[4:])  # substring form the 5 symbol to the end
print(phrase[10:14])  # substring from 10 to 14 symbols

print(len(phrase)) # length of the string

print("Hi! " * 3) # prints 'Hi! Hi! Hi! '
