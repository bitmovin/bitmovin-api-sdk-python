class HeAacV1AudioConfigurationListQueryParams(dict):
    def __init__(self, offset=None, limit=None, name=None):
        # type: (int, int, string_types) -> None
        super(HeAacV1AudioConfigurationListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.name = name
