class ManifestListQueryParams(object):
    def __init__(self, offset=None, limit=None, sort=None):
        # type: (int, int, string_types) -> None
        super(ManifestListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.sort = sort

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'sort': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit',
            'sort': 'sort'
        }

        return attributes
