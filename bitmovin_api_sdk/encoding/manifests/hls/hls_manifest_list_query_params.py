class HlsManifestListQueryParams(object):
    def __init__(self, offset=None, limit=None, sort=None, encoding_id=None):
        # type: (int, int, string_types, string_types) -> None
        super(HlsManifestListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.sort = sort
        self.encoding_id = encoding_id

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'sort': 'string_types',
            'encoding_id': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit',
            'sort': 'sort',
            'encoding_id': 'encodingId'
        }

        return attributes
