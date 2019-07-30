class UdpMulticastInputListQueryParams(dict):
    def __init__(self, offset=None, limit=None, name=None):
        # type: (int, int, string_types) -> None
        super(UdpMulticastInputListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.name = name
