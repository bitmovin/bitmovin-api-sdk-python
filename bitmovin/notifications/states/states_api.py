# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.notification_state_entry import NotificationStateEntry
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.notifications.states.notification_state_entry_list_query_params import NotificationStateEntryListQueryParams


class StatesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(StatesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, notification_id, resource_id, query_params: NotificationStateEntryListQueryParams = None, **kwargs):
        """List Notification State History (Specific Resource)"""

        return self.api_client.get(
            '/notifications/{notification_id}/states/{resource_id}',
            path_params={'notification_id': notification_id, 'resource_id': resource_id},
            query_params=query_params,
            pagination_response=True,
            type=NotificationStateEntry,
            **kwargs
        )
