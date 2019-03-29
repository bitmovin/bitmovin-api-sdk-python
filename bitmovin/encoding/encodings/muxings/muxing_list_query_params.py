from bitmovin.models import StreamMode

class MuxingListQueryParams(dict):
    def __init__(self, offset: int = None, limit: int = None, stream_mode: StreamMode = None, *args, **kwargs):
        super(MuxingListQueryParams, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit
        self.stream_mode = stream_mode
