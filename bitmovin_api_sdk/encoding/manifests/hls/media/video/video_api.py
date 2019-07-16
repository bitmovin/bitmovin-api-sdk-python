# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.standard_media_info import StandardMediaInfo
from bitmovin_api_sdk.models.video_media_info import VideoMediaInfo
from bitmovin_api_sdk.encoding.manifests.hls.media.video.video_media_info_list_query_params import VideoMediaInfoListQueryParams


class VideoApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(VideoApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, video_media_info, **kwargs):
        # type: (string_types, VideoMediaInfo, dict) -> VideoMediaInfo
        """Add Video Media

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param video_media_info: The Video Media to be added
        :type video_media_info: VideoMediaInfo, required
        :return: Video media details
        :rtype: VideoMediaInfo
        """

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/media/video',
            video_media_info,
            path_params={'manifest_id': manifest_id},
            type=VideoMediaInfo,
            **kwargs
        )

    def delete(self, manifest_id, media_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Video Media

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param media_id: Id of the video media.
        :type media_id: string_types, required
        :return: Id of the video media
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}/media/video/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, media_id, **kwargs):
        # type: (string_types, string_types, dict) -> VideoMediaInfo
        """Video Media Details

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param media_id: Id of the video media.
        :type media_id: string_types, required
        :return: Video media details
        :rtype: VideoMediaInfo
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/video/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=VideoMediaInfo,
            **kwargs
        )

    def list(self, manifest_id, query_params=None, **kwargs):
        # type: (string_types, VideoMediaInfoListQueryParams, dict) -> VideoMediaInfo
        """List all Video Media

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param query_params: Query parameters
        :type query_params: VideoMediaInfoListQueryParams
        :return: Video media
        :rtype: VideoMediaInfo
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/video',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=VideoMediaInfo,
            **kwargs
        )
