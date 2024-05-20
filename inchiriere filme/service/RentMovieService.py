from repo.Repository import Repository


class RentMovieService:
    def __init__(self, movie_repo: Repository, customer_repo: Repository):
        self.movie_repo = movie_repo
        self.customer_repo = customer_repo

    def rent_movie(self, movie_id, customer_id):
        movie = self.movie_repo.find_by_id(movie_id)
        customer = self.customer_repo.find_by_id(customer_id)
        if movie.get_rented_by_customer_id() is not None:
            raise ValueError('Movie already rented!')
        movie.set_rented_by_customer_id(customer_id)

        number_of_rents = movie.get_number_of_rents()
        movie.set_number_of_rents(number_of_rents + 1)

        number_of_rents = customer.get_number_of_rents()
        customer.set_number_of_rents(number_of_rents + 1)

    def return_movie(self, movie_id, customer_id):
        movie = self.movie_repo.find_by_id(movie_id)
        customer = self.customer_repo.find_by_id(customer_id)
        if customer_id != movie.get_rented_by_customer_id():
            raise ValueError('Movie is not rented by customer')
        movie.set_rented_by_customer_id(None)