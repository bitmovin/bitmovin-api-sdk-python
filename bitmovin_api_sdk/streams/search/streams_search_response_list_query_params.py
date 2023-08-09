class StreamsSearchResponseListQueryParams(object):
    def __init__(self, offset=None, limit=None, query=None):
        # type: (int, int, string_types) -> None
        super(StreamsSearchResponseListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.query = query

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'query': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit',
            'query': 'query'
        }

        return attributes
