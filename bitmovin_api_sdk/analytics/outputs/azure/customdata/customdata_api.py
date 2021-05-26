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

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> CustomData
        """Azure Output Custom Data

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Azure output custom data
        :rtype: CustomData
        """

        return self.api_client.get(
            '/analytics/outputs/azure/{output_id}/customData',
            path_params={'output_id': output_id},
            type=CustomData,
            **kwargs
        )
