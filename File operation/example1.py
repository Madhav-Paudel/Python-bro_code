# Python file detection 
import os

file_path = r"c:\Users\Acer\OneDrive\Desktop\broCode\File operation\eg1.txt"


if os.path.isfile(file_path):  
    print(f"Found the file '{file_path}'")
    if os.path.isfile(file_path):
        print("This is file ")
    elif os.path.isdir(file_path):
        print("This is a folder")

else:
    print("File not found")

