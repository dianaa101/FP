from entities.Evidence import Evidence


class EvidenceSerializer:
    def serialize(self, entity):
        return [
            entity.get_id(),
            entity.get_description(),
            entity.get_date(),
            entity.get_type(),
            entity.get_suspect()
        ]

    def deserialize(self, parts):
        id_ = parts[0]
        description = parts[1]
        str_date = parts[2]
        str_date_parts = str_date.split('/')
        y = int(str_date_parts[0])
        m = int(str_date_parts[1])
        d = int(str_date_parts[2])
        type_ = parts[3]
        suspect = parts[4]
        return Evidence(id_, description, [y, m, d], type_, suspect)