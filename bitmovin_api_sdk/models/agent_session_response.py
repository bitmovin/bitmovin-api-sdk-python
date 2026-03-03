# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AgentSessionResponse(object):
    @poscheck_model
    def __init__(self,
                 session_id=None,
                 app_name=None,
                 user_id=None):
        # type: (string_types, string_types, string_types) -> None

        self._session_id = None
        self._app_name = None
        self._user_id = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if app_name is not None:
            self.app_name = app_name
        if user_id is not None:
            self.user_id = user_id

    @property
    def openapi_types(self):
        types = {
            'session_id': 'string_types',
            'app_name': 'string_types',
            'user_id': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'session_id': 'sessionId',
            'app_name': 'appName',
            'user_id': 'userId'
        }
        return attributes

    @property
    def session_id(self):
        # type: () -> string_types
        """Gets the session_id of this AgentSessionResponse.

        Session ID (required)

        :return: The session_id of this AgentSessionResponse.
        :rtype: string_types
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        # type: (string_types) -> None
        """Sets the session_id of this AgentSessionResponse.

        Session ID (required)

        :param session_id: The session_id of this AgentSessionResponse.
        :type: string_types
        """

        if session_id is not None:
            if not isinstance(session_id, string_types):
                raise TypeError("Invalid type for `session_id`, type has to be `string_types`")

        self._session_id = session_id

    @property
    def app_name(self):
        # type: () -> string_types
        """Gets the app_name of this AgentSessionResponse.

        Agent application name (required)

        :return: The app_name of this AgentSessionResponse.
        :rtype: string_types
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        # type: (string_types) -> None
        """Sets the app_name of this AgentSessionResponse.

        Agent application name (required)

        :param app_name: The app_name of this AgentSessionResponse.
        :type: string_types
        """

        if app_name is not None:
            if not isinstance(app_name, string_types):
                raise TypeError("Invalid type for `app_name`, type has to be `string_types`")

        self._app_name = app_name

    @property
    def user_id(self):
        # type: () -> string_types
        """Gets the user_id of this AgentSessionResponse.

        User ID (required)

        :return: The user_id of this AgentSessionResponse.
        :rtype: string_types
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        # type: (string_types) -> None
        """Sets the user_id of this AgentSessionResponse.

        User ID (required)

        :param user_id: The user_id of this AgentSessionResponse.
        :type: string_types
        """

        if user_id is not None:
            if not isinstance(user_id, string_types):
                raise TypeError("Invalid type for `user_id`, type has to be `string_types`")

        self._user_id = user_id

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
        if not isinstance(other, AgentSessionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
