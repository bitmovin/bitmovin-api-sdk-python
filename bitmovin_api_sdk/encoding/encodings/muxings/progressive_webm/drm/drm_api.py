# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.drm import Drm
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_webm.drm.cenc.cenc_api import CencApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_webm.drm.speke.speke_api import SpekeApi


class DrmApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DrmApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.cenc = CencApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.speke = SpekeApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, muxing_id, drm_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> Drm
        """DRM Details of a Progressive WEBM muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Progressive WEBM muxing
        :type muxing_id: string_types, required
        :param drm_id: Id of the DRM.
        :type drm_id: string_types, required
        :return: DRM
        :rtype: Drm
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-webm/{muxing_id}/drm/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=Drm,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> Drm
        """List all DRMs of Progressive WEBM muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Progressive WEBM muxing
        :type muxing_id: string_types, required
        :return: List of DRM configurations
        :rtype: Drm
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-webm/{muxing_id}/drm',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            pagination_response=True,
            type=Drm,
            **kwargs
        )
