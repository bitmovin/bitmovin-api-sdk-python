class CodecConfigurationListQueryParams(object):
    def __init__(self, offset=None, limit=None, name=None, sort=None):
        # type: (int, int, string_types, string_types) -> None
        super(CodecConfigurationListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.name = name
        self.sort = sort

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'name': 'string_types',
            'sort': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit',
            'name': 'name',
            'sort': 'sort'
        }

        return attributes
