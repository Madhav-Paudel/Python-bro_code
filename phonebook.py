import csv


file=open("phonebook.csv","a")

name=input("Name:")
number=input("Number:")


writer=csv.writer(file)


writer.writerow([name,number])

file.close()