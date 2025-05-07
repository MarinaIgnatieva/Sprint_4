import pytest

from main import BooksCollector

@pytest.fixture
def collector_with_books():
    collector=BooksCollector()
    books = {
        'Му-Му': 'Ужасы',
        'Винни-Пух': 'Мультфильмы',
        'Девчата' : 'Комедии',
        'Операция Ы': 'Комедии',
    }
    for name, genre in books.items():
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector

