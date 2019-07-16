class NotificationStateEntryListQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(NotificationStateEntryListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
