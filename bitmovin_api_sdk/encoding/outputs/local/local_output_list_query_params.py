class LocalOutputListQueryParams(dict):
    def __init__(self, offset=None, limit=None, name=None):
        # type: (int, int, string_types) -> None
        super(LocalOutputListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.name = name
