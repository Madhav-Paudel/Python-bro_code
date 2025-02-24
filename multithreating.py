# multithreading= Used to perform multiple tasks concurrently (multitasking)
#                Good for I/0 bound tasks like reading files or fetching data from APIs
#                threading. Thread(target=my_function)
import threading
import time


def walk_dog(first,last):
    time.sleep(8)
    print(f"You finish Walking {first} {last}")

def you_out_trash():
    time.sleep(2)
    print("You take out the trash!")

def get_mail():
    time.sleep(4)
    print("You get the mail")

# # it take 8 second 
# walk_dog()
# # it take 2 second 
# you_out_trash()
# #it take 4 second
# get_mail()

# here the all the task are doing at the same time same as pipelining but the task which take less time is done at the first 

chore1=threading.Thread(target=walk_dog,args=("scooby","doo"))
chore1.start()

chore2=threading.Thread(target=you_out_trash)
chore2.start()

chore3=threading.Thread(target=get_mail)
chore3.start()
# here join method is collectively joining all the task after that the task of printing will be done 

chore1.join()
chore2.join()
chore3.join()


print("All task are done")
