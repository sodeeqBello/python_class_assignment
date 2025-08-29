'''Assignment 1: Create a class named 'Book' with attributes like title, author, year, 
   pages, price, publisher, and language. Include a method to display book information.
   Then, create a subclass named 'EBook' that inherits from 'Book' and adds attributes like 
   file_size and format. Include a method to display ebook information.'''

# Parent Class
class Book:
    # Constructor
    def __init__(self, title, author, year, pages, price, publisher, language):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.price = price
        self.publisher = publisher
        self.language = language

    # Method to display book information
    def get_info(self):
        print(
            f"📖 '{self.title}' by {self.author} ({self.year})\n"
            f"- Pages: {self.pages}\n"
            f"- Price: ${self.price}\n"
            f"- Publisher: {self.publisher}\n"
            f"- Language: {self.language}\n"
        )

# Child Class
class EBook(Book):
    # Constructor
    def __init__(self, book, file_size, format):
        super().__init__(
            book.title, book.author, book.year, book.pages,
            book.price, book.publisher, book.language
        )
        self.file_size = file_size
        self.format = format

    # Method to display ebook information
    def get_ebook_info(self):
        print(
            f"💻 eBook Version of '{self.title}'\n"
            f"- Format: {self.format}\n"
            f"- File Size: {self.file_size} MB\n"
        )

print("This program shows how a Book class holds basic details, while an EBook subclass extends it with file size and format.\n")

# Creating an instance of Book
book1 = Book("Think and Grow Rich", "Napoleon Hill", 1937, 238, 15.99, "The Ralston Society", "English")
book1.get_info()

book2 = Book("The Alchemist", "Paulo Coelho", 1988, 208, 10.99, "HarperTorch", "English")
book2.get_info()

# Creating an instance of EBook (from book1)
ebook1 = EBook(book1, 2, "PDF")
ebook1.get_ebook_info()

ebook2 = EBook(book2, 1.5, "ePub")
ebook2.get_ebook_info()

'''Assignment 2: Create a parent class named 'Vehicle' with a method named 'move' that
   returns a string indicating how the vehicle moves. Then, create child classes named
    'Car', 'Plane', 'Boat', and 'Train' that inherit from 'Vehicle' and override the
    'move' method to provide specific movement descriptions for each vehicle type.'''

# Activity 2: Polymorphism Challenge (with Inheritance)
# Parent Class
class Vehicle:
    def move(self):
        return "This vehicle moves in some way."

# Child Classes
class Car(Vehicle):
    def move(self):
        return "Driving! 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying! ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing! ⛵"

class Train(Vehicle):
    def move(self):
        return "Choo Choo! 🚆"

# Polymorphism in action
vehicles = [Car(), Plane(), Boat(), Train()]

print("This program demonstrates polymorphism using a parent class 'Vehicle' and child classes 'Car', \n" \
"'Plane', 'Boat', and 'Train', each overriding the 'move' method to show different ways vehicles can move.\n")


for v in vehicles:
    print(v.move())
