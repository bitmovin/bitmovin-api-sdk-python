# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bif import Bif
from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.streams.bifs.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.streams.bifs.bif_list_query_params import BifListQueryParams


class BifsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(BifsApi, self).__init__(
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

    def create(self, encoding_id, stream_id, bif, **kwargs):
        """Add a Roku Bif file"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/bifs',
            bif,
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=Bif,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, bif_id, **kwargs):
        """Delete Bif"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/bifs/{bif_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'bif_id': bif_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, stream_id, bif_id, **kwargs):
        """Bif Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/bifs/{bif_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'bif_id': bif_id},
            type=Bif,
            **kwargs
        )

    def list(self, encoding_id, stream_id, query_params: BifListQueryParams = None, **kwargs):
        """List Bifs"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/bifs',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=Bif,
            **kwargs
        )
