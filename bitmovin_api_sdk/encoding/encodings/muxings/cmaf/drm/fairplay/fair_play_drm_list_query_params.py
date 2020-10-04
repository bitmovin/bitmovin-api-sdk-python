class FairPlayDrmListQueryParams(object):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(FairPlayDrmListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit'
        }

        return attributes
