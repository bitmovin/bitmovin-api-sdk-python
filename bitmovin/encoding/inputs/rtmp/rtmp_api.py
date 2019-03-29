# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.rtmp_input import RtmpInput
from bitmovin.encoding.inputs.rtmp.rtmp_input_list_query_params import RtmpInputListQueryParams


class RtmpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(RtmpApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, input_id, **kwargs):
        """RTMP Input Details"""

        return self.api_client.get(
            '/encoding/inputs/rtmp/{input_id}',
            path_params={'input_id': input_id},
            type=RtmpInput,
            **kwargs
        )

    def list(self, query_params: RtmpInputListQueryParams = None, **kwargs):
        """List RTMP Inputs"""

        return self.api_client.get(
            '/encoding/inputs/rtmp',
            query_params=query_params,
            pagination_response=True,
            type=RtmpInput,
            **kwargs
        )
