
class DashMp4RepresentationListQueryParams(dict):
    def __init__(self, offset: int = None, limit: int = None, *args, **kwargs):
        super(DashMp4RepresentationListQueryParams, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit
