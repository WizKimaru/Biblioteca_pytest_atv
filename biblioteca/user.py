from .book import book

class user:
    def __init__(self, name: str, bookList: int):
        if bookList > 3:
            raise ValueError("Não é permitido pegar mais de 3 livros ao mesmo tempo.")
        
        self.name = name
        self.bookList = bookList

    def add_book(self, book: book, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantidade deve ser positiva.")
        book.reduce_stock(quantity)
        self.items.append((book, quantity))

        