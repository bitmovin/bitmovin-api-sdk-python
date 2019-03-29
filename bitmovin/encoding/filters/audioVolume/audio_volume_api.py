# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.audio_volume_filter import AudioVolumeFilter
from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.filters.audioVolume.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.filters.audioVolume.audio_volume_filter_list_query_params import AudioVolumeFilterListQueryParams


class AudioVolumeApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
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
        """Create Audio Volume Filter"""

        return self.api_client.post(
            '/encoding/filters/audio-volume',
            audio_volume_filter,
            type=AudioVolumeFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete Audio Volume Filter"""

        return self.api_client.delete(
            '/encoding/filters/audio-volume/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """Audio Volume Filter Details"""

        return self.api_client.get(
            '/encoding/filters/audio-volume/{filter_id}',
            path_params={'filter_id': filter_id},
            type=AudioVolumeFilter,
            **kwargs
        )

    def list(self, query_params: AudioVolumeFilterListQueryParams = None, **kwargs):
        """List Audio Volume Filters"""

        return self.api_client.get(
            '/encoding/filters/audio-volume',
            query_params=query_params,
            pagination_response=True,
            type=AudioVolumeFilter,
            **kwargs
        )
