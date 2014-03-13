'''
Helping students study for the midterm

author: @abekim
'''
from sets import Set
# sum of multiples
def sum_mults(n):
    ''' return the sum of all multiples of 3 and 5 less than n '''
    all_mults=[]
    i=1
    j=1
    mult3=0
    mult5=0
    while mult3<n:
        mult3=3*i
        if mult3<n:
            all_mults.append(mult3)
        i +=1
    while mult5<n:
        mult5=5*j
        if mult5<n:
            all_mults.append(mult5)
        j +=1    
    no_repeats=list(Set(all_mults))
    return sum(no_repeats)

# flatten
def flatten(li):
    ''' flattens li by one layer '''
    Flattened=[]
    for item in li:
        if type(item)==list:
            for subitem in item:
                Flattened.append(subitem)
        else:
            Flattened.append(item)
    return Flattened
    

# ROTn
def rotate_word(s, n):
    ''' rotates the word s by n using ROTn encryption method '''
    numerical=[]
    translated=""
    for char in s:
        number=ord(char)+n
        if number >122:
            number += -26
        if number<97:
            number += 26
        numerical.append(chr(number))
    for code in numerical:
        translated += code
    return translated
    
# Bank Account object
class BankAccount:
    ''' A Simple Bank Account '''
    def __init__(self, balance=0.):
        ''' construct a bank account object with beginning balance '''
        self.balance=balance
        
    def get_balance(self):
        ''' return the current balance '''
        return self.balance

    def withdraw(self, amount):
        ''' withdraw amount and return new balance '''
        self.balance -= amount
        return  self.balance

    def deposit(self, amount):
        ''' deposit certain amount and return new balance '''
        self.balance+= amount
        return self.balance

# Book
class Book:
    def __init__(self, title, author, length, published):
        ''' construct a book object with given properties '''
        self.title=title
        self.author=author
        self.length=length
        self.published=published

    def __repr__(self):
        return "%s" % self.title
        
# Collection of Books
class Collection:
    def __init__(self, books=[]):
        self.books = books
    
    def filter_by_published(self, year):
        ''' return all books in collection published in year '''
        Published=[]
        for book in self.books:
            if book.published==year:
                Published.append(book)
        return Published
        
    def filter_by_author(self, author):
        ''' return all books in collection by author '''
        Authored=[]
        for book in self.books:
            if book.author==author:
                Authored.append(book)
        return Authored
        
    def filter_by_title(self, char):
        ''' returns all books in collection whose title starts with char '''
        Titles=[]
        for book in self.books:
            if book.title[0]==char:
                Titles.append(book)
        return Titles

if __name__ == '__main__':
    books = [
        Book('Kavalier & Clay', 'Michael Chabon', 400, 2000),
        Book('1984', 'George Orwell', 100, 1984), 
        Book('Bible', 'No one knows', 10000, -2000),
        Book('Animal Farm', 'George Orwell', 200, 2000),
        Book('Abe\'s Book', 'Abe Kim', 50, 1984)
    ]
    
    col = Collection(books)
     
    