# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.notification_state_entry import NotificationStateEntry
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.notifications.states.notification_state_entry_list_query_params import NotificationStateEntryListQueryParams


class StatesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(StatesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, notification_id, resource_id, query_params=None, **kwargs):
        # type: (string_types, string_types, NotificationStateEntryListQueryParams, dict) -> NotificationStateEntry
        """List Notification State History (Specific Resource)

        :param notification_id: Id of the notification
        :type notification_id: string_types, required
        :param resource_id: Id of the resource, e.g. encoding id
        :type resource_id: string_types, required
        :param query_params: Query parameters
        :type query_params: NotificationStateEntryListQueryParams
        :return: List of state entries
        :rtype: NotificationStateEntry
        """

        return self.api_client.get(
            '/notifications/{notification_id}/states/{resource_id}',
            path_params={'notification_id': notification_id, 'resource_id': resource_id},
            query_params=query_params,
            pagination_response=True,
            type=NotificationStateEntry,
            **kwargs
        )
