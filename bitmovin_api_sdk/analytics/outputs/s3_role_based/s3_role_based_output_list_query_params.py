class S3RoleBasedOutputListQueryParams(dict):
    def __init__(self, offset=None, limit=None, name=None):
        # type: (int, int, string_types) -> None
        super(S3RoleBasedOutputListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.name = name
