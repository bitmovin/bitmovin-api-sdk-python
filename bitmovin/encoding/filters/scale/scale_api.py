# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.scale_filter import ScaleFilter
from bitmovin.encoding.filters.scale.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.filters.scale.scale_filter_list_query_params import ScaleFilterListQueryParams


class ScaleApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ScaleApi, self).__init__(
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

    def create(self, scale_filter, **kwargs):
        """Create Scale Filter"""

        return self.api_client.post(
            '/encoding/filters/scale',
            scale_filter,
            type=ScaleFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete Scale Filter"""

        return self.api_client.delete(
            '/encoding/filters/scale/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """Scale Filter Details"""

        return self.api_client.get(
            '/encoding/filters/scale/{filter_id}',
            path_params={'filter_id': filter_id},
            type=ScaleFilter,
            **kwargs
        )

    def list(self, query_params: ScaleFilterListQueryParams = None, **kwargs):
        """List Scale Filters"""

        return self.api_client.get(
            '/encoding/filters/scale',
            query_params=query_params,
            pagination_response=True,
            type=ScaleFilter,
            **kwargs
        )
