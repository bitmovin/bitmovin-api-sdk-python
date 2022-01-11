# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.output_type_response import OutputTypeResponse
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

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> OutputTypeResponse
        """Get Output Type

        :param output_id: Id of the wanted output
        :type output_id: string_types, required
        :return: Output type response
        :rtype: OutputTypeResponse
        """

        return self.api_client.get(
            '/encoding/outputs/{output_id}/type',
            path_params={'output_id': output_id},
            type=OutputTypeResponse,
            **kwargs
        )
