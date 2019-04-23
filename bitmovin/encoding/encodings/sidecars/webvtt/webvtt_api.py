# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.web_vtt_sidecar_file import WebVttSidecarFile


class WebvttApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(WebvttApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, web_vtt_sidecar_file, **kwargs):
        """Add WebVTT sidecar file"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/sidecars/webvtt',
            web_vtt_sidecar_file,
            path_params={'encoding_id': encoding_id},
            type=WebVttSidecarFile,
            **kwargs
        )

    def delete(self, encoding_id, sidecar_id, **kwargs):
        """Delete Sidecar"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/sidecars/webvtt/{sidecar_id}',
            path_params={'encoding_id': encoding_id, 'sidecar_id': sidecar_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, sidecar_id, **kwargs):
        """WebVTT Sidecar Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/sidecars/webvtt/{sidecar_id}',
            path_params={'encoding_id': encoding_id, 'sidecar_id': sidecar_id},
            type=WebVttSidecarFile,
            **kwargs
        )
