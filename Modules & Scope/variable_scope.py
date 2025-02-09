# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
# --- x is local version to specific function 
def fun1():
    a=1
    print(a)

def fun2():
    b=2
    print(b)

fun1()
fun2()
#  here a and b are local variable to specific function 


# we are giving the value of x as global variable 
x=15
def fun1():
    print(x)

def fun2():
    print(x)

#  function calling 
fun1()
fun2()

def fun1():
    a=10
    def fun2():
        print(a)
    fun2()

fun1()
