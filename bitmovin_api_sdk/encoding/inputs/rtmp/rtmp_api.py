# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.rtmp_input import RtmpInput
from bitmovin_api_sdk.encoding.inputs.rtmp.rtmp_input_list_query_params import RtmpInputListQueryParams


class RtmpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(RtmpApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> RtmpInput
        """RTMP Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: RTMP input
        :rtype: RtmpInput
        """

        return self.api_client.get(
            '/encoding/inputs/rtmp/{input_id}',
            path_params={'input_id': input_id},
            type=RtmpInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (RtmpInputListQueryParams, dict) -> RtmpInput
        """List RTMP Inputs

        :param query_params: Query parameters
        :type query_params: RtmpInputListQueryParams
        :return: List of RTMP inputs
        :rtype: RtmpInput
        """

        return self.api_client.get(
            '/encoding/inputs/rtmp',
            query_params=query_params,
            pagination_response=True,
            type=RtmpInput,
            **kwargs
        )
