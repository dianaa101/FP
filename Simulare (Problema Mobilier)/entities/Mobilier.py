from entities.Entity import Entity


class Mobilier(Entity):
    def __init__(self, id_, type_, name, price, available_stock):
        super().__init__(id_)
        self.__type_ = type_
        self.__name = name
        self.__price = price
        self.__available_stock = available_stock

    def get_type(self):
        return self.__type_

    def set_type(self, type_):
        self.__type_ = type_

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_available_stock(self):
        return self.__available_stock

    def set_available_stock(self, available_stock):
        self.__available_stock = available_stock

    def set_multiple(self, id_=None, type_=None, name=None, price=None, available_stock=None):
        super().set_multiple(id_=id_)
        if type_ is not None:
            self.set_type(type_)
        if price is not None:
            self.set_type(price)
        if name is not None:
            self.set_name(name)
        if available_stock is not None:
            self.set_available_stock(available_stock)

    def __str__(self):
        s = super().__str__()
        s = s + f'Type: {self.get_type()} \n'
        s = s + f'Name: {self.get_name()} \n'
        s = s + f'Price: {self.get_price()} \n'
        s = s + f'Available Stock: {self.get_available_stock()}'
        return s

