# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.denoise_hqdn3d_filter import DenoiseHqdn3dFilter
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.filters.denoise_hqdn3d.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.filters.denoise_hqdn3d.denoise_hqdn3d_filter_list_query_params import DenoiseHqdn3dFilterListQueryParams


class DenoiseHqdn3dApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DenoiseHqdn3dApi, self).__init__(
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

    def create(self, denoise_hqdn3d_filter, **kwargs):
        # type: (DenoiseHqdn3dFilter, dict) -> DenoiseHqdn3dFilter
        """Create Denoise hqdn3d Filter

        :param denoise_hqdn3d_filter: The Denoise hqdn3d Filter to be created
        :type denoise_hqdn3d_filter: DenoiseHqdn3dFilter, required
        :return: Denoise hqdn3d details
        :rtype: DenoiseHqdn3dFilter
        """

        return self.api_client.post(
            '/encoding/filters/denoise-hqdn3d',
            denoise_hqdn3d_filter,
            type=DenoiseHqdn3dFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Denoise hqdn3d Filter

        :param filter_id: Id of the denoise hqdn3d filter
        :type filter_id: string_types, required
        :return: Id of the watermark.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/filters/denoise-hqdn3d/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> DenoiseHqdn3dFilter
        """Denoise hqdn3d Filter Details

        :param filter_id: Id of the denoise hqdn3d filter
        :type filter_id: string_types, required
        :return: Denoise hqdn3d details
        :rtype: DenoiseHqdn3dFilter
        """

        return self.api_client.get(
            '/encoding/filters/denoise-hqdn3d/{filter_id}',
            path_params={'filter_id': filter_id},
            type=DenoiseHqdn3dFilter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (DenoiseHqdn3dFilterListQueryParams, dict) -> DenoiseHqdn3dFilter
        """List Denoise hqdn3d Filters

        :param query_params: Query parameters
        :type query_params: DenoiseHqdn3dFilterListQueryParams
        :return: List of denoise hqdn3d ids
        :rtype: DenoiseHqdn3dFilter
        """

        return self.api_client.get(
            '/encoding/filters/denoise-hqdn3d',
            query_params=query_params,
            pagination_response=True,
            type=DenoiseHqdn3dFilter,
            **kwargs
        )
