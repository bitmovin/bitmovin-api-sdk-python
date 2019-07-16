class DashFmp4RepresentationListQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(DashFmp4RepresentationListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
