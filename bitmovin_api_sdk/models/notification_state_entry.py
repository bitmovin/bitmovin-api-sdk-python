# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.notification_states import NotificationStates
import pprint
import six


class NotificationStateEntry(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 state=None,
                 muted=None,
                 notification_id=None,
                 resource_id=None,
                 triggered_at=None):
        # type: (string_types, NotificationStates, bool, string_types, string_types, datetime) -> None
        super(NotificationStateEntry, self).__init__(id_=id_)

        self._state = None
        self._muted = None
        self._notification_id = None
        self._resource_id = None
        self._triggered_at = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if muted is not None:
            self.muted = muted
        if notification_id is not None:
            self.notification_id = notification_id
        if resource_id is not None:
            self.resource_id = resource_id
        if triggered_at is not None:
            self.triggered_at = triggered_at

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(NotificationStateEntry, self), 'openapi_types'):
            types = getattr(super(NotificationStateEntry, self), 'openapi_types')

        types.update({
            'state': 'NotificationStates',
            'muted': 'bool',
            'notification_id': 'string_types',
            'resource_id': 'string_types',
            'triggered_at': 'datetime'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(NotificationStateEntry, self), 'attribute_map'):
            attributes = getattr(super(NotificationStateEntry, self), 'attribute_map')

        attributes.update({
            'state': 'state',
            'muted': 'muted',
            'notification_id': 'notificationId',
            'resource_id': 'resourceId',
            'triggered_at': 'triggeredAt'
        })
        return attributes

    @property
    def state(self):
        # type: () -> NotificationStates
        """Gets the state of this NotificationStateEntry.


        :return: The state of this NotificationStateEntry.
        :rtype: NotificationStates
        """
        return self._state

    @state.setter
    def state(self, state):
        # type: (NotificationStates) -> None
        """Sets the state of this NotificationStateEntry.


        :param state: The state of this NotificationStateEntry.
        :type: NotificationStates
        """

        if state is not None:
            if not isinstance(state, NotificationStates):
                raise TypeError("Invalid type for `state`, type has to be `NotificationStates`")

        self._state = state

    @property
    def muted(self):
        # type: () -> bool
        """Gets the muted of this NotificationStateEntry.

        Indicate if notification was sent (required)

        :return: The muted of this NotificationStateEntry.
        :rtype: bool
        """
        return self._muted

    @muted.setter
    def muted(self, muted):
        # type: (bool) -> None
        """Sets the muted of this NotificationStateEntry.

        Indicate if notification was sent (required)

        :param muted: The muted of this NotificationStateEntry.
        :type: bool
        """

        if muted is not None:
            if not isinstance(muted, bool):
                raise TypeError("Invalid type for `muted`, type has to be `bool`")

        self._muted = muted

    @property
    def notification_id(self):
        # type: () -> string_types
        """Gets the notification_id of this NotificationStateEntry.

        The notification this state belongs to (required)

        :return: The notification_id of this NotificationStateEntry.
        :rtype: string_types
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        # type: (string_types) -> None
        """Sets the notification_id of this NotificationStateEntry.

        The notification this state belongs to (required)

        :param notification_id: The notification_id of this NotificationStateEntry.
        :type: string_types
        """

        if notification_id is not None:
            if not isinstance(notification_id, string_types):
                raise TypeError("Invalid type for `notification_id`, type has to be `string_types`")

        self._notification_id = notification_id

    @property
    def resource_id(self):
        # type: () -> string_types
        """Gets the resource_id of this NotificationStateEntry.

        Indicate if triggered for specific resource (required)

        :return: The resource_id of this NotificationStateEntry.
        :rtype: string_types
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        # type: (string_types) -> None
        """Sets the resource_id of this NotificationStateEntry.

        Indicate if triggered for specific resource (required)

        :param resource_id: The resource_id of this NotificationStateEntry.
        :type: string_types
        """

        if resource_id is not None:
            if not isinstance(resource_id, string_types):
                raise TypeError("Invalid type for `resource_id`, type has to be `string_types`")

        self._resource_id = resource_id

    @property
    def triggered_at(self):
        # type: () -> datetime
        """Gets the triggered_at of this NotificationStateEntry.


        :return: The triggered_at of this NotificationStateEntry.
        :rtype: datetime
        """
        return self._triggered_at

    @triggered_at.setter
    def triggered_at(self, triggered_at):
        # type: (datetime) -> None
        """Sets the triggered_at of this NotificationStateEntry.


        :param triggered_at: The triggered_at of this NotificationStateEntry.
        :type: datetime
        """

        if triggered_at is not None:
            if not isinstance(triggered_at, datetime):
                raise TypeError("Invalid type for `triggered_at`, type has to be `datetime`")

        self._triggered_at = triggered_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(NotificationStateEntry, self), "to_dict"):
            result = super(NotificationStateEntry, self).to_dict()
        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                if len(value) == 0:
                    continue
                result[self.attribute_map.get(attr)] = [y.value if isinstance(y, Enum) else y for y in [x.to_dict() if hasattr(x, "to_dict") else x for x in value]]
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = {k: (v.to_dict() if hasattr(v, "to_dict") else v) for (k, v) in value.items()}
            else:
                result[self.attribute_map.get(attr)] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NotificationStateEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
