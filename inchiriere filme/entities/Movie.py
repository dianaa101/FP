from entities.Entity import Entity


class Movie(Entity):
    def __init__(self, id_, title, description, genre, rented_by_customer_id, number_of_rents):
        super().__init__(id_)

        self.__title = title
        self.__description = description
        self.__genre = genre
        self.__rented_by_customer_id = rented_by_customer_id
        self.__number_of_rents = number_of_rents

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def get_rented_by_customer_id(self):
        return self.__rented_by_customer_id

    def set_rented_by_customer_id(self, rented_by_customer_id):
        self.__rented_by_customer_id = rented_by_customer_id

    def get_number_of_rents(self):
        return self.__number_of_rents

    def set_number_of_rents(self, number_of_rents):
        self.__number_of_rents = number_of_rents

    def set_multiple(self, id_=None, title=None, description=None, genre=None, rented_by_customer_id=None, number_of_rents=None):
        super().set_multiple(id_=id_)
        if title is not None:
            self.set_title(title)
        if description is not None:
            self.set_description(description)
        if genre is not None:
            self.set_genre(genre)
        if rented_by_customer_id is not None:
            self.set_rented_by_customer_id(rented_by_customer_id)
        if number_of_rents is not None:
            self.set_number_of_rents(number_of_rents)

    def __str__(self):
        s = super().__str__()
        s = s + f'Title: {self.__title} \n'
        s = s + f'Description: {self.__description} \n'
        s = s + f'Genre: {self.__genre} \n'
        s = s + f'Number of rents: {self.__number_of_rents}'
        return s
