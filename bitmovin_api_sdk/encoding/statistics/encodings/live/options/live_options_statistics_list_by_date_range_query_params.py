class LiveOptionsStatisticsListByDateRangeQueryParams(object):
    def __init__(self, from_=None, to=None, offset=None, limit=None):
        # type: (date, date, int, int) -> None
        super(LiveOptionsStatisticsListByDateRangeQueryParams, self).__init__()

        self.from_ = from_
        self.to = to
        self.offset = offset
        self.limit = limit

    @property
    def openapi_types(self):
        types = {
            'from_': 'date',
            'to': 'date',
            'offset': 'int',
            'limit': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'from_': 'from',
            'to': 'to',
            'offset': 'offset',
            'limit': 'limit'
        }

        return attributes
