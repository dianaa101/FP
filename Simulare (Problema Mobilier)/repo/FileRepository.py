from repo.Repository import Repository


class FileRepository(Repository):
    def __init__(self, file_path, serializer):
        super().__init__()

        self.__file_path = file_path
        self.__serializer = serializer
        self.__separator = ','

    def _save_to_file(self):
        with open(self.__file_path, 'w') as f:
            for entity in self._data:
                parts = self.__serializer.serialize(entity)
                parts = [str(x) for x in parts]
                line = self.__separator.join(parts) + '\n'
                f.write(line)

    def _load_from_file(self):
        try:
            with open(self.__file_path, 'r') as f:
                entities = []
                for line in f:
                    line = line[:-1]
                    parts = line.split(self.__separator)
                    try:
                        entity = self.__serializer.deserialize(parts)
                        entities.append(entity)
                    except Exception as e:
                        print(f'Failed to deserialize: "{line}"', e)
                self._data = entities
        except FileNotFoundError:
            with open(self.__file_path, 'w'):
                self._data = []

    def get_all(self):
        self._load_from_file()
        return super().get_all()

    def find_by_id(self, id_):
        self._load_from_file()
        return super().find_by_id(id_)

    def find_by_type(self, type_):
        self._load_from_file()
        return super().find_by_type(type_)

    def update(self, id_, *args, **kwargs):
        self._load_from_file()
        x = super().update(id_, *args, **kwargs)
        self._save_to_file()
        return x
