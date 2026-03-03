# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AgentChatMessage(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 role=None,
                 parts=None):
        # type: (string_types, string_types, list[AgentChatMessagePart]) -> None

        self._id = None
        self._role = None
        self._parts = list()
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if role is not None:
            self.role = role
        if parts is not None:
            self.parts = parts

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'role': 'string_types',
            'parts': 'list[AgentChatMessagePart]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'role': 'role',
            'parts': 'parts'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this AgentChatMessage.

        Message ID (required)

        :return: The id of this AgentChatMessage.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this AgentChatMessage.

        Message ID (required)

        :param id_: The id of this AgentChatMessage.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def role(self):
        # type: () -> string_types
        """Gets the role of this AgentChatMessage.

        Message role (required)

        :return: The role of this AgentChatMessage.
        :rtype: string_types
        """
        return self._role

    @role.setter
    def role(self, role):
        # type: (string_types) -> None
        """Sets the role of this AgentChatMessage.

        Message role (required)

        :param role: The role of this AgentChatMessage.
        :type: string_types
        """

        if role is not None:
            if not isinstance(role, string_types):
                raise TypeError("Invalid type for `role`, type has to be `string_types`")

        self._role = role

    @property
    def parts(self):
        # type: () -> list[AgentChatMessagePart]
        """Gets the parts of this AgentChatMessage.

        Message parts (required)

        :return: The parts of this AgentChatMessage.
        :rtype: list[AgentChatMessagePart]
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        # type: (list) -> None
        """Sets the parts of this AgentChatMessage.

        Message parts (required)

        :param parts: The parts of this AgentChatMessage.
        :type: list[AgentChatMessagePart]
        """

        if parts is not None:
            if not isinstance(parts, list):
                raise TypeError("Invalid type for `parts`, type has to be `list[AgentChatMessagePart]`")

        self._parts = parts

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
        if not isinstance(other, AgentChatMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
