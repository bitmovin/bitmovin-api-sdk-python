from bitmovin_api_sdk.models import SceneAnalysisListSort


class SceneAnalysisListItemListQueryParams(object):
    def __init__(self, offset=None, limit=None, search_text=None, sort=None, created_at_from=None, created_at_to=None):
        # type: (int, int, string_types, SceneAnalysisListSort, datetime, datetime) -> None
        super(SceneAnalysisListItemListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.search_text = search_text
        self.sort = sort
        self.created_at_from = created_at_from
        self.created_at_to = created_at_to

    @property
    def openapi_types(self):
        types = {
            'offset': 'int',
            'limit': 'int',
            'search_text': 'string_types',
            'sort': 'SceneAnalysisListSort',
            'created_at_from': 'datetime',
            'created_at_to': 'datetime'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'limit': 'limit',
            'search_text': 'searchText',
            'sort': 'sort',
            'created_at_from': 'createdAtFrom',
            'created_at_to': 'createdAtTo'
        }

        return attributes
