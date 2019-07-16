class EmailNotificationWithStreamConditionsListQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(EmailNotificationWithStreamConditionsListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
