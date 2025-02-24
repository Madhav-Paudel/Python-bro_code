import csv 
# here we are working with comma separated value pair so it is csv file 

file_path="writing1.csv"

employee = [["Name","Age","Job"],
			["Michael",25,"CEO"],
			["Tek",25,"Dr"],
			["John",26,"Software Dev"]]

try:
	with open(file_path, "w",newline="") as file:
		writer=csv.writer(file)
		for row in employee:
			writer.writerow(row)
	print(f"csv file '{file_path}' was created")
except FileExistsError:
	print("That file already exists!")