from bitmovin_api_sdk.models import StreamMode


class MuxingListQueryParams(dict):
    def __init__(self, offset=None, limit=None, stream_mode=None):
        # type: (int, int, StreamMode) -> None
        super(MuxingListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.stream_mode = stream_mode
