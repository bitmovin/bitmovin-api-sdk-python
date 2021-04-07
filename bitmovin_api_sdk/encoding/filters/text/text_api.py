# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.text_filter import TextFilter
from bitmovin_api_sdk.encoding.filters.text.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.filters.text.text_filter_list_query_params import TextFilterListQueryParams


class TextApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(TextApi, self).__init__(
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

    def create(self, text_filter, **kwargs):
        # type: (TextFilter, dict) -> TextFilter
        """Create Text Filter

        :param text_filter: The Text Filter to be created
        :type text_filter: TextFilter, required
        :return: Text filter details
        :rtype: TextFilter
        """

        return self.api_client.post(
            '/encoding/filters/text',
            text_filter,
            type=TextFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Text Filter

        :param filter_id: Id of the Text Filter
        :type filter_id: string_types, required
        :return: Id of the Text Filter.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/filters/text/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> TextFilter
        """Text Filter Details

        :param filter_id: Id of the Text Filter
        :type filter_id: string_types, required
        :return: Text filter details
        :rtype: TextFilter
        """

        return self.api_client.get(
            '/encoding/filters/text/{filter_id}',
            path_params={'filter_id': filter_id},
            type=TextFilter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (TextFilterListQueryParams, dict) -> TextFilter
        """List Text Filters

        :param query_params: Query parameters
        :type query_params: TextFilterListQueryParams
        :return: List of Text Filters
        :rtype: TextFilter
        """

        return self.api_client.get(
            '/encoding/filters/text',
            query_params=query_params,
            pagination_response=True,
            type=TextFilter,
            **kwargs
        )
