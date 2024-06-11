# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.azure_speech_to_captions_filter import AzureSpeechToCaptionsFilter
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.filters.azure_speech_to_captions.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.filters.azure_speech_to_captions.azure_speech_to_captions_filter_list_query_params import AzureSpeechToCaptionsFilterListQueryParams


class AzureSpeechToCaptionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AzureSpeechToCaptionsApi, self).__init__(
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

    def create(self, azure_speech_to_captions_filter, **kwargs):
        # type: (AzureSpeechToCaptionsFilter, dict) -> AzureSpeechToCaptionsFilter
        """Create Azure Speech to captions Filter

        :param azure_speech_to_captions_filter: The Azure Speech to captions Filter to be created
        :type azure_speech_to_captions_filter: AzureSpeechToCaptionsFilter, required
        :return: Azure Speech to captions details
        :rtype: AzureSpeechToCaptionsFilter
        """

        return self.api_client.post(
            '/encoding/filters/azure-speech-to-captions',
            azure_speech_to_captions_filter,
            type=AzureSpeechToCaptionsFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Azure Speech to captions Filter

        :param filter_id: Id of the Azure Speech to captions Filter.
        :type filter_id: string_types, required
        :return: Id of the Azure Speech to captions filter.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/filters/azure-speech-to-captions/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> AzureSpeechToCaptionsFilter
        """Azure Speech to captions Filter details

        :param filter_id: Id of the Azure Speech to captions Filter.
        :type filter_id: string_types, required
        :return: Azure Speech to captions filter details
        :rtype: AzureSpeechToCaptionsFilter
        """

        return self.api_client.get(
            '/encoding/filters/azure-speech-to-captions/{filter_id}',
            path_params={'filter_id': filter_id},
            type=AzureSpeechToCaptionsFilter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AzureSpeechToCaptionsFilterListQueryParams, dict) -> AzureSpeechToCaptionsFilter
        """List Azure Speech to captions Filters

        :param query_params: Query parameters
        :type query_params: AzureSpeechToCaptionsFilterListQueryParams
        :return: List of Azure Speech to captions Filters
        :rtype: AzureSpeechToCaptionsFilter
        """

        return self.api_client.get(
            '/encoding/filters/azure-speech-to-captions',
            query_params=query_params,
            pagination_response=True,
            type=AzureSpeechToCaptionsFilter,
            **kwargs
        )
