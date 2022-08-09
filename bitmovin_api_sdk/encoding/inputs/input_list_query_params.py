class InputListQueryParams(object):
    def __init__(self, offset=None, limit=None, name=None, type_=None, sort=None):
        # type: (int, int, string_types, string_types, string_types) -> None
        super(InputListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.name = name
        self.type = type_
        self.sort = sort

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'name': 'string_types',
            'type': 'string_types',
            'sort': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit',
            'name': 'name',
            'type': 'type',
            'sort': 'sort'
        }

        return attributes
