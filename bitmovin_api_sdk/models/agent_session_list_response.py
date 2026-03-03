# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AgentSessionListResponse(object):
    @poscheck_model
    def __init__(self,
                 app_name=None,
                 user_id=None,
                 sessions=None):
        # type: (string_types, string_types, list[AgentSessionListItem]) -> None

        self._app_name = None
        self._user_id = None
        self._sessions = list()
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if user_id is not None:
            self.user_id = user_id
        if sessions is not None:
            self.sessions = sessions

    @property
    def openapi_types(self):
        types = {
            'app_name': 'string_types',
            'user_id': 'string_types',
            'sessions': 'list[AgentSessionListItem]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'app_name': 'appName',
            'user_id': 'userId',
            'sessions': 'sessions'
        }
        return attributes

    @property
    def app_name(self):
        # type: () -> string_types
        """Gets the app_name of this AgentSessionListResponse.

        Agent application name (required)

        :return: The app_name of this AgentSessionListResponse.
        :rtype: string_types
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        # type: (string_types) -> None
        """Sets the app_name of this AgentSessionListResponse.

        Agent application name (required)

        :param app_name: The app_name of this AgentSessionListResponse.
        :type: string_types
        """

        if app_name is not None:
            if not isinstance(app_name, string_types):
                raise TypeError("Invalid type for `app_name`, type has to be `string_types`")

        self._app_name = app_name

    @property
    def user_id(self):
        # type: () -> string_types
        """Gets the user_id of this AgentSessionListResponse.

        User ID (required)

        :return: The user_id of this AgentSessionListResponse.
        :rtype: string_types
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        # type: (string_types) -> None
        """Sets the user_id of this AgentSessionListResponse.

        User ID (required)

        :param user_id: The user_id of this AgentSessionListResponse.
        :type: string_types
        """

        if user_id is not None:
            if not isinstance(user_id, string_types):
                raise TypeError("Invalid type for `user_id`, type has to be `string_types`")

        self._user_id = user_id

    @property
    def sessions(self):
        # type: () -> list[AgentSessionListItem]
        """Gets the sessions of this AgentSessionListResponse.

        Sessions for the user (required)

        :return: The sessions of this AgentSessionListResponse.
        :rtype: list[AgentSessionListItem]
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions):
        # type: (list) -> None
        """Sets the sessions of this AgentSessionListResponse.

        Sessions for the user (required)

        :param sessions: The sessions of this AgentSessionListResponse.
        :type: list[AgentSessionListItem]
        """

        if sessions is not None:
            if not isinstance(sessions, list):
                raise TypeError("Invalid type for `sessions`, type has to be `list[AgentSessionListItem]`")

        self._sessions = sessions

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
        if not isinstance(other, AgentSessionListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
