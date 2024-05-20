from repositories.Repository import Repository
from services.BookRentService import BookRentService
from services.BookService import BookService
from services.CustomerService import CustomerService
from ui.console import Console
from validator.BookValidator import BookValidator
from validator.CustomerValidator import CustomerValidator

# run_tests()
book_repo = Repository()
customer_repo = Repository()
book_validator = BookValidator()
customer_validator = CustomerValidator()
book_service = BookService(book_validator, book_repo)
customer_service = CustomerService(customer_validator, customer_repo)
rent_book_service = BookRentService(book_repo, customer_repo)
console = Console(book_service, customer_service, rent_book_service)
console.run()
