# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.rotate_filter import RotateFilter
from bitmovin_api_sdk.encoding.filters.rotate.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.filters.rotate.rotate_filter_list_query_params import RotateFilterListQueryParams


class RotateApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(RotateApi, self).__init__(
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

    def create(self, rotate_filter, **kwargs):
        # type: (RotateFilter, dict) -> RotateFilter
        """Create Rotate Filter

        :param rotate_filter: The Rotate Filter to be created
        :type rotate_filter: RotateFilter, required
        :return: Rotate Filter details
        :rtype: RotateFilter
        """

        return self.api_client.post(
            '/encoding/filters/rotate',
            rotate_filter,
            type=RotateFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Rotate Filter

        :param filter_id: Id of the Rotate Filter.
        :type filter_id: string_types, required
        :return: Id of the Rotate Filter
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/filters/rotate/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> RotateFilter
        """Rotate Filter Details

        :param filter_id: Id of the Rotate Filter.
        :type filter_id: string_types, required
        :return: Rotate Configuration
        :rtype: RotateFilter
        """

        return self.api_client.get(
            '/encoding/filters/rotate/{filter_id}',
            path_params={'filter_id': filter_id},
            type=RotateFilter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (RotateFilterListQueryParams, dict) -> RotateFilter
        """List Rotate Filters

        :param query_params: Query parameters
        :type query_params: RotateFilterListQueryParams
        :return: List of Rotate Filters
        :rtype: RotateFilter
        """

        return self.api_client.get(
            '/encoding/filters/rotate',
            query_params=query_params,
            pagination_response=True,
            type=RotateFilter,
            **kwargs
        )
