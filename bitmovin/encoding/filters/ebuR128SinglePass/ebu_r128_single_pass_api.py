# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.ebu_r128_single_pass_filter import EbuR128SinglePassFilter
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.filters.ebuR128SinglePass.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.filters.ebuR128SinglePass.ebu_r128_single_pass_filter_list_query_params import EbuR128SinglePassFilterListQueryParams


class EbuR128SinglePassApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(EbuR128SinglePassApi, self).__init__(
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

    def create(self, ebu_r128_single_pass_filter, **kwargs):
        """Create EBU R128 Single Pass Filter"""

        return self.api_client.post(
            '/encoding/filters/ebu-r128-single-pass',
            ebu_r128_single_pass_filter,
            type=EbuR128SinglePassFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete EBU R128 Single Pass Filter"""

        return self.api_client.delete(
            '/encoding/filters/ebu-r128-single-pass/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """EBU R128 Single Pass Filter Details"""

        return self.api_client.get(
            '/encoding/filters/ebu-r128-single-pass/{filter_id}',
            path_params={'filter_id': filter_id},
            type=EbuR128SinglePassFilter,
            **kwargs
        )

    def list(self, query_params: EbuR128SinglePassFilterListQueryParams = None, **kwargs):
        """List EBU R128 Single Pass Filters"""

        return self.api_client.get(
            '/encoding/filters/ebu-r128-single-pass',
            query_params=query_params,
            pagination_response=True,
            type=EbuR128SinglePassFilter,
            **kwargs
        )
