class Av1VideoConfigurationListQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(Av1VideoConfigurationListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
