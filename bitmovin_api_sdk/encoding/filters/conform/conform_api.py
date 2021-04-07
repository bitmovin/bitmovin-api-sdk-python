# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.conform_filter import ConformFilter
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.filters.conform.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.filters.conform.conform_filter_list_query_params import ConformFilterListQueryParams


class ConformApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ConformApi, self).__init__(
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

    def create(self, conform_filter, **kwargs):
        # type: (ConformFilter, dict) -> ConformFilter
        """Create Conform Filter. Keeps all the frames of the input. The playback time of the output will be slower or faster.

        :param conform_filter: The Conform Filter to be created
        :type conform_filter: ConformFilter, required
        :return: Conform Filter details
        :rtype: ConformFilter
        """

        return self.api_client.post(
            '/encoding/filters/conform',
            conform_filter,
            type=ConformFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Conform Filter

        :param filter_id: Id of the conform filter
        :type filter_id: string_types, required
        :return: Id of the Conform Filter.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/filters/conform/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> ConformFilter
        """Conform Filter Details

        :param filter_id: Id of the conform filter
        :type filter_id: string_types, required
        :return: Conform Filter details
        :rtype: ConformFilter
        """

        return self.api_client.get(
            '/encoding/filters/conform/{filter_id}',
            path_params={'filter_id': filter_id},
            type=ConformFilter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (ConformFilterListQueryParams, dict) -> ConformFilter
        """List Conform Filters

        :param query_params: Query parameters
        :type query_params: ConformFilterListQueryParams
        :return: List of Conform Filters
        :rtype: ConformFilter
        """

        return self.api_client.get(
            '/encoding/filters/conform',
            query_params=query_params,
            pagination_response=True,
            type=ConformFilter,
            **kwargs
        )
