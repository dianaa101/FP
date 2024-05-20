from entities.Entity import Entity


class Activity(Entity):
    def __init__(self, id_, battery_percentage, description, instructions):
        super().__init__(id_)
        self.__battery_percentage = battery_percentage
        self.__description = description
        self.__instructions = instructions

    def get_battery_percentage(self):
        return self.__battery_percentage

    def get_description(self):
        return self.__description

    def get_instructions(self):
        return self.__instructions

    def __str__(self):
        s = super().__str__()
        s = s + f'Battery Percentage: {self.__battery_percentage}\n'
        s = s + f'Description: {self.__description}\n'
        s = s + f'Instructions: {",".join(self.__instructions)}\n'
        return s
