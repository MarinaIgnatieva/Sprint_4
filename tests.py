from symbol import and_test

import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_no_genre(self, collector_with_books):

        collector_with_books.add_new_book('Вечный зов')

        assert collector_with_books.get_book_genre('Вечный зов') == ''

    def test_add_new_book_add_same_book(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир','Ужасы')
        collector.add_new_book('Война и мир')

        assert collector.get_books_genre().get('Война и мир') == 'Ужасы'



    @pytest.mark.parametrize(
        'new_book, genre_book, new_genre, result',
        [
            ['Му-му', 'Му-му', 'Ужасы', 'Ужасы'],
            ['Му-му', 'Скажи жизни ДА', 'Ужасы', None],
            ['Му-му', 'Му-му', 'Фэнтези', '']
        ]
    )
    def test_set_book_genre(self, new_book, genre_book, new_genre, result):
        collector = BooksCollector()

        collector.add_new_book(new_book)
        collector.set_book_genre(genre_book, new_genre)

        assert collector.get_books_genre().get(genre_book) == result




    def test_get_book_genre_known_book(self, collector_with_books):

        assert collector_with_books.get_book_genre('Му-Му') == 'Ужасы'


    def test_get_book_genre_unknown_book(self, collector_with_books):

        assert collector_with_books.get_book_genre('Атлант расправил плечи') is None




    def test_get_books_with_specific_genre_specific_genre(self, collector_with_books):
        books = collector_with_books.get_books_with_specific_genre('Комедии')

        assert (len(books) == 2
                and 'Девчата' in books
                and 'Операция Ы' in books)

    def test_get_books_with_specific_genre_unknown_genre(self, collector_with_books):
        books = collector_with_books.get_books_with_specific_genre('Фэнтези')

        assert len(books) == 0


    def test_get_books_genre_list_books(self, collector_with_books):
        books = collector_with_books.get_books_genre()

        assert (len(books) == 4
                and 'Му-Му' in books
                and 'Винни-Пух' in books
                and 'Девчата' in books
                and 'Операция Ы' in books)


    def test_get_books_for_children_without_rating_only(self, collector_with_books):
        books = collector_with_books.get_books_for_children()

        assert (len(books) == 3
                and 'Винни-Пух' in books
                and 'Девчата' in books
                and 'Операция Ы' in books)

    def test_get_books_for_children_no_rating_books(self, collector_with_books):
        books = collector_with_books.get_books_for_children()

        assert  'Му-Му' not in books


    def test_add_book_in_favorites_add_book(self, collector_with_books):
        collector_with_books.add_book_in_favorites('Девчата')

        assert (len(collector_with_books.favorites) == 1
                and 'Девчата' in collector_with_books.favorites)

    def test_add_book_in_favorites_unknown_book(self, collector_with_books):
        collector_with_books.add_book_in_favorites('Неизвестная книга')

        assert 'Неизвестная книга' not in collector_with_books.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delet_book(self, collector_with_books):
        collector_with_books.add_book_in_favorites('Винни-Пух')
        collector_with_books.delete_book_from_favorites('Винни-Пух')

        assert len(collector_with_books.favorites) == 0


    def test_get_list_of_favorites_books(self, collector_with_books):
        collector_with_books.add_book_in_favorites('Винни-Пух')
        collector_with_books.add_book_in_favorites('Девчата')
        collector_with_books.get_list_of_favorites_books()

        assert (len(collector_with_books.favorites) == 2
                and 'Винни-Пух' in collector_with_books.favorites
                and 'Девчата' in collector_with_books.favorites)

