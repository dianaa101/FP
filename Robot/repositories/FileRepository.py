from repositories.Repository import Repository


class FileRepository(Repository):
    def __init__(self, file_path, serializer):
        super().__init__()

        self.__file_path = file_path
        self.__serializer = serializer
        self.__separator = ';'

    def _load_from_file(self):
        try:
            with open(self.__file_path, 'r') as f:
                entities = []
                for line in f:
                    line = line[:-1]
                    parts = line.split(self.__separator)
                    entity = self.__serializer.deserialize(parts)
                    entities.append(entity)
                self._data = entities
        except FileNotFoundError:
            with open(self.__file_path, 'w'):
                self._data = []

    def get_all(self):
        self._load_from_file()
        return super().get_all()