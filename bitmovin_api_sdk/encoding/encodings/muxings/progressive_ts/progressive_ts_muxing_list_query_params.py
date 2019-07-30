class ProgressiveTsMuxingListQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(ProgressiveTsMuxingListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
