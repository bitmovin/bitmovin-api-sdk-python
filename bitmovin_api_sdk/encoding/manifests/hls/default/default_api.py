# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.hls_manifest_default import HlsManifestDefault
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class DefaultApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DefaultApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, hls_manifest_default, **kwargs):
        # type: (HlsManifestDefault, dict) -> HlsManifestDefault
        """Create Default HLS Manifest

        :param hls_manifest_default: A Default Manifest is the easiest way to create a manifest file. Its contents will be configured automatically, depending on what output your encoding creates (muxings, thumbnails, sprites, subtitles, DRM information). If you need more control, create a Custom Manifest instead. See TODO: link
        :type hls_manifest_default: HlsManifestDefault, required
        :return: HLS manifest
        :rtype: HlsManifestDefault
        """

        return self.api_client.post(
            '/encoding/manifests/hls/default',
            hls_manifest_default,
            type=HlsManifestDefault,
            **kwargs
        )
