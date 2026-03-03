# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AgentSessionHistoryResponse(object):
    @poscheck_model
    def __init__(self,
                 session_id=None,
                 app_name=None,
                 user_id=None,
                 title=None,
                 messages=None):
        # type: (string_types, string_types, string_types, string_types, list[AgentChatMessage]) -> None

        self._session_id = None
        self._app_name = None
        self._user_id = None
        self._title = None
        self._messages = list()
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if app_name is not None:
            self.app_name = app_name
        if user_id is not None:
            self.user_id = user_id
        if title is not None:
            self.title = title
        if messages is not None:
            self.messages = messages

    @property
    def openapi_types(self):
        types = {
            'session_id': 'string_types',
            'app_name': 'string_types',
            'user_id': 'string_types',
            'title': 'string_types',
            'messages': 'list[AgentChatMessage]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'session_id': 'sessionId',
            'app_name': 'appName',
            'user_id': 'userId',
            'title': 'title',
            'messages': 'messages'
        }
        return attributes

    @property
    def session_id(self):
        # type: () -> string_types
        """Gets the session_id of this AgentSessionHistoryResponse.

        Session ID (required)

        :return: The session_id of this AgentSessionHistoryResponse.
        :rtype: string_types
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        # type: (string_types) -> None
        """Sets the session_id of this AgentSessionHistoryResponse.

        Session ID (required)

        :param session_id: The session_id of this AgentSessionHistoryResponse.
        :type: string_types
        """

        if session_id is not None:
            if not isinstance(session_id, string_types):
                raise TypeError("Invalid type for `session_id`, type has to be `string_types`")

        self._session_id = session_id

    @property
    def app_name(self):
        # type: () -> string_types
        """Gets the app_name of this AgentSessionHistoryResponse.

        Agent application name (required)

        :return: The app_name of this AgentSessionHistoryResponse.
        :rtype: string_types
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        # type: (string_types) -> None
        """Sets the app_name of this AgentSessionHistoryResponse.

        Agent application name (required)

        :param app_name: The app_name of this AgentSessionHistoryResponse.
        :type: string_types
        """

        if app_name is not None:
            if not isinstance(app_name, string_types):
                raise TypeError("Invalid type for `app_name`, type has to be `string_types`")

        self._app_name = app_name

    @property
    def user_id(self):
        # type: () -> string_types
        """Gets the user_id of this AgentSessionHistoryResponse.

        User ID (required)

        :return: The user_id of this AgentSessionHistoryResponse.
        :rtype: string_types
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        # type: (string_types) -> None
        """Sets the user_id of this AgentSessionHistoryResponse.

        User ID (required)

        :param user_id: The user_id of this AgentSessionHistoryResponse.
        :type: string_types
        """

        if user_id is not None:
            if not isinstance(user_id, string_types):
                raise TypeError("Invalid type for `user_id`, type has to be `string_types`")

        self._user_id = user_id

    @property
    def title(self):
        # type: () -> string_types
        """Gets the title of this AgentSessionHistoryResponse.

        Session title

        :return: The title of this AgentSessionHistoryResponse.
        :rtype: string_types
        """
        return self._title

    @title.setter
    def title(self, title):
        # type: (string_types) -> None
        """Sets the title of this AgentSessionHistoryResponse.

        Session title

        :param title: The title of this AgentSessionHistoryResponse.
        :type: string_types
        """

        if title is not None:
            if not isinstance(title, string_types):
                raise TypeError("Invalid type for `title`, type has to be `string_types`")

        self._title = title

    @property
    def messages(self):
        # type: () -> list[AgentChatMessage]
        """Gets the messages of this AgentSessionHistoryResponse.

        Session message history (required)

        :return: The messages of this AgentSessionHistoryResponse.
        :rtype: list[AgentChatMessage]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        # type: (list) -> None
        """Sets the messages of this AgentSessionHistoryResponse.

        Session message history (required)

        :param messages: The messages of this AgentSessionHistoryResponse.
        :type: list[AgentChatMessage]
        """

        if messages is not None:
            if not isinstance(messages, list):
                raise TypeError("Invalid type for `messages`, type has to be `list[AgentChatMessage]`")

        self._messages = messages

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
        if not isinstance(other, AgentSessionHistoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
