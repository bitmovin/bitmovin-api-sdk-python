# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.captions_embed_cea import CaptionsEmbedCea
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.muxings.ts.captions.cea.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.muxings.ts.captions.cea.captions_embed_cea_list_query_params import CaptionsEmbedCeaListQueryParams


class CeaApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(CeaApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, captions_embed_cea, **kwargs):
        """TS Embed CEA 608/708 Captions"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/captions/cea',
            captions_embed_cea,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=CaptionsEmbedCea,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, captions_id, **kwargs):
        """Delete Embedded CEA 608/708 Captions"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/captions/cea/{captions_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'captions_id': captions_id},
            type=CaptionsEmbedCea,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, captions_id, **kwargs):
        """Embedded CEA 608/708 Captions Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/captions/cea/{captions_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'captions_id': captions_id},
            type=CaptionsEmbedCea,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params: CaptionsEmbedCeaListQueryParams = None, **kwargs):
        """List TS Embedded CEA 608/708 Captions"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/captions/cea',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=CaptionsEmbedCea,
            **kwargs
        )
