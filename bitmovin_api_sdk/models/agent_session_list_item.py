# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AgentSessionListItem(object):
    @poscheck_model
    def __init__(self,
                 session_id=None,
                 title=None,
                 last_update_time_seconds=None):
        # type: (string_types, string_types, float) -> None

        self._session_id = None
        self._title = None
        self._last_update_time_seconds = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if title is not None:
            self.title = title
        if last_update_time_seconds is not None:
            self.last_update_time_seconds = last_update_time_seconds

    @property
    def openapi_types(self):
        types = {
            'session_id': 'string_types',
            'title': 'string_types',
            'last_update_time_seconds': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'session_id': 'sessionId',
            'title': 'title',
            'last_update_time_seconds': 'lastUpdateTimeSeconds'
        }
        return attributes

    @property
    def session_id(self):
        # type: () -> string_types
        """Gets the session_id of this AgentSessionListItem.

        Session ID (required)

        :return: The session_id of this AgentSessionListItem.
        :rtype: string_types
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        # type: (string_types) -> None
        """Sets the session_id of this AgentSessionListItem.

        Session ID (required)

        :param session_id: The session_id of this AgentSessionListItem.
        :type: string_types
        """

        if session_id is not None:
            if not isinstance(session_id, string_types):
                raise TypeError("Invalid type for `session_id`, type has to be `string_types`")

        self._session_id = session_id

    @property
    def title(self):
        # type: () -> string_types
        """Gets the title of this AgentSessionListItem.

        Session title

        :return: The title of this AgentSessionListItem.
        :rtype: string_types
        """
        return self._title

    @title.setter
    def title(self, title):
        # type: (string_types) -> None
        """Sets the title of this AgentSessionListItem.

        Session title

        :param title: The title of this AgentSessionListItem.
        :type: string_types
        """

        if title is not None:
            if not isinstance(title, string_types):
                raise TypeError("Invalid type for `title`, type has to be `string_types`")

        self._title = title

    @property
    def last_update_time_seconds(self):
        # type: () -> float
        """Gets the last_update_time_seconds of this AgentSessionListItem.

        Last update time in seconds

        :return: The last_update_time_seconds of this AgentSessionListItem.
        :rtype: float
        """
        return self._last_update_time_seconds

    @last_update_time_seconds.setter
    def last_update_time_seconds(self, last_update_time_seconds):
        # type: (float) -> None
        """Sets the last_update_time_seconds of this AgentSessionListItem.

        Last update time in seconds

        :param last_update_time_seconds: The last_update_time_seconds of this AgentSessionListItem.
        :type: float
        """

        if last_update_time_seconds is not None:
            if not isinstance(last_update_time_seconds, (float, int)):
                raise TypeError("Invalid type for `last_update_time_seconds`, type has to be `float`")

        self._last_update_time_seconds = last_update_time_seconds

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
        if not isinstance(other, AgentSessionListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
