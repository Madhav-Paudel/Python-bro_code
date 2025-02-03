# *args = allows you to pass multiple non-key arguments
# ** kwargs = allows you to pass multiple keyword-arguments 
#             * unpacking operator
#             1. positional 2. default 3. keyword 4. ARBITRARY


# making a function 
def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print(" ")
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    print(" ")
    # for key in kwargs.keys():
    #     print(key)
    # print(" ")
    # for value in kwargs.values():
    #     print(value)
    # print(" ")
    print("--------------")
    # another approach of printing kwargs and it is used to display different dictionary item into new line 
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('apt')}")
    print(f"{kwargs.get('city')}")
    print(f"{kwargs.get('state')}")
    print(f"{kwargs.get('zip')}")
    print("------------------------------")
    if "apt" in kwargs:
        print(f"{kwargs.get('street')},{kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')},{kwargs.get('pobox')}")
    else:
            print(f"{kwargs.get('street')}")


shipping_label("Mr.","Madhav","P.","Paudel",
               street="howpur",
               apt="200",
               pobox="1010",
               city="bansgadhi",
               state="lumbini",
               zip="456789"
               )