# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.muxing_type_response import MuxingTypeResponse
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

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> MuxingTypeResponse
        """Get Muxing type

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the muxing.
        :type muxing_id: string_types, required
        :return: Muxing type response
        :rtype: MuxingTypeResponse
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/{muxing_id}/type',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=MuxingTypeResponse,
            **kwargs
        )
