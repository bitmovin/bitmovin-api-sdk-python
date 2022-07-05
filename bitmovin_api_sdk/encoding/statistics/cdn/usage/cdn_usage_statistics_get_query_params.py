class CdnUsageStatisticsGetQueryParams(object):
    def __init__(self, from_=None, to=None):
        # type: (datetime, datetime) -> None
        super(CdnUsageStatisticsGetQueryParams, self).__init__()

        self.from_ = from_
        self.to = to

    @property
    def openapi_types(self):
        types = {
            'from_': 'datetime',
            'to': 'datetime'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'from_': 'from',
            'to': 'to'
        }

        return attributes
