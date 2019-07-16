class CencDrmListQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (string_types, string_types) -> None
        super(CencDrmListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
