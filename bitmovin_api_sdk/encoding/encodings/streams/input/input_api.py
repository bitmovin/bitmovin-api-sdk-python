# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.encoding_stream_input_details import EncodingStreamInputDetails
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class InputApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(InputApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> EncodingStreamInputDetails
        """Stream Input Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :return: Details about the stream input
        :rtype: EncodingStreamInputDetails
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/input',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=EncodingStreamInputDetails,
            **kwargs
        )
