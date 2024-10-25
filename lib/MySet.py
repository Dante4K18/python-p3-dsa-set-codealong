class MySet:
    def __init__(self, iterable=None):
        self.dictionary = {}  # Using a dictionary to simulate set behavior
        if iterable is not None:
            for item in iterable:
                self.add(item)  # Add items to the set

    def add(self, value):
        self.dictionary[value] = True  # Use dictionary keys for unique values

    def delete(self, value):
        if value in self.dictionary:
            del self.dictionary[value]

    def has(self, value):
        return value in self.dictionary

    def size(self):
        return len(self.dictionary)
