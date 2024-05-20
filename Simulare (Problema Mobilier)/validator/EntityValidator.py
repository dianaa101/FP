from entities.Entity import Entity


class EntityValidator:
    def validate_entity(self, entity):
        if not isinstance(entity, Entity):
            raise ValueError('Entity is not the correct type')
        self.validate_id(entity.get_id())

    def validate_id(self, id_):
        if not isinstance(id_, str):
            raise ValueError('Entity id is not a string')
