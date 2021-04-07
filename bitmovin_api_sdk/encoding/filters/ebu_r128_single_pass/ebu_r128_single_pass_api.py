# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.ebu_r128_single_pass_filter import EbuR128SinglePassFilter
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.filters.ebu_r128_single_pass.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.filters.ebu_r128_single_pass.ebu_r128_single_pass_filter_list_query_params import EbuR128SinglePassFilterListQueryParams


class EbuR128SinglePassApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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
        # type: (EbuR128SinglePassFilter, dict) -> EbuR128SinglePassFilter
        """Create EBU R128 Single Pass Filter

        :param ebu_r128_single_pass_filter: The EBU R128 Single Pass Filter to be created
        :type ebu_r128_single_pass_filter: EbuR128SinglePassFilter, required
        :return: EBU R128 Single Pass Filter details
        :rtype: EbuR128SinglePassFilter
        """

        return self.api_client.post(
            '/encoding/filters/ebu-r128-single-pass',
            ebu_r128_single_pass_filter,
            type=EbuR128SinglePassFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete EBU R128 Single Pass Filter

        :param filter_id: Id of the EBU R128 Single Pass filter.
        :type filter_id: string_types, required
        :return: Id of the EBU R128 Single Pass filter.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/filters/ebu-r128-single-pass/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> EbuR128SinglePassFilter
        """EBU R128 Single Pass Filter Details

        :param filter_id: Id of the EBU R128 Single Pass filter.
        :type filter_id: string_types, required
        :return: EBU R128 Single Pass details
        :rtype: EbuR128SinglePassFilter
        """

        return self.api_client.get(
            '/encoding/filters/ebu-r128-single-pass/{filter_id}',
            path_params={'filter_id': filter_id},
            type=EbuR128SinglePassFilter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (EbuR128SinglePassFilterListQueryParams, dict) -> EbuR128SinglePassFilter
        """List EBU R128 Single Pass Filters

        :param query_params: Query parameters
        :type query_params: EbuR128SinglePassFilterListQueryParams
        :return: List of EBU R128 Single Pass Filters
        :rtype: EbuR128SinglePassFilter
        """

        return self.api_client.get(
            '/encoding/filters/ebu-r128-single-pass',
            query_params=query_params,
            pagination_response=True,
            type=EbuR128SinglePassFilter,
            **kwargs
        )
