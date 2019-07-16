class H264VideoConfigurationListQueryParams(dict):
    def __init__(self, offset=None, limit=None, name=None):
        # type: (int, int, string_types) -> None
        super(H264VideoConfigurationListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.name = name
