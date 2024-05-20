class Repository:
    def __init__(self):
        self._data = []

    def add(self, entity):
        # daca x se afla in lista
        for x in self._data:
            # atunci verificam daca id-ul e luat cumva
            if x.get_id() == entity.get_id():
                raise ValueError(f'Id: {entity.get_id()} already exists')
        # daca nu, se adauga la lista
        self._data.append(entity)

    def get_available_id(self):
        id_ = 0
        # daca x se afla in lista
        for x in self._data:
            # verificam daca id-ul este mai mare sau egal cu cel mai mare id current
            if x.get_id() >= id_:
                # daca da, se adauga 1 la id, cuz it has to be unique
                id_ = x.get_id() + 1
        return id_

    def get_all(self):
        # when you use [:] with a list, it creates a new list that is a shallow copy of the original list.
        # A shallow copy means that the new list contains references to the same objects as the original list
        return self._data[:]

    def find_by_id(self, id_):
        for x in self._data:
            if x.get_id() == id_:
                return x
        raise ValueError(f'Id: {id_} was not found')

    def remove_by_id(self, id_):
        searched_ids = self.get_all()
        for x in searched_ids:
            if x.get_id() == id_:
                self._data.remove(x)
                return x
        raise ValueError(f'Id: {id_} does not exist')

    def update(self, id_, *args, **kwargs):
        for x in self._data:
            if x.get_id() == id_:
                x.set_multiple(*args, **kwargs)
                return x
        raise ValueError(f'Id {id_} does not exist!')
