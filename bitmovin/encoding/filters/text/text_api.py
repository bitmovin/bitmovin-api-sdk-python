# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.text_filter import TextFilter
from bitmovin.encoding.filters.text.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.filters.text.text_filter_list_query_params import TextFilterListQueryParams


class TextApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(TextApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, text_filter, **kwargs):
        """Create Text Filter"""

        return self.api_client.post(
            '/encoding/filters/text',
            text_filter,
            type=TextFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete Text Filter"""

        return self.api_client.delete(
            '/encoding/filters/text/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """Text Filter Details"""

        return self.api_client.get(
            '/encoding/filters/text/{filter_id}',
            path_params={'filter_id': filter_id},
            type=TextFilter,
            **kwargs
        )

    def list(self, query_params: TextFilterListQueryParams = None, **kwargs):
        """List Text Filters"""

        return self.api_client.get(
            '/encoding/filters/text',
            query_params=query_params,
            pagination_response=True,
            type=TextFilter,
            **kwargs
        )
