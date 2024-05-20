from entities.Residence import Residence


class ResidenceSerializer:
    def serialize(self, entity):
        return [
            entity.get_id(),
            entity.get_address(),
            entity.get_city(),
            str(entity.get_price()),
            str(entity.get_warrant()),
        ]

    def deserialize(self, parts):
        id_ = parts[0]
        address = parts[1]
        city = parts[2]
        price = float(parts[3])
        warrant = float(parts[4])
        return Residence(id_, address, city, price, warrant)
