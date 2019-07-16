# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.crop_filter import CropFilter
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.filters.crop.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.filters.crop.crop_filter_list_query_params import CropFilterListQueryParams


class CropApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(CropApi, self).__init__(
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

    def create(self, crop_filter, **kwargs):
        # type: (CropFilter, dict) -> CropFilter
        """Create Crop Filter

        :param crop_filter: The Crop Filter to be created
        :type crop_filter: CropFilter, required
        :return: Crop details
        :rtype: CropFilter
        """

        return self.api_client.post(
            '/encoding/filters/crop',
            crop_filter,
            type=CropFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Crop Filter

        :param filter_id: Id of the Crop configuration.
        :type filter_id: string_types, required
        :return:
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/filters/crop/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> CropFilter
        """Crop Filter Details

        :param filter_id: Id of the Crop configuration.
        :type filter_id: string_types, required
        :return: Crop details
        :rtype: CropFilter
        """

        return self.api_client.get(
            '/encoding/filters/crop/{filter_id}',
            path_params={'filter_id': filter_id},
            type=CropFilter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (CropFilterListQueryParams, dict) -> CropFilter
        """List Crop Filters

        :param query_params: Query parameters
        :type query_params: CropFilterListQueryParams
        :return: List of watermark ids
        :rtype: CropFilter
        """

        return self.api_client.get(
            '/encoding/filters/crop',
            query_params=query_params,
            pagination_response=True,
            type=CropFilter,
            **kwargs
        )
