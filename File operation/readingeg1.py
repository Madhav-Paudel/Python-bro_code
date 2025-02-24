# Reading file using python 
import json
import csv

file_path="writing1.txt"

# exception handling for txt 
try:
    with open (file_path,"r") as file:
        content=file.read()
        print(content)

except FileNotFoundError:
    print("Check your file extension")
# exception handling for json file  

try:
    with open (file_path,"r") as file:
        content=json.load(file)
        print(content)

except FileNotFoundError:
    print("Check your file extension")
except json.JSONDecodeError:
    print("File content is not valid JSON")

# exception handling for csv file  

try:
    with open (file_path,"r") as file:
        content=csv.reader(file)
        for line in content:
            print(line)

except FileNotFoundError:
    print("Check your file extension")






