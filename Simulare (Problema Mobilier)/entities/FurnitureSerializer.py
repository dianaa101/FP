from entities.Mobilier import Mobilier


class FurnitureSerializer:
    def serialize(self, furniture):
        return [
            furniture.get_id(),
            furniture.get_type(),
            furniture.get_name(),
            str(furniture.get_price()),
            str(furniture.get_available_stock()),
        ]

    def deserialize(self, parts):
        id_ = parts[0]
        type_ = parts[1]
        name = parts[2]
        price = float(parts[3])
        available_stock = int(parts[4])
        return Mobilier(id_, type_, name, price, available_stock)
