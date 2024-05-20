from entities.Entity import Entity
from validator.EntityValidator import EntityValidator
from entities.Mobilier import Mobilier


class MobilierValidator(EntityValidator):
    def validate_mobilier(self, mobilier):
        super().validate_entity(mobilier)

        if not isinstance(mobilier, Mobilier):
            raise ValueError('Mobilier is not the correct type')

        es = ''

        try:
            self.validate_type(mobilier.get_type())
        except ValueError as e:
            es = es + str(e) + '\n'

        try:
            self.validate_name(mobilier.get_name())
        except ValueError as e:
            es = es + str(e) + '\n'

        try:
            self.validate_price(mobilier.get_price())
        except ValueError as e:
            es = es + str(e) + '\n'

        try:
            self.validate_available_stock(mobilier.get_available_stock())
        except ValueError as e:
            es = es + str(e) + '\n'

    def validate_type(self, type_):
        if not isinstance(type_, str):
            raise ValueError('Type is not the correct type')
        if len(type_) == 0:
            raise ValueError('Type is empty')

    def validate_name(self, name):
        if not isinstance(name, str):
            raise ValueError('Name is not the correct type')
        if len(name) == 0:
            raise ValueError('Name is empty')

    def validate_price(self, price):
        if not isinstance(price, float):
            raise ValueError('Price is not the correct type')

    def validate_available_stock(self, available_stock):
        if not isinstance(available_stock, int):
            raise ValueError('Available_stock is not the correct type')
