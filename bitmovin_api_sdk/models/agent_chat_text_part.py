# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.agent_chat_message_part import AgentChatMessagePart
import pprint
import six


class AgentChatTextPart(AgentChatMessagePart):
    @poscheck_model
    def __init__(self,
                 text=None):
        # type: (string_types) -> None
        super(AgentChatTextPart, self).__init__()

        self._text = None
        self.discriminator = None

        if text is not None:
            self.text = text

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AgentChatTextPart, self), 'openapi_types'):
            types = getattr(super(AgentChatTextPart, self), 'openapi_types')

        types.update({
            'text': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AgentChatTextPart, self), 'attribute_map'):
            attributes = getattr(super(AgentChatTextPart, self), 'attribute_map')

        attributes.update({
            'text': 'text'
        })
        return attributes

    @property
    def text(self):
        # type: () -> string_types
        """Gets the text of this AgentChatTextPart.

        Text message content (required)

        :return: The text of this AgentChatTextPart.
        :rtype: string_types
        """
        return self._text

    @text.setter
    def text(self, text):
        # type: (string_types) -> None
        """Sets the text of this AgentChatTextPart.

        Text message content (required)

        :param text: The text of this AgentChatTextPart.
        :type: string_types
        """

        if text is not None:
            if not isinstance(text, string_types):
                raise TypeError("Invalid type for `text`, type has to be `string_types`")

        self._text = text

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AgentChatTextPart, self), "to_dict"):
            result = super(AgentChatTextPart, self).to_dict()
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
        if not isinstance(other, AgentChatTextPart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
