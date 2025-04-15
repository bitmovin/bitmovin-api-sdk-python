class LiveEncodingStatsEventListQueryParams(object):
    def __init__(self, offset=None, limit=None, sort_by_time=None):
        # type: (int, int, bool) -> None
        super(LiveEncodingStatsEventListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.sort_by_time = sort_by_time

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'sort_by_time': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit',
            'sort_by_time': 'sortByTime'
        }

        return attributes
