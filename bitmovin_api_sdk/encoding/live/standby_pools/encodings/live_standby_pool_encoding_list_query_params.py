class LiveStandbyPoolEncodingListQueryParams(object):
    def __init__(self, offset=None, limit=None, sort=None, status=None):
        # type: (int, int, string_types, string_types) -> None
        super(LiveStandbyPoolEncodingListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.sort = sort
        self.status = status

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'sort': 'string_types',
            'status': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit',
            'sort': 'sort',
            'status': 'status'
        }

        return attributes
