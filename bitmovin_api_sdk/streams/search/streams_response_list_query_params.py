from bitmovin_api_sdk.models import StreamsType
from bitmovin_api_sdk.models import StreamsVideoStatus


class StreamsResponseListQueryParams(object):
    def __init__(self, offset=None, limit=None, query=None, type_=None, status=None, created_before=None, created_after=None, signed=None, domain_restricted=None):
        # type: (int, int, string_types, StreamsType, StreamsVideoStatus, string_types, string_types, bool, bool) -> None
        super(StreamsResponseListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.query = query
        self.type = type_
        self.status = status
        self.created_before = created_before
        self.created_after = created_after
        self.signed = signed
        self.domain_restricted = domain_restricted

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'query': 'string_types',
            'type': 'StreamsType',
            'status': 'StreamsVideoStatus',
            'created_before': 'string_types',
            'created_after': 'string_types',
            'signed': 'bool',
            'domain_restricted': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit',
            'query': 'query',
            'type': 'type',
            'status': 'status',
            'created_before': 'createdBefore',
            'created_after': 'createdAfter',
            'signed': 'signed',
            'domain_restricted': 'domainRestricted'
        }

        return attributes
