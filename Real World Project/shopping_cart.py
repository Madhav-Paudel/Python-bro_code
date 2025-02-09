# project shopping cart 
import random
#  maskpass function is used hide pasword
import maskpass  
carts=[]
Total=0
# --------- this loop is run until the number of any number of list is selected 
while True:
    select_nmbr = input("Enter the number to select the store for shopping:\n 1. Amazon Store\n 2. Daraz Store\n 3. P Mart\n ")

# ---------
    if select_nmbr == "1":
        print("\n😊 Welcome to Amazon Store 😎\n")
        break
    elif select_nmbr == "2":
        print("\n😊 Welcome to Daraz Store 😎\n")
        break
    elif select_nmbr == "3":
        print("\n😊 Welcome to P Mart 😎\n")
        break
    else:
            print("Invalid Number! Please enter 1, 2, or 3.")

# dictionary for displaying the category
def selecting_items():
    my_dictionary={"FASHION":1,
                "ELECTRONICS":2,
                "Home Goods":3,
                "Beauty & Personal Care":4,
                "Sports & Outdoors":5,
                }
    print("--------🛒 Item Category 🛒--------")
    for keys,values in my_dictionary.items():
        print(f"{keys:27}: {values}")
    print("-----------------------------------")

    # for  displaying fashion section 

dictionary_Fashion={
                    "blouses ":60,
                    "shorts ":40,
                    "pants ":65,
                    "jackets ":99,
                    "sneakers ":69,
                    "sandal ":60,
                    "heels ":69,
                    "boots ":89,
                    "scarf ":99,
                    "t-shirts ":50,
                    }
# function 1
def display_fashion():
    print("--------🛒 Fashion Item 🛒--------")
    for keys,values in dictionary_Fashion.items():
        print(f"{keys:25}: {values}")

    print("-----------------------------------")
# -----------------
# for displaying electronic section
dictionary_Electronic={
                     "mobile ":1000,
                    "laptop ":1500,
                    "headphone ":40,
                    "smartwatch ":250,
                    "camera ":599,
                    "t.v ":699,
                    }
def display_electronic():
    print("------🛒 Electronic Item 🛒--------")
    for keys,values in dictionary_Electronic.items():
        print(f"{keys:25}: {values}")
    print("-----------------------------------")
# ----------------------------------
# for displaying home goods 
dictionary_Home_goods={
                "sofas ":450,
                "chairs ":201,
                "spoon Set ":150,
                "pots ":120,
                "pans ":150,
                "utensils ":201,
                "towels ":102,
                "art ":209,
                "shower ":201,
                "lamps ":499,
                }
# function of home goods 
def display_home_good():
    print("------🛒 Home Goods Item 🛒--------")
    for keys,values in dictionary_Home_goods.items():
        print(f"{keys:25}: {values}")
    print("-----------------------------------")
# ------------------------------------
# for displaying Beauty and personal care product 
dictionary_Beauty={
                  "lipstick ":129,
                  "eyeshadow ":42,
                  "foundation ":78,
                  "moisturizer ":58,
                  "serums ":45,
                  "shampoo ":99,
                  "conditioner ":28,
                  "perfume ":40,
                  "toothpaste ":41,
}
# function of beauty 
def display_Beauty():
    print("------🛒 Beauty Item 🛒--------")
    for keys,values in dictionary_Beauty.items():
        print(f"{keys:25}: {values}")
    print("-----------------------------------")
# ---------------------------
# for displaying sports and outdoors
dictionary_sports={
                 "running shoes":25,
                 "ATHLETIC WEAR":45,
                 "BASKETBALL   ":78,
                 "TENNIS RACKET ":41,
                 "SOCCER BALL ":78,
                 "TENT    ":47,
                 "LANTERN ":98,
                 "SLEEPING BAG ":78,
}
def display__sports():
    print("------🛒 Sports Item 🛒--------")
    for keys,values in dictionary_sports.items():
        print(f"{keys:25}: {values}")
    print("-----------------------------------")
