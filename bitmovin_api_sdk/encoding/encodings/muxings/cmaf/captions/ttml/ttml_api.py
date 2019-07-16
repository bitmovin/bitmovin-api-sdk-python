# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.ttml_embed import TtmlEmbed


class TtmlApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(TtmlApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def delete(self, encoding_id, muxing_id, captions_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> TtmlEmbed
        """Delete TTML Embed Captions

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the CMAF muxing
        :type muxing_id: string_types, required
        :param captions_id: Id of the captions configuration.
        :type captions_id: string_types, required
        :return: Id of the captions configuration.
        :rtype: TtmlEmbed
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/cmaf/{muxing_id}/captions/ttml/{captions_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'captions_id': captions_id},
            type=TtmlEmbed,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, captions_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> TtmlEmbed
        """TTML Embed Captions Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the CMAF muxing
        :type muxing_id: string_types, required
        :param captions_id: Id of the captions.
        :type captions_id: string_types, required
        :return: Captions configuration
        :rtype: TtmlEmbed
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/cmaf/{muxing_id}/captions/ttml/{captions_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'captions_id': captions_id},
            type=TtmlEmbed,
            **kwargs
        )
