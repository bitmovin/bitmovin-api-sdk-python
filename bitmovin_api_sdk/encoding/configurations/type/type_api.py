# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.codec_config_type_response import CodecConfigTypeResponse
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

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> CodecConfigTypeResponse
        """Get Codec Configuration Type

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Codec Configuration type
        :rtype: CodecConfigTypeResponse
        """

        return self.api_client.get(
            '/encoding/configurations/{configuration_id}/type',
            path_params={'configuration_id': configuration_id},
            type=CodecConfigTypeResponse,
            **kwargs
        )
