from bitmovin_api_sdk.models import OutputType


class OutputListQueryParams(object):
    def __init__(self, offset=None, limit=None, name=None, sort=None, type_=None):
        # type: (int, int, string_types, string_types, OutputType) -> None
        super(OutputListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.name = name
        self.sort = sort
        self.type = type_

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'name': 'string_types',
            'sort': 'string_types',
            'type': 'OutputType'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit',
            'name': 'name',
            'sort': 'sort',
            'type': 'type'
        }

        return attributes
