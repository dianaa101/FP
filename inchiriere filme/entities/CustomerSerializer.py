from entities.Customer import Customer


class CustomerSerializer:
    def serialize(self, entity: Customer):
        return [
            entity.get_id(),
            entity.get_name(),
            entity.get_cnp(),
            entity.get_number_of_rents()
        ]

    def deserialize(self, parts):
        id_ = int(parts[0])
        name = parts[1]
        cnp = parts[2]
        number_of_rents = parts[3]
        return Customer(id_, name, cnp, number_of_rents)
