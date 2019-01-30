# x = input("How old are you?\n")
x = "26"

if int(x) >= 18:
    print("Old enough")
elif int(x) > 3:
    print("You are young")
else:
    print("Infant")

i = 0
while i < 10:
    print(i)
    i = i + 1

y = 10
while y > 20:
    print("Y is greater than 20")
else:
    print("Y is " + str(y))

for i in range(10):
    print(i ** 2)

for i in range(0, 20, 4):
    print(i)