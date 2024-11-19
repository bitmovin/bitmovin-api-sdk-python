# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.live_standby_pool_event_log_type import LiveStandbyPoolEventLogType
import pprint
import six


class LiveStandbyPoolEventLog(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 standby_pool_id=None,
                 standby_pool_encoding_id=None,
                 created_at=None,
                 message=None,
                 details=None,
                 event_type=None):
        # type: (string_types, string_types, string_types, string_types, string_types, string_types, LiveStandbyPoolEventLogType) -> None

        self._id = None
        self._standby_pool_id = None
        self._standby_pool_encoding_id = None
        self._created_at = None
        self._message = None
        self._details = None
        self._event_type = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if standby_pool_id is not None:
            self.standby_pool_id = standby_pool_id
        if standby_pool_encoding_id is not None:
            self.standby_pool_encoding_id = standby_pool_encoding_id
        if created_at is not None:
            self.created_at = created_at
        if message is not None:
            self.message = message
        if details is not None:
            self.details = details
        if event_type is not None:
            self.event_type = event_type

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'standby_pool_id': 'string_types',
            'standby_pool_encoding_id': 'string_types',
            'created_at': 'string_types',
            'message': 'string_types',
            'details': 'string_types',
            'event_type': 'LiveStandbyPoolEventLogType'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'standby_pool_id': 'standbyPoolId',
            'standby_pool_encoding_id': 'standbyPoolEncodingId',
            'created_at': 'createdAt',
            'message': 'message',
            'details': 'details',
            'event_type': 'eventType'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this LiveStandbyPoolEventLog.

        UUID of the entry

        :return: The id of this LiveStandbyPoolEventLog.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this LiveStandbyPoolEventLog.

        UUID of the entry

        :param id_: The id of this LiveStandbyPoolEventLog.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def standby_pool_id(self):
        # type: () -> string_types
        """Gets the standby_pool_id of this LiveStandbyPoolEventLog.

        Id of the standby_pool associated with the event log

        :return: The standby_pool_id of this LiveStandbyPoolEventLog.
        :rtype: string_types
        """
        return self._standby_pool_id

    @standby_pool_id.setter
    def standby_pool_id(self, standby_pool_id):
        # type: (string_types) -> None
        """Sets the standby_pool_id of this LiveStandbyPoolEventLog.

        Id of the standby_pool associated with the event log

        :param standby_pool_id: The standby_pool_id of this LiveStandbyPoolEventLog.
        :type: string_types
        """

        if standby_pool_id is not None:
            if not isinstance(standby_pool_id, string_types):
                raise TypeError("Invalid type for `standby_pool_id`, type has to be `string_types`")

        self._standby_pool_id = standby_pool_id

    @property
    def standby_pool_encoding_id(self):
        # type: () -> string_types
        """Gets the standby_pool_encoding_id of this LiveStandbyPoolEventLog.

        (Optional) Id of the standby pool encoding associated with the event

        :return: The standby_pool_encoding_id of this LiveStandbyPoolEventLog.
        :rtype: string_types
        """
        return self._standby_pool_encoding_id

    @standby_pool_encoding_id.setter
    def standby_pool_encoding_id(self, standby_pool_encoding_id):
        # type: (string_types) -> None
        """Sets the standby_pool_encoding_id of this LiveStandbyPoolEventLog.

        (Optional) Id of the standby pool encoding associated with the event

        :param standby_pool_encoding_id: The standby_pool_encoding_id of this LiveStandbyPoolEventLog.
        :type: string_types
        """

        if standby_pool_encoding_id is not None:
            if not isinstance(standby_pool_encoding_id, string_types):
                raise TypeError("Invalid type for `standby_pool_encoding_id`, type has to be `string_types`")

        self._standby_pool_encoding_id = standby_pool_encoding_id

    @property
    def created_at(self):
        # type: () -> string_types
        """Gets the created_at of this LiveStandbyPoolEventLog.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The created_at of this LiveStandbyPoolEventLog.
        :rtype: string_types
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (string_types) -> None
        """Sets the created_at of this LiveStandbyPoolEventLog.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param created_at: The created_at of this LiveStandbyPoolEventLog.
        :type: string_types
        """

        if created_at is not None:
            if not isinstance(created_at, string_types):
                raise TypeError("Invalid type for `created_at`, type has to be `string_types`")

        self._created_at = created_at

    @property
    def message(self):
        # type: () -> string_types
        """Gets the message of this LiveStandbyPoolEventLog.

        Short description of the event

        :return: The message of this LiveStandbyPoolEventLog.
        :rtype: string_types
        """
        return self._message

    @message.setter
    def message(self, message):
        # type: (string_types) -> None
        """Sets the message of this LiveStandbyPoolEventLog.

        Short description of the event

        :param message: The message of this LiveStandbyPoolEventLog.
        :type: string_types
        """

        if message is not None:
            if not isinstance(message, string_types):
                raise TypeError("Invalid type for `message`, type has to be `string_types`")

        self._message = message

    @property
    def details(self):
        # type: () -> string_types
        """Gets the details of this LiveStandbyPoolEventLog.

        Detailed description, payloads, hints on how to resolve errors, etc

        :return: The details of this LiveStandbyPoolEventLog.
        :rtype: string_types
        """
        return self._details

    @details.setter
    def details(self, details):
        # type: (string_types) -> None
        """Sets the details of this LiveStandbyPoolEventLog.

        Detailed description, payloads, hints on how to resolve errors, etc

        :param details: The details of this LiveStandbyPoolEventLog.
        :type: string_types
        """

        if details is not None:
            if not isinstance(details, string_types):
                raise TypeError("Invalid type for `details`, type has to be `string_types`")

        self._details = details

    @property
    def event_type(self):
        # type: () -> LiveStandbyPoolEventLogType
        """Gets the event_type of this LiveStandbyPoolEventLog.


        :return: The event_type of this LiveStandbyPoolEventLog.
        :rtype: LiveStandbyPoolEventLogType
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        # type: (LiveStandbyPoolEventLogType) -> None
        """Sets the event_type of this LiveStandbyPoolEventLog.


        :param event_type: The event_type of this LiveStandbyPoolEventLog.
        :type: LiveStandbyPoolEventLogType
        """

        if event_type is not None:
            if not isinstance(event_type, LiveStandbyPoolEventLogType):
                raise TypeError("Invalid type for `event_type`, type has to be `LiveStandbyPoolEventLogType`")

        self._event_type = event_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

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
        if not isinstance(other, LiveStandbyPoolEventLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
