from entities.Entity import Entity
from validator.EntityValidator import EntityValidator
from entities.Movie import Movie


class MovieValidator(EntityValidator):
    def validate_movie(self, movie):
        super().validate_entity(movie)

        if not isinstance(movie, Movie):
            raise ValueError('Movie is not the correct type')

        es = ''

        try:
            self.validate_title(movie.get_title())
        except ValueError as e:
            es = es + str(e) + '\n'

        try:
            self.validate_description(movie.get_description())
        except ValueError as e:
            es = es + str(e) + '\n'

        try:
            self.validate_genre(movie.get_genre())
        except ValueError as e:
            es = es + str(e) + '\n'

        if len(es) != 0:
            raise ValueError(es)

    def validate_title(self, title):
        if not isinstance(title, str):
            raise ValueError('Movie title is not a string')
        if len(title) == 0:
            raise ValueError('Movie title is empty')

    def validate_description(self, description):
        if not isinstance(description, str):
            raise ValueError('Description is not a string')
        if len(description) == 0:
            raise ValueError('Description is empty')

    def validate_genre(self, genre):
        if not isinstance(genre, str):
            raise ValueError('Genre is not a string')
        if len(genre) == 0:
            raise ValueError('Genre is empty')

