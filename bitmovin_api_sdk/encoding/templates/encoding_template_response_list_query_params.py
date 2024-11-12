from bitmovin_api_sdk.models import EncodingTemplateType


class EncodingTemplateResponseListQueryParams(object):
    def __init__(self, offset=None, limit=None, type_=None):
        # type: (int, int, EncodingTemplateType) -> None
        super(EncodingTemplateResponseListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.type = type_

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'type': 'EncodingTemplateType'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit',
            'type': 'type'
        }

        return attributes
