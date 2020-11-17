class PrewarmedEncoderPoolListQueryParams(object):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(PrewarmedEncoderPoolListQueryParams, self).__init__()

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
