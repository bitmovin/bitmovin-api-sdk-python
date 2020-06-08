# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.play_ready_drm import PlayReadyDrm
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.mp4.drm.playready.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.mp4.drm.playready.play_ready_drm_list_query_params import PlayReadyDrmListQueryParams


class PlayreadyApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(PlayreadyApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, play_ready_drm, **kwargs):
        # type: (string_types, string_types, PlayReadyDrm, dict) -> PlayReadyDrm
        """Add PlayReady DRM to an MP4 muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the MP4 muxing.
        :type muxing_id: string_types, required
        :param play_ready_drm: The PlayReady DRM to be created
        :type play_ready_drm: PlayReadyDrm, required
        :return: PlayReady configuration
        :rtype: PlayReadyDrm
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}/drm/playready',
            play_ready_drm,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=PlayReadyDrm,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, drm_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete PlayReady DRM from an MP4 muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the MP4 muxing.
        :type muxing_id: string_types, required
        :param drm_id: Id of the PlayReady DRM configuration.
        :type drm_id: string_types, required
        :return: Id of the PlayReady DRM configuration.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}/drm/playready/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, drm_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> PlayReadyDrm
        """PlayReady DRM Details of an MP4 muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the MP4 muxing.
        :type muxing_id: string_types, required
        :param drm_id: Id of the PlayReady DRM configuration.
        :type drm_id: string_types, required
        :return: PlayReady configuration
        :rtype: PlayReadyDrm
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}/drm/playready/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=PlayReadyDrm,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params=None, **kwargs):
        # type: (string_types, string_types, PlayReadyDrmListQueryParams, dict) -> PlayReadyDrm
        """List PlayReady DRMs of an MP4 muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the MP4 muxing.
        :type muxing_id: string_types, required
        :param query_params: Query parameters
        :type query_params: PlayReadyDrmListQueryParams
        :return: List of PlayReady DRM configurations
        :rtype: PlayReadyDrm
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}/drm/playready',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=PlayReadyDrm,
            **kwargs
        )
