import json
# here we are working with key value pear so it is json file 

file_path="writing1.txt"

employee = {
	"name": "Spongebob",
	"age": 30,
	"job": "cook"
}

try:
	with open(file_path, "w") as file:
		json.dump(employee, file, indent=4)
	print(f"json file '{file_path}' was created")
except FileExistsError:
	print("That file already exists!")