# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class Notification(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 resolve=None,
                 resource_id=None,
                 triggered_at=None,
                 type_=None,
                 event_type=None,
                 category=None,
                 resource_type=None,
                 muted=None,
                 custom_data=None):
        # type: (string_types, bool, string_types, datetime, string_types, string_types, string_types, string_types, bool, dict) -> None
        super(Notification, self).__init__(id_=id_)

        self._resolve = None
        self._resource_id = None
        self._triggered_at = None
        self._type = None
        self._event_type = None
        self._category = None
        self._resource_type = None
        self._muted = None
        self._custom_data = None
        self.discriminator = None

        if resolve is not None:
            self.resolve = resolve
        if resource_id is not None:
            self.resource_id = resource_id
        if triggered_at is not None:
            self.triggered_at = triggered_at
        if type_ is not None:
            self.type = type_
        if event_type is not None:
            self.event_type = event_type
        if category is not None:
            self.category = category
        if resource_type is not None:
            self.resource_type = resource_type
        if muted is not None:
            self.muted = muted
        if custom_data is not None:
            self.custom_data = custom_data

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Notification, self), 'openapi_types'):
            types = getattr(super(Notification, self), 'openapi_types')

        types.update({
            'resolve': 'bool',
            'resource_id': 'string_types',
            'triggered_at': 'datetime',
            'type': 'string_types',
            'event_type': 'string_types',
            'category': 'string_types',
            'resource_type': 'string_types',
            'muted': 'bool',
            'custom_data': 'dict(str, object)'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Notification, self), 'attribute_map'):
            attributes = getattr(super(Notification, self), 'attribute_map')

        attributes.update({
            'resolve': 'resolve',
            'resource_id': 'resourceId',
            'triggered_at': 'triggeredAt',
            'type': 'type',
            'event_type': 'eventType',
            'category': 'category',
            'resource_type': 'resourceType',
            'muted': 'muted',
            'custom_data': 'customData'
        })
        return attributes

    @property
    def resolve(self):
        # type: () -> bool
        """Gets the resolve of this Notification.

        Notify when condition resolves after it was met

        :return: The resolve of this Notification.
        :rtype: bool
        """
        return self._resolve

    @resolve.setter
    def resolve(self, resolve):
        # type: (bool) -> None
        """Sets the resolve of this Notification.

        Notify when condition resolves after it was met

        :param resolve: The resolve of this Notification.
        :type: bool
        """

        if resolve is not None:
            if not isinstance(resolve, bool):
                raise TypeError("Invalid type for `resolve`, type has to be `bool`")

        self._resolve = resolve

    @property
    def resource_id(self):
        # type: () -> string_types
        """Gets the resource_id of this Notification.

        Specific resource, e.g. encoding id

        :return: The resource_id of this Notification.
        :rtype: string_types
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        # type: (string_types) -> None
        """Sets the resource_id of this Notification.

        Specific resource, e.g. encoding id

        :param resource_id: The resource_id of this Notification.
        :type: string_types
        """

        if resource_id is not None:
            if not isinstance(resource_id, string_types):
                raise TypeError("Invalid type for `resource_id`, type has to be `string_types`")

        self._resource_id = resource_id

    @property
    def triggered_at(self):
        # type: () -> datetime
        """Gets the triggered_at of this Notification.

        Last time the notification was triggered

        :return: The triggered_at of this Notification.
        :rtype: datetime
        """
        return self._triggered_at

    @triggered_at.setter
    def triggered_at(self, triggered_at):
        # type: (datetime) -> None
        """Sets the triggered_at of this Notification.

        Last time the notification was triggered

        :param triggered_at: The triggered_at of this Notification.
        :type: datetime
        """

        if triggered_at is not None:
            if not isinstance(triggered_at, datetime):
                raise TypeError("Invalid type for `triggered_at`, type has to be `datetime`")

        self._triggered_at = triggered_at

    @property
    def type(self):
        # type: () -> string_types
        """Gets the type of this Notification.


        :return: The type of this Notification.
        :rtype: string_types
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (string_types) -> None
        """Sets the type of this Notification.


        :param type_: The type of this Notification.
        :type: string_types
        """

        if type_ is not None:
            if not isinstance(type_, string_types):
                raise TypeError("Invalid type for `type`, type has to be `string_types`")

        self._type = type_

    @property
    def event_type(self):
        # type: () -> string_types
        """Gets the event_type of this Notification.


        :return: The event_type of this Notification.
        :rtype: string_types
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        # type: (string_types) -> None
        """Sets the event_type of this Notification.


        :param event_type: The event_type of this Notification.
        :type: string_types
        """

        if event_type is not None:
            if not isinstance(event_type, string_types):
                raise TypeError("Invalid type for `event_type`, type has to be `string_types`")

        self._event_type = event_type

    @property
    def category(self):
        # type: () -> string_types
        """Gets the category of this Notification.


        :return: The category of this Notification.
        :rtype: string_types
        """
        return self._category

    @category.setter
    def category(self, category):
        # type: (string_types) -> None
        """Sets the category of this Notification.


        :param category: The category of this Notification.
        :type: string_types
        """

        if category is not None:
            if not isinstance(category, string_types):
                raise TypeError("Invalid type for `category`, type has to be `string_types`")

        self._category = category

    @property
    def resource_type(self):
        # type: () -> string_types
        """Gets the resource_type of this Notification.


        :return: The resource_type of this Notification.
        :rtype: string_types
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        # type: (string_types) -> None
        """Sets the resource_type of this Notification.


        :param resource_type: The resource_type of this Notification.
        :type: string_types
        """

        if resource_type is not None:
            if not isinstance(resource_type, string_types):
                raise TypeError("Invalid type for `resource_type`, type has to be `string_types`")

        self._resource_type = resource_type

    @property
    def muted(self):
        # type: () -> bool
        """Gets the muted of this Notification.


        :return: The muted of this Notification.
        :rtype: bool
        """
        return self._muted

    @muted.setter
    def muted(self, muted):
        # type: (bool) -> None
        """Sets the muted of this Notification.


        :param muted: The muted of this Notification.
        :type: bool
        """

        if muted is not None:
            if not isinstance(muted, bool):
                raise TypeError("Invalid type for `muted`, type has to be `bool`")

        self._muted = muted

    @property
    def custom_data(self):
        # type: () -> dict(str, object)
        """Gets the custom_data of this Notification.

        User-specific meta data. This can hold anything.

        :return: The custom_data of this Notification.
        :rtype: dict(str, object)
        """
        return self._custom_data

    @custom_data.setter
    def custom_data(self, custom_data):
        # type: (dict) -> None
        """Sets the custom_data of this Notification.

        User-specific meta data. This can hold anything.

        :param custom_data: The custom_data of this Notification.
        :type: dict(str, object)
        """

        if custom_data is not None:
            if not isinstance(custom_data, dict):
                raise TypeError("Invalid type for `custom_data`, type has to be `dict(str, object)`")

        self._custom_data = custom_data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Notification, self), "to_dict"):
            result = super(Notification, self).to_dict()
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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
