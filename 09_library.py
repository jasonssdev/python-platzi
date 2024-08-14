class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_avaiable = True

    def borrow(self):
        if self.is_avaiable:
            self.is_avaiable = False
            print(f"{self.title} book has been borrowed")