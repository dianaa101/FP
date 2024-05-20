from entities.Entity import Entity


class Evidence(Entity):
    def __init__(self, id_, description, date, type_, suspect):
        super().__init__(id_)
        self.__suspect = suspect
        self.__type_ = type_
        self.__date = date
        self.__description = description

    def get_date(self):
        return self.__date

    def get_description(self):
        return self.__description

    def get_type(self):
        return self.__type_

    def get_suspect(self):
        return self.__suspect

    def __str__(self):
        s = super().__str__()
        s = s + f'Description: {self.__description} \n'
        s = s + f'Date: {self.__date} \n'
        s = s + f'Type: {self.__type_} \n'
        s = s + f'Suspect: {self.__suspect}'
        return s
