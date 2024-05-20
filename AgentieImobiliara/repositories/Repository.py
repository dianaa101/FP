class Repository:
    def __init__(self):
        """
        Create a repo.
        """
        self._data = []

    def get_all(self):
        """
        Get all the entities
        :return All the entities
        """
        return self._data[:]

    def find_residences_by_price_and_city(self, price, city):
        residences = self._data
        found_residences = []

        for x in residences:
            if x.get_price() < price and x.get_city() == city:
                found_residences.append(x)
        return found_residences

    def find_by_id(self, id_):
        for x in self._data:
            if x.get_id() == id_:
                return x
        raise ValueError(f'Id: {id_} was not found')

    def remove_by_id(self, id_):
        for x in self._data:
            if x.get_id() == id_:
                self._data.remove(x)
                return x
        raise ValueError(f'Id: {id_} does not exist')
