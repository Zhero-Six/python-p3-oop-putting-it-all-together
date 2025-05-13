# lib/shoe.py

class Shoe:
    def __init__(self, brand, size):
        """Initialize a Shoe with brand and size"""
        self._brand = brand
        self._size = size
        self.condition = None  # Initialize condition attribute

    @property
    def brand(self):
        """Get the shoe brand"""
        return self._brand

    @property
    def size(self):
        """Get the shoe size"""
        return self._size

    @size.setter
    def size(self, value):
        """Set the shoe size with type validation"""
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        """Repair the shoe and set condition to New"""
        print("Your shoe is as good as new!")
        self.condition = "New"