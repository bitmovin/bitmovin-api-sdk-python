# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.input_stream_type_response import InputStreamTypeResponse
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

    def get(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> InputStreamTypeResponse
        """Get Input Stream Type

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the input stream
        :type input_stream_id: string_types, required
        :return: Service specific result
        :rtype: InputStreamTypeResponse
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/{input_stream_id}/type',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=InputStreamTypeResponse,
            **kwargs
        )
