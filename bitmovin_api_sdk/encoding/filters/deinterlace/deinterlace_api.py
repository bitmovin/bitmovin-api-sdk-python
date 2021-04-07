# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.deinterlace_filter import DeinterlaceFilter
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.filters.deinterlace.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.filters.deinterlace.deinterlace_filter_list_query_params import DeinterlaceFilterListQueryParams


class DeinterlaceApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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
        # type: (DeinterlaceFilter, dict) -> DeinterlaceFilter
        """Create Deinterlace Filter

        :param deinterlace_filter: The Deinterlace Filter to be created
        :type deinterlace_filter: DeinterlaceFilter, required
        :return: Deinterlace Filter details
        :rtype: DeinterlaceFilter
        """

        return self.api_client.post(
            '/encoding/filters/deinterlace',
            deinterlace_filter,
            type=DeinterlaceFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Deinterlace Filter

        :param filter_id: Id of the Deinterlace Filter
        :type filter_id: string_types, required
        :return: Id of the Deinterlace Filter.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/filters/deinterlace/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> DeinterlaceFilter
        """Deinterlace Filter Details

        :param filter_id: Id of the Deinterlace Filter
        :type filter_id: string_types, required
        :return: Deinterlace Filter details
        :rtype: DeinterlaceFilter
        """

        return self.api_client.get(
            '/encoding/filters/deinterlace/{filter_id}',
            path_params={'filter_id': filter_id},
            type=DeinterlaceFilter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (DeinterlaceFilterListQueryParams, dict) -> DeinterlaceFilter
        """List Deinterlace Filters

        :param query_params: Query parameters
        :type query_params: DeinterlaceFilterListQueryParams
        :return: List of Deinterlace Filters
        :rtype: DeinterlaceFilter
        """

        return self.api_client.get(
            '/encoding/filters/deinterlace',
            query_params=query_params,
            pagination_response=True,
            type=DeinterlaceFilter,
            **kwargs
        )
