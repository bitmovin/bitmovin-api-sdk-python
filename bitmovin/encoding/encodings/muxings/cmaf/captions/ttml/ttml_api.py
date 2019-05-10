# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.ttml_embed import TtmlEmbed


class TtmlApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(TtmlApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def delete(self, encoding_id, muxing_id, captions_id, **kwargs):
        """Delete TTML Embed Captions"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/cmaf/{muxing_id}/captions/ttml/{captions_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'captions_id': captions_id},
            type=TtmlEmbed,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, captions_id, **kwargs):
        """TTML Embed Captions Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/cmaf/{muxing_id}/captions/ttml/{captions_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'captions_id': captions_id},
            type=TtmlEmbed,
            **kwargs
        )
