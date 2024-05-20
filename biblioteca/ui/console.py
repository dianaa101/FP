from services.BookRentService import BookRentService
from services.CustomerService import CustomerService
from services.BookService import BookService


class Console:
    def __init__(self, book_service: BookService, customer_service: CustomerService, rent_book_service: BookRentService):
        self.book_service = book_service
        self.customer_service = customer_service
        self.rent_book_service = rent_book_service

    def run(self):
        print("""
1. Add book
2. Update book
3. Show books
4. Delete book
5. Add customer
6. Update customer
7. Show customers
8. Delete customer
9. Find book
10. Find customer
11. Book rental
12. Book return
13. Show the most rented books
14. Show customers with rented books
15. Show 20% most active customers
16. Exit
        """)
        while True:
            try:
                o = int(input("o: "))
            except ValueError:
                continue
            match o:
                case 1:
                    self.add_book()
                case 2:
                    self.update_book()
                case 3:
                    self.show_books()
                case 4:
                    self.delete_book()
                case 5:
                    self.add_customer()
                case 6:
                    self.update_customer()
                case 7:
                    self.show_customers()
                case 8:
                    self.delete_customer()
                case 9:
                    self.find_book()
                case 10:
                    self.find_customer()
                case 11:
                    self.book_rental()
                case 12:
                    self.book_return()
                case 13:
                    self.show_the_most_rented_books()
                case 14:
                    self.show_customers_with_rented_books()
                case 15:
                    self.show_20p_most_active_customers()
                case 16:
                    break

    def show_20p_most_active_customers(self):
        customers = self.customer_service.top_20p_most_active_customers()
        for x in customers:
            print(x)

    def show_customers_with_rented_books(self):
        customers = self.customer_service.get_customers_with_rented_books()
        for x in customers:
            print(x)

    def show_the_most_rented_books(self):
        try:
            number_of_books = int(input('Number of books: '))
            books = self.book_service.most_rented_books(number_of_books)
            print(f'Top {number_of_books} rented books')
            for x in books:
                print(x)
        except ValueError as e:
            print(e)

    def book_return(self):
        try:
            book_id = int(input('Book id: '))
            customer_id = int(input('Customer id: '))
            self.rent_book_service.return_book(book_id, customer_id)
            print('Book returned')
        except ValueError as e:
            print(e)

    def book_rental(self):
        try:
            book_id = int(input('Book id: '))
            customer_id = int(input('Customer id: '))
            self.rent_book_service.rent_book(book_id, customer_id)
            print('Book rented')
        except ValueError as e:
            print(e)

    def find_customer(self):
        try:
            id_ = int(input('Customer Id: '))
            customer = self.customer_service.find_by_id(id_)
            print(customer)
        except ValueError as e:
            print(e)

    def find_book(self):
        try:
            id_ = int(input('Book Id: '))
            book = self.book_service.find_by_id(id_)
            print(book)
        except ValueError as e:
            print(e)

    def delete_customer(self):
        try:
            id_ = int(input('Customer Id: '))
            customer = self.customer_service.remove(id_)
            print(customer)
        except ValueError as e:
            print(e)

    def show_customers(self):
        customers = self.customer_service.get_all()
        for x in customers:
            print(x)

    def update_customer(self):
        try:
            id_ = int(input('Customer id: '))
            name = input('Customer name: ')
            cnp = input('CNP: ')
            if len(name) == 0:
                name = None
            if len(cnp) == 0:
                cnp = None
            customer = self.customer_service.update(id_, name, cnp)
            print(customer)
        except ValueError as e:
            print(e)

    def add_customer(self):
        try:
            name = input('Name: ')
            cnp = input('CNP: ')
            customer = self.customer_service.create_customer(name, cnp)
            print(customer)
        except ValueError as e:
            print(e)

    def delete_book(self):
        try:
            id_ = int(input('Book Id: '))
            book = self.book_service.remove(id_)
            print('Deleted')
            print(book)
        except ValueError as e:
            print(e)

    def show_books(self):
        books = self.book_service.get_all()
        for x in books:
            print(x)

    def update_book(self):
        try:
            id_ = int(input('Book id: '))
            title = input('Title: ')
            author = input('Author name: ')
            description = input('Description: ')
            if len(title) == 0:
                title = None
            if len(author) == 0:
                author = None
            if len(description) == 0:
                description = None
            book = self.book_service.update(id_, title, author, description)
            print(book)
        except ValueError as e:
            print(e)

    def add_book(self):
        try:
            title = input('Title: ')
            author = input('Author name: ')
            description = input('Description: ')
            book = self.book_service.create_book(title, author, description)
            print(book)
        except ValueError as e:
            print(e)
