from abc import ABC,abstractmethod
class LibraryItem(ABC):
    def __init__(self,title,item_id,):
        self.title=title
        self.item_id=item_id
     
    @abstractmethod
    def check_out(self):
        pass
    def return_item(self):
        pass
    def display_details(self):
        pass
class Book(LibraryItem):
    def __init__(self, title, item_id,author,genre):
        super().__init__(title, item_id)
        self.author=author
        self.genre=genre
    def check_out(self):
        return f"the book of title {self.title},item id {self.item_id}, author {self.author},and genre {self.genre} has been checked out"
    def return_item(self):
        return f"the book of title {self.title},item id {self.item_id}, author {self.author},and genre {self.genre} has been returned"
    def display_details(self):
        return f"the book of title {self.title} has author {self.author} and genre {self.genre}" 
class DVD(LibraryItem):
    def __init__(self, title, item_id,director,duration):
        super().__init__(title, item_id)
        self.director=director
        self.duration=duration
    def check_out(self):
        return f"the DVD of title {self.title},item id {self.item_id}, director {self.director},and duration {self.duration} minutes has been checked out"
    def return_item(self):
        return f"the DVD of title {self.title},item id {self.item_id}, director {self.director},and duration {self.duration} minutes has been returned"
    def display_details(self):
        return f"the DVD of title {self.title} has director {self.director} and duration {self.duration} minutes" 
b=Book('Tales',201,'Charles','Mystery')
d=DVD('Hangover201',101,'Gillespie',200)
print(b.check_out())
print(b.return_item())
print(b.display_details())
print(d.check_out())
print(d.return_item())
print(d.display_details())

    
        
    



from abc import ABC, abstractmethod
class Book(ABC):
def init__(self, title, quantity, author, price):
self.title = title
self.quantity = quantity
self.author = author
self. price = price
self. discount = None

def set discount(self, discount):
self discount = discount

def get price(self):
if self discount:
return self price* (1-self.____discount)
return self price
@abstractmethod

def repr_(self):
return "Book: (self.title), Quantity: (self.quantity), Author: (self.author), Price: (self.get_price())"

class Novel(Book):
def init__(self, title, quantity, author, price, pages):
super(). init (title, quantity, author, price)
self-pages = pages

def repr (self):
return f"Book: (self.title), Quantity: {self.quantity), Author: {self.author), Price: {self.get_price()}"

class Academic(Book):
def ____init__(self, title, quantity, author, price, branch): super(). init (title, quantity, author, price)
self.branch branch

def repr (self):
return "Book: [self.title), Branch: (self.branch), Quantity: (self.quantity), Author: (self.author), Price:
(self.get price()}"
novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
novel1.set_discount(0.20)
academic1 = Academic("Python Foundations', 12, 'PSF', 655, 'IT')
print(novel1)
print(academic1)
