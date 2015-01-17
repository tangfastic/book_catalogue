import sys
from book_catalogue import Book, Catalogue

class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.catalogue = Catalogue()
        self.choices = {
            "1": self.show_books,
            "2": self.search_books,
            "3": self.add_book,
            "4": self.quit}

    def display_menu(self):
        print("""
Book Catalogue Menu

1. Show All Books
2. Search Books
3. Add Book
4. Quit
""")

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if not choice:
                print("You need to select an option.")
            elif action:
                action()
            else:
                print("{} is not a valid option".format(choice))

    def show_books(self):
        self.catalogue.show_books()

    def search_books(self):
        title = input("Enter the title: ")
        authors = input("Enter the author(s): ")
        subject = input("Enter the subject: ")
        isbn = input("Enter the ISBN: ")
        self.catalogue.search(title, authors, subject, isbn)

    def add_book(self):
        title = input("Enter title: ")
        authors = input("Enter author(s): ")
        subject = input("Enter the subject: ")
        isbn = input("Enter ISBN: ")
        self.catalogue.new_book(title, authors, subject, isbn)
        print("Book has been added")
        
    def quit(self):
        print("Thank you for using the Book Catalogue today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
