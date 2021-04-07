# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.scale_filter import ScaleFilter
from bitmovin_api_sdk.encoding.filters.scale.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.filters.scale.scale_filter_list_query_params import ScaleFilterListQueryParams


class ScaleApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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
        # type: (ScaleFilter, dict) -> ScaleFilter
        """Create Scale Filter

        :param scale_filter: The Scale Filter to be created
        :type scale_filter: ScaleFilter, required
        :return: Scale Filter details
        :rtype: ScaleFilter
        """

        return self.api_client.post(
            '/encoding/filters/scale',
            scale_filter,
            type=ScaleFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Scale Filter

        :param filter_id: Id of the scale filter
        :type filter_id: string_types, required
        :return: Id of the Scale Filter.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/filters/scale/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> ScaleFilter
        """Scale Filter Details

        :param filter_id: Id of the scale filter
        :type filter_id: string_types, required
        :return: Scale Filter details
        :rtype: ScaleFilter
        """

        return self.api_client.get(
            '/encoding/filters/scale/{filter_id}',
            path_params={'filter_id': filter_id},
            type=ScaleFilter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (ScaleFilterListQueryParams, dict) -> ScaleFilter
        """List Scale Filters

        :param query_params: Query parameters
        :type query_params: ScaleFilterListQueryParams
        :return: List of Scale Filers
        :rtype: ScaleFilter
        """

        return self.api_client.get(
            '/encoding/filters/scale',
            query_params=query_params,
            pagination_response=True,
            type=ScaleFilter,
            **kwargs
        )
