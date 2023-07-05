# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.dash_manifest_default import DashManifestDefault
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

    def create(self, dash_manifest_default, **kwargs):
        # type: (DashManifestDefault, dict) -> DashManifestDefault
        """Create Default DASH Manifest

        :param dash_manifest_default: The Default DASH Manifest to be created.
        :type dash_manifest_default: DashManifestDefault, required
        :return: Id of the DASH Manifest
        :rtype: DashManifestDefault
        """

        return self.api_client.post(
            '/encoding/manifests/dash/default',
            dash_manifest_default,
            type=DashManifestDefault,
            **kwargs
        )
