# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.esam_media_point import EsamMediaPoint
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class MediaPointsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(MediaPointsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, esam_media_point, **kwargs):
        # type: (string_types, EsamMediaPoint, dict) -> EsamMediaPoint
        """Create ESAM media point for live stream

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :param esam_media_point: ESAM media point
        :type esam_media_point: EsamMediaPoint, required
        :return: ESAM media point
        :rtype: EsamMediaPoint
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/live/esam/media-points',
            esam_media_point,
            path_params={'encoding_id': encoding_id},
            type=EsamMediaPoint,
            **kwargs
        )
