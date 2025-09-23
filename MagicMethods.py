class Book:
    def __init__(self, title, author, numPages):
        self.title = title
        self.author = author
        self.numPages = numPages

    def __str__(self): # print something custom instead of the memory address when using print(object)
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other): # Define when the object will be equal to another object of this class
        return self.author == other.author and self.title == other.title
    
    def __lt__(self, other): # Define when the object is smaller than another object of this class
        return True if self.numPages < other.numPages else False
    
    def __gt__(self, other): # Define when the object is greater than another object of this class
        return True if self.numPages > other.numPages else False
    
    def __add__(self, other): # Define how objects of this class add together
        return f"{self.numPages + other.numPages} pages"
    
    def __contains__(self, keyword): # Define what will be searched when using keyword in object 
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key): # Define how indexes would work on an object like object[key]
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "numPages":
            return self.numPages
        else:
            print(f"{key} was not found")

book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry Potter and the Philosopher's stone", "J.K Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S Lewis", 172)
book4 = Book("Harry Potter and the Philosopher's stone", "J.K Rowling", 225)

print(book1)
print(book2 == book4)
print(book3 < book4)
print(book1 > book2)
print(book1 + book2)
print("Lion" in book3)
print(book1["author"])
print(book3[3])