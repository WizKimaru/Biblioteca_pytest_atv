class BibliotecaError(Exception): 
    """ Exceção base para erros no sistema  de e-commerce. """
    
class OutStockError(BibliotecaError): 
    """ Erro quando não há estoque suficiente. """

class InvalidQuantityError(BibliotecaError): 
    """ Erro quando a quantidade é inválida. """
