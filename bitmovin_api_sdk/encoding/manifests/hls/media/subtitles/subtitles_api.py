# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.subtitles_media_info import SubtitlesMediaInfo
from bitmovin_api_sdk.encoding.manifests.hls.media.subtitles.subtitles_media_info_list_query_params import SubtitlesMediaInfoListQueryParams


class SubtitlesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SubtitlesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, subtitles_media_info, **kwargs):
        # type: (string_types, SubtitlesMediaInfo, dict) -> SubtitlesMediaInfo
        """Add Subtitles Media

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param subtitles_media_info: The Subtitles Media to be added
        :type subtitles_media_info: SubtitlesMediaInfo, required
        :return: Subtitles media details
        :rtype: SubtitlesMediaInfo
        """

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/media/subtitles',
            subtitles_media_info,
            path_params={'manifest_id': manifest_id},
            type=SubtitlesMediaInfo,
            **kwargs
        )

    def delete(self, manifest_id, media_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Subtitles Media

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param media_id: Id of the subtitles media.
        :type media_id: string_types, required
        :return: Id of the subtitles media
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}/media/subtitles/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, media_id, **kwargs):
        # type: (string_types, string_types, dict) -> SubtitlesMediaInfo
        """Subtitles Media Details

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param media_id: Id of the subtitles media.
        :type media_id: string_types, required
        :return: Subtitles media details
        :rtype: SubtitlesMediaInfo
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/subtitles/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=SubtitlesMediaInfo,
            **kwargs
        )

    def list(self, manifest_id, query_params=None, **kwargs):
        # type: (string_types, SubtitlesMediaInfoListQueryParams, dict) -> SubtitlesMediaInfo
        """List all Subtitles Media

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param query_params: Query parameters
        :type query_params: SubtitlesMediaInfoListQueryParams
        :return: Subtitles media
        :rtype: SubtitlesMediaInfo
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/subtitles',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=SubtitlesMediaInfo,
            **kwargs
        )
