from entities.Customer import Customer
from repo.Repository import Repository
from validator.CustomerValidator import CustomerValidator


class CustomerService:
    def __init__(self, validator: CustomerValidator, repo: Repository):
        self.__validator = validator
        self.__repo = repo

    def create(self, name, cnp):
        id_ = self.__repo.get_available_id()
        customer = Customer(id_, name, cnp, 0)
        self.__validator.validate_customer(customer)
        self.__repo.add(customer)
        return customer

    def remove(self, id_):
        return self.__repo.remove_by_id(id_)

    def get_all(self):
        return self.__repo.get_all()

    def update(self, id_, name=None, cnp=None):
        if name is not None:
            self.__validator.validate_name(name)
        if cnp is not None:
            self.__validator.validate_cnp(cnp)
        return self.__repo.update(id_, name=name, cnp=cnp)

    def find_by_id(self, id_):
        return self.__repo.find_by_id(id_)

    def get_customers_with_rented_movies(self):
        customers = self.get_all()
        c_rents = []
        for x in customers:
            if x.get_number_of_rents() != 0:
                c_rents.append(x)

        c_rents.sort(key=lambda x:(x.get_name(), x.get_number_of_rents()))
        return c_rents

    def get_top_30p_customers_with_rented_movies(self):
        customers = self.get_all()
        c_rents = []
        for x in customers:
            if x.get_number_of_rents() != 0:
                c_rents.append(x)

        c_rents.sort(key=lambda x:(x.get_name(), x.get_number_of_rents()))

        n = int(len(c_rents) * 0.3)
        cr = max(n, 1)
        return c_rents[:cr]
