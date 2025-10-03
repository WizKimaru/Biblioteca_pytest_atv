from .book import book

class library:
    def __init__(self, book: int, user: int, stock: int):
        if stock < 0:
            raise ValueError("O estoque não pode ser negativo.")
        
        self.book = book
        self.user = user
        self.stock = stock 

    def borrow_book(self, quantity: int):
        if quantity > self.stock:
            raise ValueError("Estoque insuficiente.")
        self.stock -= quantity

    def return_book(self, quantity: int):
        if quantity <= 0:
            raise ValueError("A quantidade deve ser positiva.")
        self.stock += quantity