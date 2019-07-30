# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.redundant_rtmp_input import RedundantRtmpInput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.inputs.redundant_rtmp.redundant_rtmp_input_list_query_params import RedundantRtmpInputListQueryParams


class RedundantRtmpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(RedundantRtmpApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, redundant_rtmp_input, **kwargs):
        # type: (RedundantRtmpInput, dict) -> RedundantRtmpInput
        """Create Redundant RTMP Input

        :param redundant_rtmp_input: The Redundant RTMP input to be created
        :type redundant_rtmp_input: RedundantRtmpInput, required
        :return: Redundant RTMP input
        :rtype: RedundantRtmpInput
        """

        return self.api_client.post(
            '/encoding/inputs/redundant-rtmp',
            redundant_rtmp_input,
            type=RedundantRtmpInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Redundant RTMP Input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the input
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/inputs/redundant-rtmp/{input_id}',
            path_params={'input_id': input_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> RedundantRtmpInput
        """Redundant RTMP Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Redundant RTMP input
        :rtype: RedundantRtmpInput
        """

        return self.api_client.get(
            '/encoding/inputs/redundant-rtmp/{input_id}',
            path_params={'input_id': input_id},
            type=RedundantRtmpInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (RedundantRtmpInputListQueryParams, dict) -> RedundantRtmpInput
        """List Redundant RTMP Inputs

        :param query_params: Query parameters
        :type query_params: RedundantRtmpInputListQueryParams
        :return: List of Redundant RTMP inputs
        :rtype: RedundantRtmpInput
        """

        return self.api_client.get(
            '/encoding/inputs/redundant-rtmp',
            query_params=query_params,
            pagination_response=True,
            type=RedundantRtmpInput,
            **kwargs
        )
