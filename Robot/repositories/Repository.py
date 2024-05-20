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