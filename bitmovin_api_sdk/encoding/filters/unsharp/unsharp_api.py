# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.unsharp_filter import UnsharpFilter
from bitmovin_api_sdk.encoding.filters.unsharp.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.filters.unsharp.unsharp_filter_list_query_params import UnsharpFilterListQueryParams


class UnsharpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(UnsharpApi, self).__init__(
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

    def create(self, unsharp_filter, **kwargs):
        # type: (UnsharpFilter, dict) -> UnsharpFilter
        """Create Unsharp Filter

        :param unsharp_filter: The Unsharp Filter to be created
        :type unsharp_filter: UnsharpFilter, required
        :return: Unsharp Filter details
        :rtype: UnsharpFilter
        """

        return self.api_client.post(
            '/encoding/filters/unsharp',
            unsharp_filter,
            type=UnsharpFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Unsharp Filter

        :param filter_id: Id of the unsharp filter
        :type filter_id: string_types, required
        :return: Id of the unsharp filter.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/filters/unsharp/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> UnsharpFilter
        """Unsharp Filter Details

        :param filter_id: Id of the unsharp filter
        :type filter_id: string_types, required
        :return: Unsharp Filter details
        :rtype: UnsharpFilter
        """

        return self.api_client.get(
            '/encoding/filters/unsharp/{filter_id}',
            path_params={'filter_id': filter_id},
            type=UnsharpFilter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (UnsharpFilterListQueryParams, dict) -> UnsharpFilter
        """List Unsharp Filters

        :param query_params: Query parameters
        :type query_params: UnsharpFilterListQueryParams
        :return: List of unsharp ids
        :rtype: UnsharpFilter
        """

        return self.api_client.get(
            '/encoding/filters/unsharp',
            query_params=query_params,
            pagination_response=True,
            type=UnsharpFilter,
            **kwargs
        )
