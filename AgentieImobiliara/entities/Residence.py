from entities.Entity import Entity


class Residence(Entity):
    def __init__(self, id_, address, city, price, warrant):
        super().__init__(id_)
        self.__address = address
        self.__city = city
        self.__price = price
        self.__warrant = warrant

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_price(self):
        return self.__price

    def get_warrant(self):
        return self.__warrant

    def __str__(self):
        s = super().__str__()
        s = s + f'Address: {self.__address} \n'
        s = s + f'City: {self.__city} \n'
        s = s + f'Price: {self.__price} \n'
        s = s + f'Warrant: {self.__warrant}'
        return s