class CencDrmListQueryParams(object):
    def __init__(self, offset=None, limit=None):
        # type: (string_types, string_types) -> None
        super(CencDrmListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit

    @property
    def openapi_types(self):
        types = {
            'offset': 'string_types',
            'limit': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit'
        }

        return attributes
