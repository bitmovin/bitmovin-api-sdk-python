from bitmovin_api_sdk.models import CloudRegion


class EncodingListQueryParams(dict):
    def __init__(self, offset=None, limit=None, sort=None, type_=None, status=None, cloud_region=None, encoder_version=None, name=None, search=None):
        # type: (int, int, string_types, string_types, string_types, CloudRegion, string_types, string_types, string_types) -> None
        super(EncodingListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.sort = sort
        self.type = type_
        self.status = status
        self.cloud_region = cloud_region
        self.encoder_version = encoder_version
        self.name = name
        self.search = search
