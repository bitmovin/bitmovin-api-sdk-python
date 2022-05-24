# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.encoding_output_paths import EncodingOutputPaths
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class OutputPathsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(OutputPathsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> list[EncodingOutputPaths]
        """Encoding Output Paths Retrieval

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :return: List of output paths per defined encoding output
        :rtype: list[EncodingOutputPaths]
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/output-paths',
            path_params={'encoding_id': encoding_id},
            list_response=True,
            type=EncodingOutputPaths,
            **kwargs
        )
