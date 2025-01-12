# dictionary= a collection of {key:value} pairs ordered and changeable. no duplicates 


country={
    "Nepal":"Kathmandu",
    "India":"New Delhi",
    "Bhutan":"Thimpu",
    "Bangladesh":"Dhaka",
}
# print(country.get("India"))

# if country.get("India"):
#     print(f"that capital exist ")
#     print(country.get("India"))
# else:
#     print("that capital does not exist")
# ----- updating the dictionary------

# country.update({"Pakistan":"Islamabad"})
# print(country,end="\n")
# print("---------------")
# # removing the item form the dictionary 
# country.pop("Nepal")
# print(country)
# print("-----")
# # removing the latest added item form the dictionary 
# country.popitem()
# print(country)
# print("____-")
# for clearing the dictionary   
# # country.clear()
# print(country)
# # for getting key only 
# print(country.keys())
# for key in country.keys():
#     print(key)
# # for getting value in the dictionary
# print(country.values())
# for value in country.values():
#     print(value)
# using items() for printing the key and value at the same time printing as 2d list
for key,value in country.items():
    print(f"{key}:{value}")
    