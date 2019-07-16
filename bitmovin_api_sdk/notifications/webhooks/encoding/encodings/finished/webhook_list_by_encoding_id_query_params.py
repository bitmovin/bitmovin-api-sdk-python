class WebhookListByEncodingIdQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(WebhookListByEncodingIdQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
