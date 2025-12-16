# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.kantar_watermark import KantarWatermark
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class KantarWatermarkApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(KantarWatermarkApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, kantar_watermark, **kwargs):
        # type: (string_types, KantarWatermark, dict) -> KantarWatermark
        """Create or replace the Kantar Watermark for an encoding

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param kantar_watermark: The Kantar Watermark to be created
        :type kantar_watermark: KantarWatermark, required
        :return: Kantar Watermark
        :rtype: KantarWatermark
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/kantar-watermark',
            kantar_watermark,
            path_params={'encoding_id': encoding_id},
            type=KantarWatermark,
            **kwargs
        )

    def delete(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete the Kantar Watermark for an encoding

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :return: Id of the Kantar Watermark
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/kantar-watermark',
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> KantarWatermark
        """Get the Kantar Watermark for an encoding

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :return:
        :rtype: KantarWatermark
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/kantar-watermark',
            path_params={'encoding_id': encoding_id},
            type=KantarWatermark,
            **kwargs
        )
