class ScheduledInsertableContentListQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(ScheduledInsertableContentListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
