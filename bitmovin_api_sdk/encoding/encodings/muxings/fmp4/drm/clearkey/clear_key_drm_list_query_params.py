class ClearKeyDrmListQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(ClearKeyDrmListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
