# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.message_type import MessageType
import pprint
import six


class Message(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 type_=None,
                 text=None,
                 field=None,
                 links=None,
                 more=None,
                 date_=None):
        # type: (string_types, MessageType, string_types, string_types, list[Link], object, datetime) -> None
        super(Message, self).__init__(id_=id_)

        self._type = None
        self._text = None
        self._field = None
        self._links = list()
        self._more = None
        self._date = None
        self.discriminator = None

        if type_ is not None:
            self.type = type_
        if text is not None:
            self.text = text
        if field is not None:
            self.field = field
        if links is not None:
            self.links = links
        if more is not None:
            self.more = more
        if date_ is not None:
            self.date = date_

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Message, self), 'openapi_types'):
            types = getattr(super(Message, self), 'openapi_types')

        types.update({
            'type': 'MessageType',
            'text': 'string_types',
            'field': 'string_types',
            'links': 'list[Link]',
            'more': 'object',
            'date': 'datetime'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Message, self), 'attribute_map'):
            attributes = getattr(super(Message, self), 'attribute_map')

        attributes.update({
            'type': 'type',
            'text': 'text',
            'field': 'field',
            'links': 'links',
            'more': 'more',
            'date': 'date'
        })
        return attributes

    @property
    def type(self):
        # type: () -> MessageType
        """Gets the type of this Message.

        Message type giving a hint on the importance of the message (log level) (required)

        :return: The type of this Message.
        :rtype: MessageType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (MessageType) -> None
        """Sets the type of this Message.

        Message type giving a hint on the importance of the message (log level) (required)

        :param type_: The type of this Message.
        :type: MessageType
        """

        if type_ is not None:
            if not isinstance(type_, MessageType):
                raise TypeError("Invalid type for `type`, type has to be `MessageType`")

        self._type = type_

    @property
    def text(self):
        # type: () -> string_types
        """Gets the text of this Message.

        Message text (required)

        :return: The text of this Message.
        :rtype: string_types
        """
        return self._text

    @text.setter
    def text(self, text):
        # type: (string_types) -> None
        """Sets the text of this Message.

        Message text (required)

        :param text: The text of this Message.
        :type: string_types
        """

        if text is not None:
            if not isinstance(text, string_types):
                raise TypeError("Invalid type for `text`, type has to be `string_types`")

        self._text = text

    @property
    def field(self):
        # type: () -> string_types
        """Gets the field of this Message.

        Name of the field to which the message is referring to

        :return: The field of this Message.
        :rtype: string_types
        """
        return self._field

    @field.setter
    def field(self, field):
        # type: (string_types) -> None
        """Sets the field of this Message.

        Name of the field to which the message is referring to

        :param field: The field of this Message.
        :type: string_types
        """

        if field is not None:
            if not isinstance(field, string_types):
                raise TypeError("Invalid type for `field`, type has to be `string_types`")

        self._field = field

    @property
    def links(self):
        # type: () -> list[Link]
        """Gets the links of this Message.

        collection of links to webpages containing further information on the topic

        :return: The links of this Message.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        # type: (list) -> None
        """Sets the links of this Message.

        collection of links to webpages containing further information on the topic

        :param links: The links of this Message.
        :type: list[Link]
        """

        if links is not None:
            if not isinstance(links, list):
                raise TypeError("Invalid type for `links`, type has to be `list[Link]`")

        self._links = links

    @property
    def more(self):
        # type: () -> object
        """Gets the more of this Message.

        Service-specific information

        :return: The more of this Message.
        :rtype: object
        """
        return self._more

    @more.setter
    def more(self, more):
        # type: (object) -> None
        """Sets the more of this Message.

        Service-specific information

        :param more: The more of this Message.
        :type: object
        """

        if more is not None:
            if not isinstance(more, object):
                raise TypeError("Invalid type for `more`, type has to be `object`")

        self._more = more

    @property
    def date(self):
        # type: () -> datetime
        """Gets the date of this Message.

        Timestamp when the message occured

        :return: The date of this Message.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date_):
        # type: (datetime) -> None
        """Sets the date of this Message.

        Timestamp when the message occured

        :param date_: The date of this Message.
        :type: datetime
        """

        if date_ is not None:
            if not isinstance(date_, datetime):
                raise TypeError("Invalid type for `date`, type has to be `datetime`")

        self._date = date_

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Message, self), "to_dict"):
            result = super(Message, self).to_dict()
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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
