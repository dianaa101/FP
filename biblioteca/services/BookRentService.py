from repositories.Repository import Repository


class BookRentService:
    def __init__(self, book_repo: Repository, customer_repo: Repository):
        self.book_repo = book_repo
        self.customer_repo = customer_repo

    def rent_book(self, book_id, customer_id):
        book = self.book_repo.find_by_id(book_id)
        customer = self.customer_repo.find_by_id(customer_id)
        if book.get_rented_by_customer_id() is not None:
            raise ValueError('Book already rented!')
        book.set_rented_by_customer_id(customer_id)

        number_of_rents = book.get_number_of_rents()
        book.set_number_of_rents(number_of_rents + 1)

        number_of_rents = customer.get_number_of_rents()
        customer.set_number_of_rents(number_of_rents + 1)

    def return_book(self, book_id, customer_id):
        book = self.book_repo.find_by_id(book_id)
        customer = self.customer_repo.find_by_id(customer_id)
        if customer_id != book.get_rented_by_customer_id():
            raise ValueError('Book is not rented by this customer')
        book.set_rented_by_customer_id(None)


