# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.audio_volume_filter import AudioVolumeFilter
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.filters.audio_volume.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.filters.audio_volume.audio_volume_filter_list_query_params import AudioVolumeFilterListQueryParams


class AudioVolumeApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AudioVolumeApi, self).__init__(
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

    def create(self, audio_volume_filter, **kwargs):
        # type: (AudioVolumeFilter, dict) -> AudioVolumeFilter
        """Create Audio Volume Filter

        :param audio_volume_filter: The Audio Volume Filter to be created
        :type audio_volume_filter: AudioVolumeFilter, required
        :return: Audio volume details
        :rtype: AudioVolumeFilter
        """

        return self.api_client.post(
            '/encoding/filters/audio-volume',
            audio_volume_filter,
            type=AudioVolumeFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Audio Volume Filter

        :param filter_id: Id of the Audio Volume Filter.
        :type filter_id: string_types, required
        :return: Id of the Audio volume.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/filters/audio-volume/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> AudioVolumeFilter
        """Audio Volume Filter Details

        :param filter_id: Id of the Audio Volume Filter.
        :type filter_id: string_types, required
        :return: Audio volume details
        :rtype: AudioVolumeFilter
        """

        return self.api_client.get(
            '/encoding/filters/audio-volume/{filter_id}',
            path_params={'filter_id': filter_id},
            type=AudioVolumeFilter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AudioVolumeFilterListQueryParams, dict) -> AudioVolumeFilter
        """List Audio Volume Filters

        :param query_params: Query parameters
        :type query_params: AudioVolumeFilterListQueryParams
        :return: List of Audio Volume Filters
        :rtype: AudioVolumeFilter
        """

        return self.api_client.get(
            '/encoding/filters/audio-volume',
            query_params=query_params,
            pagination_response=True,
            type=AudioVolumeFilter,
            **kwargs
        )
