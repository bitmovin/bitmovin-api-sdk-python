
class Av1VideoConfigurationListQueryParams(dict):
    def __init__(self, offset: int = None, limit: int = None, *args, **kwargs):
        super(Av1VideoConfigurationListQueryParams, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit
