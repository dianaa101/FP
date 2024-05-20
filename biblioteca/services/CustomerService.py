from entities.Customer import Customer
from repositories.Repository import Repository
from validator.CustomerValidator import CustomerValidator


class CustomerService:
    def __init__(self, validator: CustomerValidator, repo: Repository):
        self.__validator = validator
        self.__repo = repo

    def create_customer(self, name, cnp):
        id_ = self.__repo.get_available_id()
        customer = Customer(id_, name, cnp, 0)
        self.__validator.validate_customer(customer)
        self.__repo.add(customer)
        return customer

    def remove(self, id_):
        self.__repo.remove_by_id(id_)

    def get_all(self):
        return self.__repo.get_all()

    def find_by_id(self, id_):
        return self.__repo.find_by_id(id_)

    def update(self, id_, name, cnp):
        if name is not None:
            self.__validator.validate_customer(name)
        if cnp is not None:
            self.__validator.validate_customer(cnp)
        return self.__repo.update_by_id(id_, name=name, cnp=cnp)

    def get_customers_with_rented_books(self):
        customers = self.get_all()

        filtered = []
        for x in customers:
            if x.get_number_of_rents() != 0:
                filtered.append(x)
        customers = filtered

        customers.sort(key=lambda x: (x.get_name(), -x.get_number_of_rents()))
        return customers

    def top_20p_most_active_customers(self):
        # nume client + nr de carti inchiriate

        customers = self.get_all()

        filtered = []
        for x in customers:
            if x.get_number_of_rents() != 0:
                filtered.append(x)
        customers = filtered

        customers.sort(key=lambda x: x.get_number_of_rents(), reverse=True)

        n = len(customers) // 5
        if n == 0:
            n = 1
        return customers[:n]