# -------------------------
while True:
    selecting_items()
    value=input("enter number for selecting category (q for quit)\n").lower()
    if value.lower()=="q":
        break
    if value=="1":
        # this function displaying the fashion items 
        display_fashion()
        Name_prod=input("\nEnter the name of product and give space\n").lower()
        # this is checking if the enter production is in dictionary or not  
        if Name_prod in dictionary_Fashion:
            carts.append((Name_prod, dictionary_Fashion[Name_prod]))
            print(f"{Name_prod} Added Item to cart ${dictionary_Fashion[Name_prod]}")
            Total+=dictionary_Fashion[Name_prod]
        else:
            print(f"\n{Name_prod} is not in list or check spelling of product ❌\n")
    elif value=="2":
        display_electronic()
        Name_prod=input("\nEnter the name of product and give Space\n").lower()
        # this is checking if the enter production is in dictionary or not  
        if Name_prod in dictionary_Electronic:
            carts.append((Name_prod,dictionary_Electronic[Name_prod]))
            print(f"{Name_prod} Added Item to cart ${dictionary_Electronic[Name_prod]}")
            Total+=dictionary_Electronic[Name_prod]
        else:
            print(f"\n{Name_prod} is not in list or check spelling of product ❌\n")
    elif value=="3":
        display_home_good()
        Name_prod=input("\nEnter the name of product and give Space\n").lower()
        # this is checking if the enter production is in dictionary or not  
        if Name_prod in dictionary_Home_goods:
            carts.append((Name_prod,dictionary_Home_goods[Name_prod]))
            print(f"{Name_prod} Added Item to cart ${dictionary_Home_goods[Name_prod]}")
            Total+=dictionary_Home_goods[Name_prod]
        else:
            print(f"\n{Name_prod} is not in list or check spelling of product ❌\n")
    elif value=="4":
        display_Beauty()
        Name_prod=input("\nEnter the name of product and give Space\n").lower()
        # this is checking if the enter production is in dictionary or not  
        if Name_prod in dictionary_Beauty:
            carts.append((Name_prod,dictionary_Beauty[Name_prod]))
            print(f"{Name_prod} Added Item to cart ${dictionary_Beauty[Name_prod]}")
            Total+=dictionary_Beauty[Name_prod]
        else:
            print(f"\n{Name_prod} is not in list or check spelling of product ❌\n")
    elif value=="5":
        display__sports()
        Name_prod=input("\nEnter the name of product and give Space\n").lower()
        # this is checking if the enter production is in dictionary or not  
        if Name_prod in dictionary_sports:
            carts.append((Name_prod,dictionary_sports[Name_prod]))
            print(f"{Name_prod} Added Item to cart ${dictionary_sports[Name_prod]}")
            Total+=dictionary_sports[Name_prod]
        else:
            print(f"\n{Name_prod} is not in list or check spelling of product ❌\n")
    else:
        print("Invalid error")

# converting list in dictionary by using list comprehension 
final = [(name, price) for name, price in carts]
print("---------bill------------")
print("Item                   price")
for keys,value in final:
    print(f"{keys:25}:${value}")

print(f"total price ${Total:15}")
print("--------------------------")
print()
# payment method ko lagi 
while True:
    value1=input("Choose number for payment\n 1.Online Payment\n2.Card\n")
    # chooing two method 
    if value1=="1":
        string=input("Enter number for online payment\n1.Bitcoin\n2.PayPal")
        # this for crypto 
        if string=="1":
            print("Sent Bitcoin in following wallet address\n Make Sure Your Network Must Be SEGWITBTC BTC(SegWit)\n")
            print("bc1qzddsuzch3t3jw5vd08wfqglvu6hmhpdyyrcv72")
            rand_num=random.randint(1,10)
            if rand_num<=5:
                print("Payment Received 😊")
                break
            else:
                print("Payment Unsuccessful 😔 ")
        # this is for online 
        elif string=="2":
            print("\nEnter your PayPal Information\n")
            username=input("\nEnter username\n")
            password=maskpass.askpass("\nEnter you pass here\n")
            # this is for only testing
            print(password)
            rand_num=random.randint(1,10)
            if rand_num<=5:
                print("\nPayment Received 😊\n")
                break
            else:
                print("\nPayment Unsuccessful 😔\n")
        else:
            print("Invalid ❌ Error\n")
    elif value1=="2":
        username=input("\nEnter username\n")
        password=maskpass.askpass("\nEnter you pass here\n")
        # this is for only testing
        print(password)
        rand_num=random.randint(1,10)
        if rand_num<=5:
            print("\nPayment Received 😊\n")
            break
        else:
            print("\nPayment Unsuccessful 😔\n")

if select_nmbr == "1":
    print("\n😊 Thank you For Choosing Amazon Store 😎\n")
    
elif select_nmbr == "2":
    print("\n😊 Thank you For Choosing Welcome to Daraz Store 😎\n")
    
elif select_nmbr == "3":
    print("\n😊 Thank you For Choosing P Mart 😎\n")

    

