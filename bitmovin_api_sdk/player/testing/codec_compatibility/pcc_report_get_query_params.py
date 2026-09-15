class PccReportGetQueryParams(object):
    def __init__(self, include_prerelease=None, reported_only=None, hdr_only=None, codec=None, device=None):
        # type: (bool, bool, bool, string_types, string_types) -> None
        super(PccReportGetQueryParams, self).__init__()

        self.include_prerelease = include_prerelease
        self.reported_only = reported_only
        self.hdr_only = hdr_only
        self.codec = codec
        self.device = device

    @property
    def openapi_types(self):
        types = {
            'include_prerelease': 'bool',
            'reported_only': 'bool',
            'hdr_only': 'bool',
            'codec': 'string_types',
            'device': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'include_prerelease': 'includePrerelease',
            'reported_only': 'reportedOnly',
            'hdr_only': 'hdrOnly',
            'codec': 'codec',
            'device': 'device'
        }

        return attributes
