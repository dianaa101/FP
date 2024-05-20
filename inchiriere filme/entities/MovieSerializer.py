from entities.Movie import Movie


class MovieSerializer:
    def serialize(self, entity):
        return [
            entity.get_id(),
            entity.get_title(),
            entity.get_description(),
            entity.get_genre()
        ]

    def deserialize(self, parts):
        id_ = int(parts[0])
        title = parts[1]
        description = parts[2]
        genre = parts[3]
        return Movie(id_, title, description, genre)

