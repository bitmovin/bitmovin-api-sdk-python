# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.live_standby_pool_details import LiveStandbyPoolDetails
from bitmovin_api_sdk.models.live_standby_pool_request import LiveStandbyPoolRequest
from bitmovin_api_sdk.models.live_standby_pool_response import LiveStandbyPoolResponse
from bitmovin_api_sdk.models.live_standby_pool_update import LiveStandbyPoolUpdate
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.live.standby_pools.actions.actions_api import ActionsApi
from bitmovin_api_sdk.encoding.live.standby_pools.encodings.encodings_api import EncodingsApi
from bitmovin_api_sdk.encoding.live.standby_pools.logs.logs_api import LogsApi


class StandbyPoolsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(StandbyPoolsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.actions = ActionsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.encodings = EncodingsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.logs = LogsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, live_standby_pool_request, **kwargs):
        # type: (LiveStandbyPoolRequest, dict) -> LiveStandbyPoolDetails
        """Create new standby pool

        :param live_standby_pool_request: The pool to be created
        :type live_standby_pool_request: LiveStandbyPoolRequest, required
        :return:
        :rtype: LiveStandbyPoolDetails
        """

        return self.api_client.post(
            '/encoding/live/standby-pools',
            live_standby_pool_request,
            type=LiveStandbyPoolDetails,
            **kwargs
        )

    def delete(self, pool_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete standby pool by id

        :param pool_id: Id of the standby pool
        :type pool_id: string_types, required
        :return: Id of the standby pool that was deleted
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/live/standby-pools/{pool_id}',
            path_params={'pool_id': pool_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, pool_id, **kwargs):
        # type: (string_types, dict) -> LiveStandbyPoolDetails
        """Get details of a standby pool by id

        :param pool_id: Id of the standby pool
        :type pool_id: string_types, required
        :return:
        :rtype: LiveStandbyPoolDetails
        """

        return self.api_client.get(
            '/encoding/live/standby-pools/{pool_id}',
            path_params={'pool_id': pool_id},
            type=LiveStandbyPoolDetails,
            **kwargs
        )

    def list(self, **kwargs):
        # type: (dict) -> LiveStandbyPoolResponse
        """List Standby pools

        :return: Standby pools list response
        :rtype: LiveStandbyPoolResponse
        """

        return self.api_client.get(
            '/encoding/live/standby-pools',
            pagination_response=True,
            type=LiveStandbyPoolResponse,
            **kwargs
        )

    def patch(self, pool_id, live_standby_pool_update, **kwargs):
        # type: (string_types, LiveStandbyPoolUpdate, dict) -> LiveStandbyPoolDetails
        """Partially update standby pool by id

        :param pool_id: Id of the standby pool
        :type pool_id: string_types, required
        :param live_standby_pool_update: The updated standby pool object.
        :type live_standby_pool_update: LiveStandbyPoolUpdate, required
        :return:
        :rtype: LiveStandbyPoolDetails
        """

        return self.api_client.patch(
            '/encoding/live/standby-pools/{pool_id}',
            live_standby_pool_update,
            path_params={'pool_id': pool_id},
            type=LiveStandbyPoolDetails,
            **kwargs
        )
