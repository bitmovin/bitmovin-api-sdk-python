# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.audio_media_info import AudioMediaInfo
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.manifests.hls.media.audio.audio_media_info_list_query_params import AudioMediaInfoListQueryParams


class AudioApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AudioApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, audio_media_info, **kwargs):
        # type: (string_types, AudioMediaInfo, dict) -> AudioMediaInfo
        """Add Audio Media

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param audio_media_info: The Audio Media to be added
        :type audio_media_info: AudioMediaInfo, required
        :return: Audio media details
        :rtype: AudioMediaInfo
        """

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/media/audio',
            audio_media_info,
            path_params={'manifest_id': manifest_id},
            type=AudioMediaInfo,
            **kwargs
        )

    def delete(self, manifest_id, media_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Audio Media

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param media_id: Id of the audio media.
        :type media_id: string_types, required
        :return: Id of the audio media
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}/media/audio/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, media_id, **kwargs):
        # type: (string_types, string_types, dict) -> AudioMediaInfo
        """Audio Media Details

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param media_id: Id of the audio media.
        :type media_id: string_types, required
        :return: Audio media details
        :rtype: AudioMediaInfo
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/audio/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=AudioMediaInfo,
            **kwargs
        )

    def list(self, manifest_id, query_params=None, **kwargs):
        # type: (string_types, AudioMediaInfoListQueryParams, dict) -> AudioMediaInfo
        """List all Audio Media

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param query_params: Query parameters
        :type query_params: AudioMediaInfoListQueryParams
        :return: Audio media
        :rtype: AudioMediaInfo
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/audio',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=AudioMediaInfo,
            **kwargs
        )
