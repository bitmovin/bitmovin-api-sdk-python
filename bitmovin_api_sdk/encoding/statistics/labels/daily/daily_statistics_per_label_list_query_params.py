class DailyStatisticsPerLabelListQueryParams(dict):
    def __init__(self, offset=None, limit=None, labels=None):
        # type: (int, int, string_types) -> None
        super(DailyStatisticsPerLabelListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.labels = labels
