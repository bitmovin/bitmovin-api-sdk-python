# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.agent_chat_attachments_data import AgentChatAttachmentsData
from bitmovin_api_sdk.models.agent_chat_message_part import AgentChatMessagePart
import pprint
import six


class AgentChatAttachmentsPart(AgentChatMessagePart):
    @poscheck_model
    def __init__(self,
                 data=None):
        # type: (AgentChatAttachmentsData) -> None
        super(AgentChatAttachmentsPart, self).__init__()

        self._data = None
        self.discriminator = None

        if data is not None:
            self.data = data

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AgentChatAttachmentsPart, self), 'openapi_types'):
            types = getattr(super(AgentChatAttachmentsPart, self), 'openapi_types')

        types.update({
            'data': 'AgentChatAttachmentsData'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AgentChatAttachmentsPart, self), 'attribute_map'):
            attributes = getattr(super(AgentChatAttachmentsPart, self), 'attribute_map')

        attributes.update({
            'data': 'data'
        })
        return attributes

    @property
    def data(self):
        # type: () -> AgentChatAttachmentsData
        """Gets the data of this AgentChatAttachmentsPart.

        Attachment payload (required)

        :return: The data of this AgentChatAttachmentsPart.
        :rtype: AgentChatAttachmentsData
        """
        return self._data

    @data.setter
    def data(self, data):
        # type: (AgentChatAttachmentsData) -> None
        """Sets the data of this AgentChatAttachmentsPart.

        Attachment payload (required)

        :param data: The data of this AgentChatAttachmentsPart.
        :type: AgentChatAttachmentsData
        """

        if data is not None:
            if not isinstance(data, AgentChatAttachmentsData):
                raise TypeError("Invalid type for `data`, type has to be `AgentChatAttachmentsData`")

        self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AgentChatAttachmentsPart, self), "to_dict"):
            result = super(AgentChatAttachmentsPart, self).to_dict()
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
        if not isinstance(other, AgentChatAttachmentsPart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
