##

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


b = Book('Python rocks', 'Jane', '50')

print(b)
print(b.pages)
