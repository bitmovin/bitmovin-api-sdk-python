class HlsManifestListQueryParams(object):
    def __init__(self, offset=None, limit=None, encoding_id=None):
        # type: (int, int, string_types) -> None
        super(HlsManifestListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.encoding_id = encoding_id

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'encoding_id': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit',
            'encoding_id': 'encodingId'
        }

        return attributes
