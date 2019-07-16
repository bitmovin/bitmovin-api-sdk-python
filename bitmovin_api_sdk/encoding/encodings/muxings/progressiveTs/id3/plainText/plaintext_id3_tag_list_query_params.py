class PlaintextId3TagListQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(PlaintextId3TagListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
