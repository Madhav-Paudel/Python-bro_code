# exception = An event that interrupts the flow of a program
#            (ZeroDivisionError, TypeError, ValueError)
#            1.try, 2.except, 3.finally

# try:
    # try some code here
# except Exception:
    # handel an exception 
# finally:
    #   do some clean here 
try:
    number=int(input("Enter a number"))
    print(1/number)
except ZeroDivisionError:
    print("You cannot divide by zero you idiot !")

except ValueError as e:
    print(f"{e} value can't divide")

except TypeError:
    print("Type error !")

except Exception:
    print("Something went wrong!")

# except exception is wrong practice to use at the first place it is always to tell user what went wrong
 
finally:
    print("hello world")

# here finally block will executed at last as after executing the all other block 



