from service.CustomerService import CustomerService
from service.MovieService import MovieService
from service.RentMovieService import RentMovieService


class Console:
    def __init__(self, movie_service: MovieService, customer_service: CustomerService, rent_movie_service: RentMovieService):
        self.movie_service = movie_service
        self.customer_service = customer_service
        self.rent_movie_service = rent_movie_service

    def run(self):
        print("""
1. Add movie
2. Update movie
3. Show movies
4. Delete movie
5. Find movie
6. Add customer
7. Update customer
8. Show customers
9. Delete customer
10. Find customer
11. Movie rent
12. Movie return
13. Show customers with rents
14. Get top 20 customers with rents
15. Most rented movies
16. Exit
        """)
        while True:
            try:
                o = int(input("o: "))
            except ValueError:
                continue
            match o:
                case 1:
                    self.add_movie()
                case 2:
                    self.update_movie()
                case 3:
                    self.show_movies()
                case 4:
                    self.delete_movie()
                case 5:
                    self.find_movie()
                case 6:
                    self.add_customer()
                case 7:
                    self.update_customer()
                case 8:
                    self.show_customers()
                case 9:
                    self.delete_customer()
                case 10:
                    self.find_customer()
                case 11:
                    self.movie_rent()
                case 12:
                    self.movie_return()
                case 13:
                    self.show_customers_with_rents()
                case 14:
                    self.show_top_30p_customers_with_rents()
                case 15:
                    self.most_rented_movies()
                case 16:
                    break

    def find_movie(self):
        try:
            id_ = int(input('Movie Id: '))
            movie = self.movie_service.find_by_id(id_)
            print(movie)
        except ValueError as e:
            print(e)

    def delete_movie(self):
        try:
            id_ = int(input('Movie ID: '))
            movie = self.movie_service.remove(id_)
            print('Deleted')
            print(movie)
        except ValueError as e:
            print(e)

    def show_movies(self):
        movies = self.movie_service.get_all()
        for x in movies:
            print(x)

    def update_movie(self):
        try:
            id_ = int(input('Movie Id: '))
            title = input('Title: ')
            description = input('Description: ')
            genre = input('Genre: ')
            if len(title) == 0:
                title = None
            if len(description) == 0:
                description = None
            if len(genre) == 0:
                genre = None
            movie = self.movie_service.update(id_, title, description, genre)
            print(movie)
        except ValueError as e:
            print(e)

    def add_movie(self):
        try:
            title = input('Title: ')
            description = input('Description: ')
            genre = input('Genre: ')
            movie = self.movie_service.create(title, description, genre)
            print(movie)
        except ValueError as e:
            return e

    def add_customer(self):
        try:
            name = input('Name: ')
            cnp = input('CNP: ')
            customer = self.customer_service.create(name, cnp)
            print(customer)
        except ValueError as e:
            return e

    def update_customer(self):
        try:
            id_ = int(input('Customer Id: '))
            name = input('Name: ')
            cnp = input('CNP: ')
            if len(name) == 0:
                name = None
            if len(cnp) == 0:
                cnp = None
            customer = self.customer_service.update(id_, name, cnp)
            print(customer)
        except ValueError as e:
            print(e)

    def show_customers(self):
        customers = self.customer_service.get_all()
        for x in customers:
            print(x)

    def delete_customer(self):
        try:
            id_ = int(input('Customer ID: '))
            customer = self.customer_service.remove(id_)
            print('Deleted')
            print(customer)
        except ValueError as e:
            print(e)

    def find_customer(self):
        try:
            id_ = int(input('Customer ID: '))
            customer = self.customer_service.find_by_id(id_)
            print(customer)
        except ValueError as e:
            print(e)

    def movie_rent(self):
        try:
            movie_id = int(input('Movie ID: '))
            customer_id = int(input('Customer ID: '))
            self.rent_movie_service.rent_movie(movie_id, customer_id)
            print('Movie rented')
        except ValueError as e:
            print(e)

    def movie_return(self):
        try:
            movie_id = int(input('Movie ID: '))
            customer_id = int(input('Customer ID: '))
            self.rent_movie_service.return_movie(movie_id, customer_id)
            print('Movie returned')
        except ValueError as e:
            print(e)

    def show_customers_with_rents(self):
        customers = self.customer_service.get_customers_with_rented_movies()
        for x in customers:
            print(x)

    def show_top_30p_customers_with_rents(self):
        customers = self.customer_service.get_top_30p_customers_with_rented_movies()
        for x in customers:
            print(x)

    def most_rented_movies(self):
        try:
            number_of_movies = int(input('Number of movies: '))
            movies = self.movie_service.get_most_rented_movies(number_of_movies)
            print(f'Top {number_of_movies} rented movies')
            for x in movies:
                print(x)
        except ValueError as e:
            print(e)