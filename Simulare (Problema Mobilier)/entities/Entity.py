class Entity:
    def __init__(self, id_):
        self.__id = id_

    def get_id(self):
        return self.__id

    def set_id(self, id_):
        self.__id = id_

    def set_multiple(self, id_=None):
        if id_ is not None:
            self.set_id(id_)

    def __str__(self):
        s = f'Id: {self.__id}\n'
        return s

