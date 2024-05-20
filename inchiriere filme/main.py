from repo.Repository import Repository
from service.CustomerService import CustomerService
from service.MovieService import MovieService
from service.RentMovieService import RentMovieService
from ui.console import Console
from validator.CustomerValidator import CustomerValidator
from validator.MovieValidator import MovieValidator
from tests import run_tests

movie_repo = Repository()
customer_repo = Repository()
movie_validator = MovieValidator()
customer_validator = CustomerValidator()
movie_service = MovieService(movie_validator, movie_repo)
customer_service = CustomerService(customer_validator, customer_repo)
rent_movie_service = RentMovieService(movie_repo, customer_repo)
console = Console(movie_service, customer_service, rent_movie_service)
console.run()
run_tests()