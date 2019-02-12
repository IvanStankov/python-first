import os

file_path = "../../../../resource/new-file.txt"
empty_file_path = "../../../../resource/empty-file.txt"

if os.path.exists(file_path):
    # remove a file
    os.remove(file_path)  # throws an error if the file was not found
if os.path.exists(empty_file_path):
    os.remove(empty_file_path)

with open(file_path, "x") as new_file:
    new_file.write("What is your name?")

# create an empty file
open(empty_file_path, "x")

new_dir = "../../../../resource/new_dir"
os.mkdir(new_dir)
os.rmdir(new_dir)