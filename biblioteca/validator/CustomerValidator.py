from entities.Customer import Customer
from validator.EntityValidator import EntityValidator


class CustomerValidator(EntityValidator):
    def validate_customer(self, customer):
        super().validate_entity(customer)
        if not isinstance(customer, Customer):
            raise ValueError('Customer is not the correct type')

    def validate_customer_name(self, name):
        if not isinstance(name, str):
            raise ValueError('Customer name is not a string')
        if len(name) == 0:
            raise ValueError('Customer name is empty')

    def validate_customer_cnp(self, cnp):
        if not isinstance(self, cnp):
            raise ValueError('Customer cnp is not a string')
        if len(cnp) == 0:
            raise ValueError('Customer cnp is empty')
        # TODO: validate nr of cifre
