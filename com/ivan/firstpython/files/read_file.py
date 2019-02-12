f1 = open("../../../../resource/test.txt", "r")
print(f1.readline())
f1.close()

# automatically closes the file after leaving with section
with open("../../../../resource/test.txt", "r") as text_file:
    for line in text_file.readlines():
        print(line, end="")
print(text_file.closed)  # file is already closed
