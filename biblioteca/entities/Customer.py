from entities.Entity import Entity


class Customer(Entity):
    def __init__(self, id_, name, cnp, number_of_rents):
        super().__init__(id_)

        self.__name = name
        self.__cnp = cnp
        self.__number_of_rents = number_of_rents

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_cnp(self):
        return self.__cnp

    def set_cnp(self, cnp):
        self.__cnp = cnp

    def get_number_of_rents(self):
        return self.__number_of_rents

    def set_number_of_rents(self, number_of_rents):
        self.__number_of_rents = number_of_rents

    def set_multiple(self, id_=None, name=None, cnp=None, number_of_rents=None):
        super().set_multiple(id_=id_)
        if name is not None:
            self.set_name(name)
        if cnp is not None:
            self.set_cnp(cnp)
        if number_of_rents is not None:
            self.set_number_of_rents(number_of_rents)

    def __str__(self):
        s = super().__str__()
        s = s + f'Name: {self.__name}\n'
        s = s + f'CNP: {self.__cnp}\n'
        s = s + f'Number of rents: {self.__number_of_rents}\n'
        return s
