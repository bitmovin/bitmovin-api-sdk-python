class SmoothStreamingRepresentationListQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(SmoothStreamingRepresentationListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
