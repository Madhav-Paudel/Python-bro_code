#   Match-case statement (switch): An alternative to using many 'elif' 
#                                   statements  Execute some code if a value matches a 'case'
#                                   Benefits: cleaner and syntax is more readable
# this is the example by using if and elif
def day_of_weeks(day):
    if day== 1:
        print("It's Sunday")
    elif day==2:
        print("It's Monday")
    elif day==3:
        print("It's Tuesday")
    elif day==4:
        print("It's Wednesday ")
    elif day==5:
        print("It's Thursday")
    elif day==6:
        print("It's Friday")
    elif day==7:
        print("It's Saturday")
    else:
        print("number is invalid")


day_of_weeks(5)
# example of match case 
def day_of_weeks(day):
    match day:
        case 1:
            print("It's Sunday")
        case 2:
            print("It's Monday")
        case 3:
            print("It's Tuesday")
        case 4:
            print("It's Wednesday ")
        case 5:
            print("It's Thursday")
        case 6:
            print("It's Friday")
        case 7:
            print("It's Saturday")
        case _:
            print("number is invalid")


day_of_weeks(7)



def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False

print(is_weekend("Friday"))
