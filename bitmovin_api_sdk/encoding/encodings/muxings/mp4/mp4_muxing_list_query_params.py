class Mp4MuxingListQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(Mp4MuxingListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
