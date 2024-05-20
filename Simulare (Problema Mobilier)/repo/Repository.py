class Repository:
    def __init__(self):
        self._data = []

    def get_all(self):
        return self._data[:]

    def find_by_type(self, type_):
        furnitures = []
        for x in self._data:
            if x.get_type() == type_ and x.get_available_stock() != 0:
                furnitures.append(x)
        return furnitures

    def find_by_id(self, id_):
        for x in self._data:
            if x.get_id() == id_:
                return x
        raise ValueError(f'Id: {id_} was not found')

    def update(self, id_, *args, **kwargs):
        for x in self._data:
            if x.get_id() == id_:
                x.set_multiple(*args, **kwargs)
                return x
        raise ValueError(f'Id {id_} does not exist!')