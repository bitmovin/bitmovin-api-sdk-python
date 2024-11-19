# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.live_standby_pool_encoding import LiveStandbyPoolEncoding
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class ActionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ActionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def acquire_encoding(self, pool_id, **kwargs):
        # type: (string_types, dict) -> LiveStandbyPoolEncoding
        """Acquire an encoding from a standby pool

        :param pool_id: Id of the standby pool
        :type pool_id: string_types, required
        :return:
        :rtype: LiveStandbyPoolEncoding
        """

        return self.api_client.post(
            '/encoding/live/standby-pools/{pool_id}/actions/acquire-encoding',
            path_params={'pool_id': pool_id},
            type=LiveStandbyPoolEncoding,
            **kwargs
        )

    def delete_error_encodings(self, pool_id, **kwargs):
        # type: (string_types, dict) -> LiveStandbyPoolEncoding
        """Delete error encodings from the standby pool

        :param pool_id: Id of the standby pool
        :type pool_id: string_types, required
        :return:
        :rtype: LiveStandbyPoolEncoding
        """

        return self.api_client.post(
            '/encoding/live/standby-pools/{pool_id}/actions/delete-error-encodings',
            path_params={'pool_id': pool_id},
            type=LiveStandbyPoolEncoding,
            **kwargs
        )
