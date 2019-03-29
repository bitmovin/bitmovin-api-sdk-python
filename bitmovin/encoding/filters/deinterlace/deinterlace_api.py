# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.deinterlace_filter import DeinterlaceFilter
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.filters.deinterlace.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.filters.deinterlace.deinterlace_filter_list_query_params import DeinterlaceFilterListQueryParams


class DeinterlaceApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(DeinterlaceApi, self).__init__(
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

    def create(self, deinterlace_filter, **kwargs):
        """Create Deinterlace Filter"""

        return self.api_client.post(
            '/encoding/filters/deinterlace',
            deinterlace_filter,
            type=DeinterlaceFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete Deinterlace Filter"""

        return self.api_client.delete(
            '/encoding/filters/deinterlace/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """Deinterlace Filter Details"""

        return self.api_client.get(
            '/encoding/filters/deinterlace/{filter_id}',
            path_params={'filter_id': filter_id},
            type=DeinterlaceFilter,
            **kwargs
        )

    def list(self, query_params: DeinterlaceFilterListQueryParams = None, **kwargs):
        """List Deinterlace Filters"""

        return self.api_client.get(
            '/encoding/filters/deinterlace',
            query_params=query_params,
            pagination_response=True,
            type=DeinterlaceFilter,
            **kwargs
        )
