# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AgentChatAttachment(object):
    @poscheck_model
    def __init__(self,
                 kind=None,
                 tool_call_id=None,
                 attributes=None):
        # type: (string_types, string_types, dict) -> None

        self._kind = None
        self._tool_call_id = None
        self._attributes = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if tool_call_id is not None:
            self.tool_call_id = tool_call_id
        if attributes is not None:
            self.attributes = attributes

    @property
    def openapi_types(self):
        types = {
            'kind': 'string_types',
            'tool_call_id': 'string_types',
            'attributes': 'dict(str, object)'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'kind': 'kind',
            'tool_call_id': 'toolCallId',
            'attributes': 'attributes'
        }
        return attributes

    @property
    def kind(self):
        # type: () -> string_types
        """Gets the kind of this AgentChatAttachment.

        Attachment kind (required)

        :return: The kind of this AgentChatAttachment.
        :rtype: string_types
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        # type: (string_types) -> None
        """Sets the kind of this AgentChatAttachment.

        Attachment kind (required)

        :param kind: The kind of this AgentChatAttachment.
        :type: string_types
        """

        if kind is not None:
            if not isinstance(kind, string_types):
                raise TypeError("Invalid type for `kind`, type has to be `string_types`")

        self._kind = kind

    @property
    def tool_call_id(self):
        # type: () -> string_types
        """Gets the tool_call_id of this AgentChatAttachment.

        Tool call identifier

        :return: The tool_call_id of this AgentChatAttachment.
        :rtype: string_types
        """
        return self._tool_call_id

    @tool_call_id.setter
    def tool_call_id(self, tool_call_id):
        # type: (string_types) -> None
        """Sets the tool_call_id of this AgentChatAttachment.

        Tool call identifier

        :param tool_call_id: The tool_call_id of this AgentChatAttachment.
        :type: string_types
        """

        if tool_call_id is not None:
            if not isinstance(tool_call_id, string_types):
                raise TypeError("Invalid type for `tool_call_id`, type has to be `string_types`")

        self._tool_call_id = tool_call_id

    @property
    def attributes(self):
        # type: () -> dict(str, object)
        """Gets the attributes of this AgentChatAttachment.

        Attachment attributes map (required)

        :return: The attributes of this AgentChatAttachment.
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        # type: (dict) -> None
        """Sets the attributes of this AgentChatAttachment.

        Attachment attributes map (required)

        :param attributes: The attributes of this AgentChatAttachment.
        :type: dict(str, object)
        """

        if attributes is not None:
            if not isinstance(attributes, dict):
                raise TypeError("Invalid type for `attributes`, type has to be `dict(str, object)`")

        self._attributes = attributes

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
        if not isinstance(other, AgentChatAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
