# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.redundant_rtmp_input import RedundantRtmpInput
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.inputs.redundantRtmp.redundant_rtmp_input_list_query_params import RedundantRtmpInputListQueryParams


class RedundantRtmpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(RedundantRtmpApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, redundant_rtmp_input, **kwargs):
        """Create Redundant RTMP Input"""

        return self.api_client.post(
            '/encoding/inputs/redundant-rtmp',
            redundant_rtmp_input,
            type=RedundantRtmpInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete Redundant RTMP Input"""

        return self.api_client.delete(
            '/encoding/inputs/redundant-rtmp/{input_id}',
            path_params={'input_id': input_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """Redundant RTMP Input Details"""

        return self.api_client.get(
            '/encoding/inputs/redundant-rtmp/{input_id}',
            path_params={'input_id': input_id},
            type=RedundantRtmpInput,
            **kwargs
        )

    def list(self, query_params: RedundantRtmpInputListQueryParams = None, **kwargs):
        """List Redundant RTMP Inputs"""

        return self.api_client.get(
            '/encoding/inputs/redundant-rtmp',
            query_params=query_params,
            pagination_response=True,
            type=RedundantRtmpInput,
            **kwargs
        )
