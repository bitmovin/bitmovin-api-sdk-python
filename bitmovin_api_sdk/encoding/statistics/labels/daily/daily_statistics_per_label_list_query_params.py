class DailyStatisticsPerLabelListQueryParams(object):
    def __init__(self, offset=None, limit=None, labels=None):
        # type: (int, int, string_types) -> None
        super(DailyStatisticsPerLabelListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.labels = labels

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'labels': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit',
            'labels': 'labels'
        }

        return attributes
