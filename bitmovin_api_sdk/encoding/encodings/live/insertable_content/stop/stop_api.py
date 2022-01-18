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

    def create(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> None
        """Stops currently running Inserted Content

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        """

        self.api_client.post(
            '/encoding/encodings/{encoding_id}/live/insertable-content/stop',
            path_params={'encoding_id': encoding_id},
            **kwargs
        )
