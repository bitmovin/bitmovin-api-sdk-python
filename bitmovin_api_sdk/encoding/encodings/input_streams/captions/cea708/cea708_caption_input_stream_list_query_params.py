class Cea708CaptionInputStreamListQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(Cea708CaptionInputStreamListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
