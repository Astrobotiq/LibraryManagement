class Library:
    def __init__(self):
        self.book = open("book.txt", "a+")

    def __del__(self):
        self.book.close()

    def list_books(self):
        self.book.seek(0)

        list = []
        for line in self.book:
            book_info = line.split(",", 3)
            if len(book_info) == 4:
                name = book_info[0].strip()
                author = book_info[1].strip()
                year = book_info[2].strip()
                page = book_info[3].strip()
                list.append([name, author, year, page])
        return list

    def add_book(self, name, author, page, date="unknown"):

        line = name.lower() + "," + author.lower() + "," + date.lower() + "," + page.lower() + "\n"
        self.book.write(line)
        print("book is added")


    def remove_book(self, name):
        contents = []
        self.book.seek(0)
        contents = self.book.readlines()
        name = name.lower()
        index = -1

        for i, line in enumerate(contents):
            book_info = line.split(",", 1)
            if book_info[0].strip() == name.strip():
                index = i
                break

        if index != -1:
            del contents[index]
            self.book.seek(0)
            self.book.truncate()
            for i in contents:
                self.book.write(i.strip() + "\n")
            print("Book deleted succesfully")
        else:
            print("Book is not found!")


library = Library()
list = library.list_books()
