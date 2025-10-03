import pytest
from biblioteca.book import book

def test_criar_livro_válido():
    b = book("Santuario de carne", "Anna Magdala", 8)
    assert b.name == "Santuario de carne"
    assert b.price == "Anna Magdala"
    assert b.stock == 8
