class Id3TagListQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(Id3TagListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
