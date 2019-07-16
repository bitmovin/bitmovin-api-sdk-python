# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.notification import Notification
from bitmovin_api_sdk.models.notification_state_entry import NotificationStateEntry
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.notifications.webhooks.webhooks_api import WebhooksApi
from bitmovin_api_sdk.notifications.states.states_api import StatesApi
from bitmovin_api_sdk.notifications.emails.emails_api import EmailsApi
from bitmovin_api_sdk.notifications.notification_list_query_params import NotificationListQueryParams
from bitmovin_api_sdk.notifications.notification_state_entry_list_by_notification_id_query_params import NotificationStateEntryListByNotificationIdQueryParams


class NotificationsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(NotificationsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.webhooks = WebhooksApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.states = StatesApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.emails = EmailsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def delete(self, notification_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Notification

        :param notification_id: Id of the notification
        :type notification_id: string_types, required
        :return: Id of the notification
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/notifications/{notification_id}',
            path_params={'notification_id': notification_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, notification_id, **kwargs):
        # type: (string_types, dict) -> Notification
        """Get Notification

        :param notification_id: Id of the notification
        :type notification_id: string_types, required
        :return: Webhook Details
        :rtype: Notification
        """

        return self.api_client.get(
            '/notifications/{notification_id}',
            path_params={'notification_id': notification_id},
            type=Notification,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (NotificationListQueryParams, dict) -> Notification
        """List Notifications

        :param query_params: Query parameters
        :type query_params: NotificationListQueryParams
        :return: List of Notifications
        :rtype: Notification
        """

        return self.api_client.get(
            '/notifications',
            query_params=query_params,
            pagination_response=True,
            type=Notification,
            **kwargs
        )

    def list_by_notification_id(self, notification_id, query_params=None, **kwargs):
        # type: (string_types, NotificationStateEntryListByNotificationIdQueryParams, dict) -> NotificationStateEntry
        """List Notification State History (All Resources)

        :param notification_id: Id of the notification
        :type notification_id: string_types, required
        :param query_params: Query parameters
        :type query_params: NotificationStateEntryListByNotificationIdQueryParams
        :return: List of state entries
        :rtype: NotificationStateEntry
        """

        return self.api_client.get(
            '/notifications/{notification_id}/states',
            path_params={'notification_id': notification_id},
            query_params=query_params,
            pagination_response=True,
            type=NotificationStateEntry,
            **kwargs
        )

    def mute(self, notification_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Mute Notification

        :param notification_id: Id of the notification
        :type notification_id: string_types, required
        :return: Id of the notification
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/notifications/{notification_id}/mute',
            path_params={'notification_id': notification_id},
            type=BitmovinResponse,
            **kwargs
        )

    def unmute(self, notification_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Unmute Notification

        :param notification_id: Id of the notification
        :type notification_id: string_types, required
        :return: Id of the notification
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/notifications/{notification_id}/unmute',
            path_params={'notification_id': notification_id},
            type=BitmovinResponse,
            **kwargs
        )
