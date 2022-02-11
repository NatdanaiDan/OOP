class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class Book:

    def __init__(self, ISBN, Author, Title, Subject, DDS):
        self._ISBN = ISBN
        self._Author = self.checkAuthor(Author)
        self._Title = Title
        self._Subject = Subject
        self._DDS = self.checkDDS(DDS)

    def checkAuthor(self, value):
        if isinstance(value, list):
            return value
        else:
            print("Author must be a list")

    def checkDDS(self, value):
        if len(str(value)) != 3:
            print("DDS must be a number and only have 3 digit")
        else:
            return value

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
        self._DDS = self.checkDDS(value)


class Catalog:
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

    def book_not_found(self, counter, book_number):
        counter += 1
        if counter == book_number:
            print("Book not found")
        return counter

    def search_book(self):
        print("---")
        by = int(
            input(f"Search By : \n 1.ISBN \n 2.Author \n 3.Title \n 4.Subject \n 5.DDS \nPlease select number : "))
        book_number = len(self.Books)
        counter = 0
        if by == 1:
            ISBN_select = int(input("Insert ISBN number : "))
            for book in self.Books:
                if ISBN_select == book.ISBN:
                    self.print_book(book)
                    break
                else:
                    counter = self.book_not_found(counter, book_number)
        elif by == 2:
            Author_select = input("Insert Author : ")
            for book in self.Books:
                if Author_select in book.Author:
                    self.print_book(book)
                else:
                    counter = self.book_not_found(counter, book_number)
        elif by == 3:
            Title_select = input("Insert Title : ")
            for book in self.Books:
                if Title_select in book.Title:
                    self.print_book(book)
                else:
                    counter = self.book_not_found(counter, book_number)

        elif by == 4:
            Subject_select = input("Insert Subject : ")
            for book in self.Books:
                if Subject_select in book.Subject:
                    self.print_book(book)
                else:
                    counter = self.book_not_found(counter, book_number)
        elif by == 5:
            DDS_select = int(input("Insert DDS : "))
            for book in self.Books:
                if DDS_select == book.DDS:
                    self.print_book(book)
                else:
                    counter = self.book_not_found(counter, book_number)

    def add_book_to_catalog(self):
        author_list = []
        while True:
            name = input("Insert Author name : ")
            if name == "":
                break
            else:
                authorname = Author(name)
                author_list.append(authorname)
        isbn_check = True
        while isbn_check:
            counter = 0
            isbn = int(input("Insert ISBN number : "))
            for book in self.Books:
                counter += 1
                if isbn == book.ISBN:
                    print("ISBN already exist")
                    break
                elif counter == len(self.Books):
                    isbn_check = False

        title = input("Insert Title : ")
        subject = input("Insert Subject : ")
        dds = int(input("Insert DDS : "))
        book = Book(isbn, author_list, title, subject, dds)
        self.Books.append(book)


Author1 = Author("A")
Author2 = Author("B")
BookA = Book(1544, [Author1, Author2], "Abook1", "Language", 400)
BookB = Book(2366, [Author2], "Abook2", "Language", 400)
libraryA = Catalog()
libraryA.add_book(BookA)
libraryA.add_book(BookB)
libraryA.add_book_to_catalog()
libraryA.search_book()
