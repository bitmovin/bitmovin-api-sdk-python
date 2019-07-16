class HlsManifestListQueryParams(dict):
    def __init__(self, offset=None, limit=None, encoding_id=None):
        # type: (int, int, string_types) -> None
        super(HlsManifestListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.encoding_id = encoding_id
