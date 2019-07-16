class Mp3MuxingListQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(Mp3MuxingListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
