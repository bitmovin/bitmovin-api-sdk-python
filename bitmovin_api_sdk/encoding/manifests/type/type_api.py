# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.manifest_type_response import ManifestTypeResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class TypeApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(TypeApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, manifest_id, **kwargs):
        # type: (string_types, dict) -> ManifestTypeResponse
        """Get Manifest Type

        :param manifest_id: UUID of the manifest
        :type manifest_id: string_types, required
        :return: Service specific result
        :rtype: ManifestTypeResponse
        """

        return self.api_client.get(
            '/encoding/manifests/{manifest_id}/type',
            path_params={'manifest_id': manifest_id},
            type=ManifestTypeResponse,
            **kwargs
        )
