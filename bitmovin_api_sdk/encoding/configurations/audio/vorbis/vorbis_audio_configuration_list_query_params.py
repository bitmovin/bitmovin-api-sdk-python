class VorbisAudioConfigurationListQueryParams(dict):
    def __init__(self, offset=None, limit=None, name=None):
        # type: (int, int, string_types) -> None
        super(VorbisAudioConfigurationListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.name = name
