class Fmp4MuxingListQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(Fmp4MuxingListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
