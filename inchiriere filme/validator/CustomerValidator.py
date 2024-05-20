from entities.Customer import Customer
from validator.EntityValidator import EntityValidator


class CustomerValidator(EntityValidator):
    def validate_customer(self, customer):
        super().validate_entity(customer)

        if not isinstance(customer, Customer):
            raise ValueError('Customer is not the correct type')

        es = ''
        try:
            self.validate_name(customer.get_name())
        except ValueError as e:
            es = es + str(e) + '\n'

        try:
            self.validate_cnp(customer.get_cnp())
        except ValueError as e:
            es = es + str(e) + '\n'

        if len(es) != 0:
            raise ValueError(es)

    def validate_name(self, name):
        if not isinstance(name, str):
            raise ValueError('Name is not a string type')
        if len(name) == 0:
            raise ValueError('Name is empty')

    def validate_cnp(self, cnp):
        if not isinstance(cnp, str):
            raise ValueError('Customer cnp is not a string')
        if len(cnp) == 0:
            raise ValueError('Customer cnp is empty')
