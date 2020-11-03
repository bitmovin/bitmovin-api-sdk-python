from bitmovin_api_sdk.models import CloudRegion
from bitmovin_api_sdk.models import EncodingMode


class EncodingListQueryParams(object):
    def __init__(self, offset=None, limit=None, sort=None, type_=None, status=None, cloud_region=None, selected_cloud_region=None, encoder_version=None, selected_encoder_version=None, selected_encoding_mode=None, name=None, search=None, created_at_newer_than=None, created_at_older_than=None, started_at_newer_than=None, started_at_older_than=None):
        # type: (int, int, string_types, string_types, string_types, CloudRegion, CloudRegion, string_types, string_types, EncodingMode, string_types, string_types, datetime, datetime, datetime, datetime) -> None
        super(EncodingListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.sort = sort
        self.type = type_
        self.status = status
        self.cloud_region = cloud_region
        self.selected_cloud_region = selected_cloud_region
        self.encoder_version = encoder_version
        self.selected_encoder_version = selected_encoder_version
        self.selected_encoding_mode = selected_encoding_mode
        self.name = name
        self.search = search
        self.created_at_newer_than = created_at_newer_than
        self.created_at_older_than = created_at_older_than
        self.started_at_newer_than = started_at_newer_than
        self.started_at_older_than = started_at_older_than

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'sort': 'string_types',
            'type': 'string_types',
            'status': 'string_types',
            'cloud_region': 'CloudRegion',
            'selected_cloud_region': 'CloudRegion',
            'encoder_version': 'string_types',
            'selected_encoder_version': 'string_types',
            'selected_encoding_mode': 'EncodingMode',
            'name': 'string_types',
            'search': 'string_types',
            'created_at_newer_than': 'datetime',
            'created_at_older_than': 'datetime',
            'started_at_newer_than': 'datetime',
            'started_at_older_than': 'datetime'
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
            'cloud_region': 'cloudRegion',
            'selected_cloud_region': 'selectedCloudRegion',
            'encoder_version': 'encoderVersion',
            'selected_encoder_version': 'selectedEncoderVersion',
            'selected_encoding_mode': 'selectedEncodingMode',
            'name': 'name',
            'search': 'search',
            'created_at_newer_than': 'createdAtNewerThan',
            'created_at_older_than': 'createdAtOlderThan',
            'started_at_newer_than': 'startedAtNewerThan',
            'started_at_older_than': 'startedAtOlderThan'
        }

        return attributes
