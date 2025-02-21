# Magic methods = Double underscore methods (double underscore) _init_, _str_, _eq_
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:
    def __init__(self,title,author,no_page):
        self.title=title
        self.author=author
        self.no_page=no_page
        # here str is used for declaring the string function 
    def __str__(self):
        return f"'{self.title}' by {self.author} it contain {self.no_page} number"
    # here __eq__ is used for the declaring the equal than symbol 
    def __eq__(self, other):
        return self.title==other.title and self.author == other.author
    # here __lt__ is used for the declaring the less than function 
    def __lt__(self,other):
        return self.no_page<other.no_page
    
    # here __lt__ is used for the declaring the greater than function 

    def __gt__(self,other):
        return self.no_page>other.no_page
    # adding function
    def __add__(self,other):
        return self.no_page+other.no_page
    # for searching the keyword 
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    # for getting the title of the book 
    def __getitem__(self,key):
        if key=='title':
            return self.title
        elif key=='author':
            return self.author
        elif key=='no_page':
            return self.no_page
        else:
            return f"key {key} not found "
        
book1=Book("i am alone","M.p petrol",212)
book2=Book("small sky","gp",412)
book3=Book("i am alone","M.p petrol",212)

print(book1)

print(book2)

print(book1==book2)

print(book1==book3)

print(f"does the '{book1.title}' has less page then '{book2.title}' - {book1<book2}")

print(f"does the '{book1.title}' has more page then '{book2.title}' - {book1>book2}")

print(f"the total no of page are {book1+book2}")

print("alone" in book1)

print(book1['title'])
print(book1['author'])
print(book1['no_page'])


print(book2['title'])
print(book2['author'])
print(book2['no_page'])

print(book3['title'])
print(book3['author'])
print(book3['no_page'])


print(book1['audio'])







                          
        