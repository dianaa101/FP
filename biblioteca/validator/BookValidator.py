from entities.Book import Book
from validator.EntityValidator import EntityValidator


class BookValidator(EntityValidator):
    def validate_book(self, book):
        super().validate_entity(book)
        if not isinstance(book, Book):
            raise ValueError('Book is not the correct type')

        es = ''

        try:
            self.validate_book_title(book.get_title())
        except ValueError as e:
            es = es + str(e) + '\n'

        try:
            self.validate_author(book.get_author())
        except ValueError as e:
            es = es + str(e) + '\n'

        try:
            self.validate_description(book.get_description())
        except ValueError as e:
            es = es + str(e) + '\n'

        if len(es) != 0:
            raise ValueError(es)

    def validate_book_title(self, title):
        if not isinstance(title, str):
            raise ValueError('Book title is not a string')
        if len(title) == 0:
            raise ValueError('Book title is empty')

    def validate_author(self, author):
        if not isinstance(author, str):
            raise ValueError('Author is not a string')
        if len(author) == 0:
            raise ValueError('Author name is empty')

    def validate_description(self, description):
        if not isinstance(description, str):
            raise ValueError('Description is not a string')
        if len(description) == 0:
            raise ValueError('Description is empty')
