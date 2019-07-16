# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.custom_data import CustomData
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class CustomdataApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(CustomdataApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, manifest_id, **kwargs):
        # type: (string_types, dict) -> CustomData
        """HLS Manifest Custom Data

        :param manifest_id: UUID of the HLS manifest
        :type manifest_id: string_types, required
        :return: HLS Manifest Custom Data
        :rtype: CustomData
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/customData',
            path_params={'manifest_id': manifest_id},
            type=CustomData,
            **kwargs
        )
