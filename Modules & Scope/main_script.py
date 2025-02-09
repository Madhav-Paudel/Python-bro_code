# if  __name__==__main__ :(this script can be imported OR run standalone)
#                         function and classes in this module can be reused
#                         without the main block of code executing 








from script1 import *

def main():
    print("this is script1 ")


if __name__=='__main__':
    main()





# if__name__==__main__: (this script can be imported OR run standalone)
# Functions and classes in this module can be reused without the main block of code executing
# Good practice (code is modular,helps readability,leaves no global variables,avoid unintended execution)
#                     Ex. library = import library for functionality
#                     When running library directly, display a help page.
