# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_error import ResponseError


class StopApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(StopApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def update(self, stream_id, **kwargs):
        # type: (string_types, dict) -> None
        """Stop live stream by id

        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        """

        self.api_client.put(
            '/streams/live/{stream_id}/stop',
            path_params={'stream_id': stream_id},
            **kwargs
        )
