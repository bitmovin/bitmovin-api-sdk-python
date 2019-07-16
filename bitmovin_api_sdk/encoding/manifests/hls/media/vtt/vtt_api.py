# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.vtt_media_info import VttMediaInfo
from bitmovin_api_sdk.encoding.manifests.hls.media.vtt.vtt_media_info_list_query_params import VttMediaInfoListQueryParams


class VttApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(VttApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, vtt_media_info, **kwargs):
        # type: (string_types, VttMediaInfo, dict) -> VttMediaInfo
        """Add VTT Media

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param vtt_media_info: The VTT Media to be added
        :type vtt_media_info: VttMediaInfo, required
        :return: VTT media details
        :rtype: VttMediaInfo
        """

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/media/vtt',
            vtt_media_info,
            path_params={'manifest_id': manifest_id},
            type=VttMediaInfo,
            **kwargs
        )

    def delete(self, manifest_id, media_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete VTT Media

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param media_id: Id of the VTT media.
        :type media_id: string_types, required
        :return: Id of the VTT media
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}/media/vtt/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, media_id, **kwargs):
        # type: (string_types, string_types, dict) -> VttMediaInfo
        """VTT Media Details

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param media_id: Id of the VTT media.
        :type media_id: string_types, required
        :return: VTT media details
        :rtype: VttMediaInfo
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/vtt/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=VttMediaInfo,
            **kwargs
        )

    def list(self, manifest_id, query_params=None, **kwargs):
        # type: (string_types, VttMediaInfoListQueryParams, dict) -> VttMediaInfo
        """List all VTT Media

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param query_params: Query parameters
        :type query_params: VttMediaInfoListQueryParams
        :return: VTT media
        :rtype: VttMediaInfo
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/vtt',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=VttMediaInfo,
            **kwargs
        )
