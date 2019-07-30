# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.closed_captions_media_info import ClosedCaptionsMediaInfo
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.manifests.hls.media.closed_captions.closed_captions_media_info_list_query_params import ClosedCaptionsMediaInfoListQueryParams


class ClosedCaptionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ClosedCaptionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, closed_captions_media_info, **kwargs):
        # type: (string_types, ClosedCaptionsMediaInfo, dict) -> ClosedCaptionsMediaInfo
        """Add Closed Captions Media

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param closed_captions_media_info: The Closed Captions Media to be added
        :type closed_captions_media_info: ClosedCaptionsMediaInfo, required
        :return: Closed Captions media details
        :rtype: ClosedCaptionsMediaInfo
        """

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/media/closed-captions',
            closed_captions_media_info,
            path_params={'manifest_id': manifest_id},
            type=ClosedCaptionsMediaInfo,
            **kwargs
        )

    def delete(self, manifest_id, media_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Closed Captions Media

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param media_id: Id of the closed captions media.
        :type media_id: string_types, required
        :return: Id of the closed captions media
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}/media/closed-captions/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, media_id, **kwargs):
        # type: (string_types, string_types, dict) -> ClosedCaptionsMediaInfo
        """Closed Captions Media Details

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param media_id: Id of the closed captions media.
        :type media_id: string_types, required
        :return: Closed Captions media details
        :rtype: ClosedCaptionsMediaInfo
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/closed-captions/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=ClosedCaptionsMediaInfo,
            **kwargs
        )

    def list(self, manifest_id, query_params=None, **kwargs):
        # type: (string_types, ClosedCaptionsMediaInfoListQueryParams, dict) -> ClosedCaptionsMediaInfo
        """List all Closed Captions Media

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param query_params: Query parameters
        :type query_params: ClosedCaptionsMediaInfoListQueryParams
        :return: Closed Captions media
        :rtype: ClosedCaptionsMediaInfo
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/closed-captions',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=ClosedCaptionsMediaInfo,
            **kwargs
        )
