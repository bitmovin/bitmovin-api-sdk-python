# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.audio_mix_filter import AudioMixFilter
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.filters.audio_mix.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.filters.audio_mix.audio_mix_filter_list_query_params import AudioMixFilterListQueryParams


class AudioMixApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AudioMixApi, self).__init__(
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

    def create(self, audio_mix_filter, **kwargs):
        # type: (AudioMixFilter, dict) -> AudioMixFilter
        """Create Audio Mix Filter

        :param audio_mix_filter: The Audio Mix Filter to be created
        :type audio_mix_filter: AudioMixFilter, required
        :return: Audio Mix configuration
        :rtype: AudioMixFilter
        """

        return self.api_client.post(
            '/encoding/filters/audio-mix',
            audio_mix_filter,
            type=AudioMixFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Audio Mix Filter

        :param filter_id: Id of the Audio Mix configuration.
        :type filter_id: string_types, required
        :return: Id of the Audio Mix configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/filters/audio-mix/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> AudioMixFilter
        """Audio Mix Filter Details

        :param filter_id: Id of the Audio Mix configuration.
        :type filter_id: string_types, required
        :return: Audio Mix configuration
        :rtype: AudioMixFilter
        """

        return self.api_client.get(
            '/encoding/filters/audio-mix/{filter_id}',
            path_params={'filter_id': filter_id},
            type=AudioMixFilter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AudioMixFilterListQueryParams, dict) -> AudioMixFilter
        """List Audio Mix Filters

        :param query_params: Query parameters
        :type query_params: AudioMixFilterListQueryParams
        :return: List of Audio Mix configurations
        :rtype: AudioMixFilter
        """

        return self.api_client.get(
            '/encoding/filters/audio-mix',
            query_params=query_params,
            pagination_response=True,
            type=AudioMixFilter,
            **kwargs
        )
