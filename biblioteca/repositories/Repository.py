class Repository:
    def __init__(self):
        self._data = []

    def add(self, entity):
        for x in self._data:
            if x.get_id() == entity.get_id():
                raise ValueError(f'Id {entity.get_id()} already exists!')
        self._data.append(entity)

    def get_available_id(self):
        id_ = 0
        for x in self._data:
            if x.get_id() >= id_:
                id_ = x.get_id() + 1
        return id_

    def get_all(self):
        return self._data[:]

    def remove_by_id(self, id_):
        entities = self.get_all()
        for x in entities:
            if x.get_id == id_:
                self._data.remove(x)
                return x
        raise ValueError(f'Id: {id_} does not exist!')

    def find_by_id(self, id_):
        for x in self._data:
            if x.get_id() == id_:
                return x
        raise ValueError(f'Id: {id_} does not exist!')

    def update_by_id(self, searched_id, *args, **kwargs):
        for x in self._data:
            if x.get_id() == searched_id:
                x.set_multiple(*args, **kwargs)
                return x
        raise ValueError(f'Id {searched_id} does not exist!')

