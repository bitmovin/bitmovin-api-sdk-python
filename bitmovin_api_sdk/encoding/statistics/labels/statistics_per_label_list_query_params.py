class StatisticsPerLabelListQueryParams(dict):
    def __init__(self, offset=None, limit=None, labels=None):
        # type: (int, int, string_types) -> None
        super(StatisticsPerLabelListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.labels = labels
