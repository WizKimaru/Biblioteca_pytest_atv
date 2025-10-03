class book:
    def __init__(self, title: str, author: str, stock: int):
        if stock < 0:
            raise ValueError("O estoque não pode ser negativo.")
        
        self.title = title
        self.author = author
        self.stock = stock 

    def reduce_stock(self, quantity: int):
        if quantity > self.stock:
            raise ValueError("Estoque insuficiente.")
        self.stock -= quantity

    def increase_stock(self, quantity: int):
        if quantity <= 0:
            raise ValueError("A quantidade deve ser positiva.")
        self.stock += quantity
        