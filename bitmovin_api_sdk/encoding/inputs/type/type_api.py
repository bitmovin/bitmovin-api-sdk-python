# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.input_type_response import InputTypeResponse
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

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> InputTypeResponse
        """Get Input Type

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Input type response
        :rtype: InputTypeResponse
        """

        return self.api_client.get(
            '/encoding/inputs/{input_id}/type',
            path_params={'input_id': input_id},
            type=InputTypeResponse,
            **kwargs
        )
