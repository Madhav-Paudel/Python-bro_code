# number pad of phone 
# this is tuple example 
num_pad=((1,2,3),
         (4,5,6),
         (7,8,9),
         ("8",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()