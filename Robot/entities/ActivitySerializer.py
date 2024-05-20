from entities.Activity import Activity

class ActivitySerializer:
    def serialize(self, entity):
        return [
            entity.get_id(),
            entity.get_battery_percentage(),
            entity.get_description(),
            entity.get_instruction()
        ]

    def deserialize(self, parts):
        id_ = parts[0]
        battery_percentage = int(parts[1])
        description = parts[2]
        instructions = parts[3].split(',')
        return Activity(id_, battery_percentage, description, instructions)
