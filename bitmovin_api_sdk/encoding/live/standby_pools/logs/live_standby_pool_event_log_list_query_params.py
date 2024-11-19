class LiveStandbyPoolEventLogListQueryParams(object):
    def __init__(self, offset=None, limit=None, sort=None, event_type=None):
        # type: (int, int, string_types, string_types) -> None
        super(LiveStandbyPoolEventLogListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.sort = sort
        self.event_type = event_type

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'sort': 'string_types',
            'event_type': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit',
            'sort': 'sort',
            'event_type': 'eventType'
        }

        return attributes
