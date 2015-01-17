"""Book Catalogue to store a directory of all your books."""

class Book:
    '''Represents a book in a catalogue.'''
    def __init__(self, title, authors, subject, isbn):
        '''Initialise a book with title, authors, subject, isbn and dds.'''
        self.title = title
        '''Authors attribute should be entered as a list. I've added a conditional
        statement to convert to list if string is entered instead.'''
        if type(authors) == str:
            authors = authors.split(", ")
        self.authors = authors
        self.subject = subject
        self.isbn = isbn

    def __str__(self):
        authors_str = ", ".join(self.authors)
        rep = "Title: {}".format(self.title) + "\n" + "Author(s): {}".format(authors_str) \
              + "\n" + "Subject: {}".format(self.subject) + "\n" + \
              "ISBN: {}".format(self.isbn)
        return rep

class Catalogue:
    '''Represents a collection of books.'''
    def __init__(self):
        '''Initialise a catalogue with an empty list.'''
        self.books =[]

    def new_book(self, title, authors, subject, isbn):
        '''Create a new book and add it to the list.'''
        self.books.append(Book(title, authors, subject, isbn))

    def show_books(self):
        for book in self.books:
            print()
            print(str(book))

    def search(self, title='', authors=[''], subject='', isbn=''):
        '''Search for book in catalogue with title, subject, authors and isbn. At least
        one parameter is needed. Others are optional.'''

        search_results = []
        '''Any books matching the search criteria will be added to this list.'''

        if type(authors) == str:
            authors = authors.split(", ")

        if not title and not subject and not isbn and authors == ['']:
            print()
            print("You need to enter at least one search parameter.")
            return None

        print()
        print("Search Results: ")
        print("-" * 14)

        for book in self.books:
            matches = 0
            if title and title == book.title:
                matches += 1
            if subject and subject == book.subject:
                matches += 1
            if authors != [''] and all(x in book.authors for x in authors):
                matches += 1
            if isbn and isbn == book.isbn:
                matches += 1

            search_p = [title, subject, authors, isbn]
            search_p = [x for x in search_p if x != '' and x != ['']]
            if matches == len(search_p):
                search_results.append(book)

        if search_results:
            for book in search_results:
                print()
                print(str(book))

        else:
            print()
            print("No books found.")

if __name__ == "__main__":
    catalogue = Catalogue()
    catalogue.new_book("Python Programming", ["Michael Dawson"], "Programming",\
                       "044328")
    catalogue.new_book("Learn Python the Hard Way", "Zed Shaw", "Programming",\
                       "032188")
    catalogue.new_book("Python 3 Object Oriented Programming", ["Dusty Phillips"],\
                       "Programming", "978184")
    catalogue.new_book(title="English Romantic Poetry: An Anthology", \
                       authors=["William Blake", "William Wordsworth", "Samuel Taylor Coleridge",\
                                "Lord Byron", "Percy Bysshe Shelley", "John Keats"],
                       subject = "English Literature", isbn="048629")
    catalogue.new_book("Enduring Love", "Ian McEwan", "English Literature", "899347")
