# writing in file in python 
txt_data1=input("enter any thing you want to take a note\n")
txt_data=["hello","madhav","paudel"]


file_path="writing.txt"
# here w mean write and if the file is not already exits it will create one 
# here with open and close the file as the work is done 
# The main operation uses a with statement, which is the
# recommended way to handle files in Python because it automatically
# closes the file when we're done:
# Here,

# . The te] file_path specifying where to create/write the file
# . The mode "w" which means write mode. This will:
# o Create a new file if it doesn't exist
# o Overwrite the file if it already exists

# Note: There's a small error in the comments. It mentions "x"
# the code actually uses
# new file but raises an error if the file already exists.

# [e] open()

# takes two parameters:

# mode. The "x"  mode, but
# x mode is different - it creates a
try:
    with open(file_path,"w") as file:
        for empolyee in txt_data:
            file.write(empolyee+"\n")
        print("file path was created\n")
        
except FileExistsError:
    print("file already exist")