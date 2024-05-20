from entities.Mobilier import Mobilier
from repo import Repository
from repo.FileRepository import FileRepository
from validator import MobilierValidator


class MobilierService:
    def __init__(self, validator: MobilierValidator, repo: FileRepository):
        self.__repo = repo
        self.__validator = validator

    def get_all(self):
        return self.__repo.get_all()

    def find_by_type(self, type_):
        return self.__repo.find_by_type(type_)

    def find_by_id(self, id_):
        return self.__repo.find_by_id(id_)

    def buy_furniture(self, id_, requested_stock):
        furniture = self.__repo.find_by_id(id_)
        price = requested_stock * furniture.get_price()
        remaining_stock = furniture.get_available_stock() - requested_stock
        if remaining_stock < 0:
            raise ValueError(f'Stock too large, remaining stock: {furniture.get_available_stock()}')
        self.__repo.update(id_, available_stock=remaining_stock)
        return [furniture.get_name(), price, remaining_stock]
