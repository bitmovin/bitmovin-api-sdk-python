# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.smooth_manifest_content_protection import SmoothManifestContentProtection
from bitmovin_api_sdk.encoding.manifests.smooth.contentprotection.smooth_manifest_content_protection_list_query_params import SmoothManifestContentProtectionListQueryParams


class ContentprotectionApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ContentprotectionApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, smooth_manifest_content_protection, **kwargs):
        # type: (string_types, SmoothManifestContentProtection, dict) -> SmoothManifestContentProtection
        """Add Content Protection to Smooth Streaming

        :param manifest_id: Id of the Smooth Streaming manifest.
        :type manifest_id: string_types, required
        :param smooth_manifest_content_protection: The Content Protection to be added
        :type smooth_manifest_content_protection: SmoothManifestContentProtection, required
        :return: Content protection
        :rtype: SmoothManifestContentProtection
        """

        return self.api_client.post(
            '/encoding/manifests/smooth/{manifest_id}/contentprotection',
            smooth_manifest_content_protection,
            path_params={'manifest_id': manifest_id},
            type=SmoothManifestContentProtection,
            **kwargs
        )

    def delete(self, manifest_id, protection_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Content Protection of Smooth Streaming

        :param manifest_id: Id of the Smooth Streaming manifest.
        :type manifest_id: string_types, required
        :param protection_id: Id of the content protection.
        :type protection_id: string_types, required
        :return: Id of the content protection
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/smooth/{manifest_id}/contentprotection/{protection_id}',
            path_params={'manifest_id': manifest_id, 'protection_id': protection_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, protection_id, **kwargs):
        # type: (string_types, string_types, dict) -> SmoothManifestContentProtection
        """Content Protection of Smooth Streaming Representation Details

        :param manifest_id: Id of the Smooth Streaming manifest.
        :type manifest_id: string_types, required
        :param protection_id: Id of the content protection.
        :type protection_id: string_types, required
        :return: Content protection details
        :rtype: SmoothManifestContentProtection
        """

        return self.api_client.get(
            '/encoding/manifests/smooth/{manifest_id}/contentprotection/{protection_id}',
            path_params={'manifest_id': manifest_id, 'protection_id': protection_id},
            type=SmoothManifestContentProtection,
            **kwargs
        )

    def list(self, manifest_id, query_params=None, **kwargs):
        # type: (string_types, SmoothManifestContentProtectionListQueryParams, dict) -> SmoothManifestContentProtection
        """List Content Protection of Smooth Streaming

        :param manifest_id: Id of the Smooth Streaming manifest.
        :type manifest_id: string_types, required
        :param query_params: Query parameters
        :type query_params: SmoothManifestContentProtectionListQueryParams
        :return: Content protection results
        :rtype: SmoothManifestContentProtection
        """

        return self.api_client.get(
            '/encoding/manifests/smooth/{manifest_id}/contentprotection',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=SmoothManifestContentProtection,
            **kwargs
        )
