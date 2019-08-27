from bitmovin_api_sdk.models import StreamMode


class MuxingListQueryParams(object):
    def __init__(self, offset=None, limit=None, stream_mode=None):
        # type: (int, int, StreamMode) -> None
        super(MuxingListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.stream_mode = stream_mode

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'stream_mode': 'StreamMode'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit',
            'stream_mode': 'streamMode'
        }

        return attributes
