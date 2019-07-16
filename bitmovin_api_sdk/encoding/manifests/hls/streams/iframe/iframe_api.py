# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.i_frame_playlist import IFramePlaylist
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.manifests.hls.streams.iframe.i_frame_playlist_list_query_params import IFramePlaylistListQueryParams


class IframeApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(IframeApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, stream_id, i_frame_playlist, **kwargs):
        # type: (string_types, string_types, IFramePlaylist, dict) -> IFramePlaylist
        """Add I-frame playlist to variant stream

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param stream_id: Id of the variant stream.
        :type stream_id: string_types, required
        :param i_frame_playlist: The I-frame playlist to be added
        :type i_frame_playlist: IFramePlaylist, required
        :return: Iframe-Playlist details
        :rtype: IFramePlaylist
        """

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/streams/{stream_id}/iframe',
            i_frame_playlist,
            path_params={'manifest_id': manifest_id, 'stream_id': stream_id},
            type=IFramePlaylist,
            **kwargs
        )

    def delete(self, manifest_id, stream_id, iframe_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete I-frame playlist

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param stream_id: Id of the variant stream.
        :type stream_id: string_types, required
        :param iframe_id: Id of the Iframe-Playlist.
        :type iframe_id: string_types, required
        :return: Id of the custom tag
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}/streams/{stream_id}/iframe/{iframe_id}',
            path_params={'manifest_id': manifest_id, 'stream_id': stream_id, 'iframe_id': iframe_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, stream_id, iframe_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> IFramePlaylist
        """I-frame playlist Details

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param stream_id: Id of the variant stream.
        :type stream_id: string_types, required
        :param iframe_id: Id of the Iframe-Playlist.
        :type iframe_id: string_types, required
        :return: Custom tag details
        :rtype: IFramePlaylist
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/streams/{stream_id}/iframe/{iframe_id}',
            path_params={'manifest_id': manifest_id, 'stream_id': stream_id, 'iframe_id': iframe_id},
            type=IFramePlaylist,
            **kwargs
        )

    def list(self, manifest_id, stream_id, query_params=None, **kwargs):
        # type: (string_types, string_types, IFramePlaylistListQueryParams, dict) -> IFramePlaylist
        """List all I-frame playlists of a variant stream

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param stream_id: Id of the variant stream.
        :type stream_id: string_types, required
        :param query_params: Query parameters
        :type query_params: IFramePlaylistListQueryParams
        :return: Video media
        :rtype: IFramePlaylist
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/streams/{stream_id}/iframe',
            path_params={'manifest_id': manifest_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=IFramePlaylist,
            **kwargs
        )
