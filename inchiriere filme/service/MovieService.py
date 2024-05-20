from entities.Movie import Movie
from repo.Repository import Repository
from validator.MovieValidator import MovieValidator


class MovieService:
    def __init__(self, validator: MovieValidator, repo: Repository):
        self.__validator = validator
        self.__repo = repo

    def create(self, title, description, genre):
        id_ = self.__repo.get_available_id()
        movie = Movie(id_, title, description, genre, None, 0)
        self.__validator.validate_movie(movie)
        self.__repo.add(movie)
        return movie

    def remove(self, id_):
        return self.__repo.remove_by_id(id_)

    def get_all(self):
        return self.__repo.get_all()

    def update(self, id_, title, description, genre):
        if title is not None:
            self.__validator.validate_title(title)
        if description is not None:
            self.__validator.validate_description(description)
        if genre is not None:
            self.__validator.validate_genre(genre)
        return self.__repo.update(id_, title=title, description=description, genre=genre)

    def find_by_id(self, id_):
        return self.__repo.find_by_id(id_)

    def get_most_rented_movies(self, number_of_movies):
        movies = self.get_all()
        movies.sort(key=lambda x: x.get_number_of_rents(), reverse=True)
        return movies[:number_of_movies]
