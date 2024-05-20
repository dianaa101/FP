from repositories.Repository import Repository


class Service:
    def __init__(self, repo: Repository):
        self.__repo = repo

    def find_residences_by_price_and_city(self, price, city):
        return self.__repo.find_residences_by_price_and_city(price, city)

    def rent_a_residence(self, id_):
        residence = self.__repo.find_by_id(id_)
        total_sum = residence.get_price() + residence.get_warrant() + (residence.get_price() / 2)
        self.__repo.remove_by_id(id_)
        return [residence.get_address(), residence.get_city(), total_sum]
