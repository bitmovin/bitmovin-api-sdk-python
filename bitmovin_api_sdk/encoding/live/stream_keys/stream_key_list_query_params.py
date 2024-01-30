class StreamKeyListQueryParams(object):
    def __init__(self, offset=None, limit=None, sort=None, type_=None, status=None, assigned_ingest_point_id=None, assigned_encoding_id=None):
        # type: (int, int, string_types, string_types, string_types, string_types, string_types) -> None
        super(StreamKeyListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.sort = sort
        self.type = type_
        self.status = status
        self.assigned_ingest_point_id = assigned_ingest_point_id
        self.assigned_encoding_id = assigned_encoding_id

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'sort': 'string_types',
            'type': 'string_types',
            'status': 'string_types',
            'assigned_ingest_point_id': 'string_types',
            'assigned_encoding_id': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit',
            'sort': 'sort',
            'type': 'type',
            'status': 'status',
            'assigned_ingest_point_id': 'assignedIngestPointId',
            'assigned_encoding_id': 'assignedEncodingId'
        }

        return attributes
