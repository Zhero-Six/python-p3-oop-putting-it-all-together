# lib/book.py

class Book:
    def __init__(self, title, page_count):
        """Initialize a Book with title and page_count"""
        self._title = title
        self._page_count = page_count

    @property
    def title(self):
        """Get the book title"""
        return self._title

    @property
    def page_count(self):
        """Get the page count"""
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """Set the page count with type validation"""
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        """Simulate turning a page"""
        print("Flipping the page...wow, you read fast!")