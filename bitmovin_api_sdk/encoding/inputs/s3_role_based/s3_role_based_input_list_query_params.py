class S3RoleBasedInputListQueryParams(object):
    def __init__(self, offset=None, limit=None, name=None):
        # type: (int, int, string_types) -> None
        super(S3RoleBasedInputListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.name = name

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'name': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit',
            'name': 'name'
        }

        return attributes
