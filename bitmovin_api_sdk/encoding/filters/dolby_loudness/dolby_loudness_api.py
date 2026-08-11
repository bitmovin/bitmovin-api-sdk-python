# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.dolby_loudness_filter import DolbyLoudnessFilter
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.filters.dolby_loudness.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.filters.dolby_loudness.dolby_loudness_filter_list_query_params import DolbyLoudnessFilterListQueryParams


class DolbyLoudnessApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DolbyLoudnessApi, self).__init__(
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

    def create(self, dolby_loudness_filter, **kwargs):
        # type: (DolbyLoudnessFilter, dict) -> DolbyLoudnessFilter
        """Create Dolby Loudness Filter

        :param dolby_loudness_filter: The Dolby Loudness Filter to be created
        :type dolby_loudness_filter: DolbyLoudnessFilter, required
        :return: Dolby Loudness Filter details
        :rtype: DolbyLoudnessFilter
        """

        return self.api_client.post(
            '/encoding/filters/dolby-loudness',
            dolby_loudness_filter,
            type=DolbyLoudnessFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Dolby Loudness Filter

        :param filter_id: Id of the Dolby Loudness filter.
        :type filter_id: string_types, required
        :return: Id of the Dolby Loudness filter.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/filters/dolby-loudness/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> DolbyLoudnessFilter
        """Get Dolby Loudness Filter details

        :param filter_id: Id of the Dolby Loudness filter.
        :type filter_id: string_types, required
        :return: Dolby Loudness details
        :rtype: DolbyLoudnessFilter
        """

        return self.api_client.get(
            '/encoding/filters/dolby-loudness/{filter_id}',
            path_params={'filter_id': filter_id},
            type=DolbyLoudnessFilter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (DolbyLoudnessFilterListQueryParams, dict) -> DolbyLoudnessFilter
        """List Dolby Loudness Filters

        :param query_params: Query parameters
        :type query_params: DolbyLoudnessFilterListQueryParams
        :return: List of Dolby Loudness Filters
        :rtype: DolbyLoudnessFilter
        """

        return self.api_client.get(
            '/encoding/filters/dolby-loudness',
            query_params=query_params,
            pagination_response=True,
            type=DolbyLoudnessFilter,
            **kwargs
        )
