import re
class Author():
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name





class Book():
    ISBN_runner = 1

    def __init__(self, Author, Title, Subject, DDS):
        self._ISBN = Book.ISBN_runner
        self._Author = Author
        self._Title = Title
        self._Subject = Subject
        self._DDS = self.checkDDS(DDS)

        Book.ISBN_runner += 1

    def checkDDS(self,value):
        if len(str(value)) != 3:
            print("DDS must be a number and only have 3 digit")
        else:
            self._DDS = value

    @property
    def ISBN(self):
        return self._ISBN

    @property
    def Author(self):
        list_writter = self._Author
        list_str = []
        for writter in list_writter:
            list_str.append(writter.name)
        return list_str

    @property
    def Title(self):
        return self._Title
    

    @property
    def Subject(self):
        return self._Subject
    
    @property
    def DDS(self):
        return self._DDS
    @DDS.setter
    def DDS(self, value):
        self.checkDDS(value)


class Catalog():
    def __init__(self):
        self.Books = []

    def add_book(self, Book):
        self.Books.append(Book)

    def del_book(self):
        Chosen_book = int(input("Insert ISBN number : "))
        for item in self.Books:
            if item.ISBN == Chosen_book:
                self.Books.remove(item)
                print("Book removed")

    def print_book(self, book):

        print(f"{book.ISBN}, {book.Author}, {book.Title}, {book.Subject}, {book.DDS}")

    def search_book(self):
        print("---")
        by = int(
            input(f"Search By : \n 1.ISBN \n 2.Author \n 3.Title \n 4.Subject \n 5.DDS \nPlease select number : "))
        if by == 1:
            ISBN_select = int(input("Insert ISBN number : "))
            counter = 1
            for book in self.Books:
                if ISBN_select == book.ISBN:
                    self.print_book(book)
                    break
                else:
                    counter += 1
                    if counter == len(self.Books):
                        print("Book not found")
        elif by == 2:
            Author_select = input("Insert Author : ")
            counter = 1
            for book in self.Books:
                if Author_select in book.Author:
                    self.print_book(book)
                else:
                    counter += 1
                    if counter == len(self.Books):
                        print("Book not found")
        elif by == 3:
            Title_select = input("Insert Title : ")
            counter = 1
            for book in self.Books:
                if Title_select in book.Title:
                    self.print_book(book)
                    break
                else:
                    counter += 1
                    if counter == len(self.Books):
                        print("Book not found")

        elif by == 4:
            Subject_select = input("Insert Subject : ")
            counter = 1
            for book in self.Books:
                if Subject_select in book.Subject:
                    self.print_book(book)
                else:
                    counter += 1
                    if counter == len(self.Books):
                        print("Book not found")
        elif by == 5:
            DDS_select = int(input("Insert DDS : "))
            counter = 1
            for book in self.Books:
                if DDS_select == book.DDS:
                    self.print_book(book)
                else:
                    counter += 1
                    if counter == len(self.Books):
                        print("Book not found")

    def add_book_to_catalog(self):
        global Author
        global Book
        Author_list = []
        while True:
            name = input("Insert Author name : ")
            if name == "":
                break
            else:
                Authorname = Author(name)
                Author_list.append(Authorname)
        Title = input("Insert Title : ")
        Subject = input("Insert Subject : ")
        DDS = int(input("Insert DDS : "))
        Book = Book(Author_list, Title, Subject, DDS)
        self.Books.append(Book)


Author1 = Author("A")
Author2 = Author("B")
BookA = Book([Author1, Author2], "Abook1", "Language", 400)
BookB = Book([Author2], "Abook2", "Language", 400)
libraryA = Catalog()
libraryA.add_book(BookA)
libraryA.add_book(BookB)
libraryA.add_book_to_catalog()
libraryA.search_book()
