from entities.Book import Book
from repositories.Repository import Repository
from validator.BookValidator import BookValidator


class BookService:
    def __init__(self, validator: BookValidator, repo: Repository):
        self.__validator = validator
        self.__repo = repo

    def create_book(self, title, author, description):
        id_ = self.__repo.get_available_id()
        book = Book(id_, title, author, description, None, 0)
        self.__validator.validate_book(book)
        self.__repo.add(book)
        return book

    def remove(self, id_):
        self.__repo.remove_by_id(id_)

    def get_all(self):
        return self.__repo.get_all()

    def find_by_id(self, id_):
        return self.__repo.find_by_id(id_)

    def update(self, id_, title, author, description):
        if title is not None:
            self.__validator.validate_book_title(title)
        if author is not None:
            self.__validator.validate_author(author)
        if description is not None:
            self.__validator.validate_description(description)
        return self.__repo.update_by_id(id_, title=title, author=author, description=description)

    def most_rented_books(self, number_of_books):
        books = self.get_all()
        books.sort(key=lambda x: x.get_number_of_rents(), reverse=True)
        return books[:number_of_books]
