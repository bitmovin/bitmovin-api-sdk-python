# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class ResponseErrorData(object):
    @poscheck_model
    def __init__(self,
                 code=None,
                 message=None,
                 developer_message=None,
                 links=None,
                 details=None):
        # type: (int, string_types, string_types, list[Link], list[Message]) -> None

        self._code = None
        self._message = None
        self._developer_message = None
        self._links = list()
        self._details = list()
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if developer_message is not None:
            self.developer_message = developer_message
        if links is not None:
            self.links = links
        if details is not None:
            self.details = details

    @property
    def openapi_types(self):
        types = {
            'code': 'int',
            'message': 'string_types',
            'developer_message': 'string_types',
            'links': 'list[Link]',
            'details': 'list[Message]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'code': 'code',
            'message': 'message',
            'developer_message': 'developerMessage',
            'links': 'links',
            'details': 'details'
        }
        return attributes

    @property
    def code(self):
        # type: () -> int
        """Gets the code of this ResponseErrorData.

        Contains an error code as defined in https://bitmovin.com/encoding-documentation/bitmovin-api/#/introduction/api-error-codes (required)

        :return: The code of this ResponseErrorData.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        # type: (int) -> None
        """Sets the code of this ResponseErrorData.

        Contains an error code as defined in https://bitmovin.com/encoding-documentation/bitmovin-api/#/introduction/api-error-codes (required)

        :param code: The code of this ResponseErrorData.
        :type: int
        """

        if code is not None:
            if not isinstance(code, int):
                raise TypeError("Invalid type for `code`, type has to be `int`")

        self._code = code

    @property
    def message(self):
        # type: () -> string_types
        """Gets the message of this ResponseErrorData.

        General error message (required)

        :return: The message of this ResponseErrorData.
        :rtype: string_types
        """
        return self._message

    @message.setter
    def message(self, message):
        # type: (string_types) -> None
        """Sets the message of this ResponseErrorData.

        General error message (required)

        :param message: The message of this ResponseErrorData.
        :type: string_types
        """

        if message is not None:
            if not isinstance(message, string_types):
                raise TypeError("Invalid type for `message`, type has to be `string_types`")

        self._message = message

    @property
    def developer_message(self):
        # type: () -> string_types
        """Gets the developer_message of this ResponseErrorData.

        More detailed message meant for developers (required)

        :return: The developer_message of this ResponseErrorData.
        :rtype: string_types
        """
        return self._developer_message

    @developer_message.setter
    def developer_message(self, developer_message):
        # type: (string_types) -> None
        """Sets the developer_message of this ResponseErrorData.

        More detailed message meant for developers (required)

        :param developer_message: The developer_message of this ResponseErrorData.
        :type: string_types
        """

        if developer_message is not None:
            if not isinstance(developer_message, string_types):
                raise TypeError("Invalid type for `developer_message`, type has to be `string_types`")

        self._developer_message = developer_message

    @property
    def links(self):
        # type: () -> list[Link]
        """Gets the links of this ResponseErrorData.

        collection of links to webpages containing further information on the topic

        :return: The links of this ResponseErrorData.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        # type: (list) -> None
        """Sets the links of this ResponseErrorData.

        collection of links to webpages containing further information on the topic

        :param links: The links of this ResponseErrorData.
        :type: list[Link]
        """

        if links is not None:
            if not isinstance(links, list):
                raise TypeError("Invalid type for `links`, type has to be `list[Link]`")

        self._links = links

    @property
    def details(self):
        # type: () -> list[Message]
        """Gets the details of this ResponseErrorData.

        collection of messages containing more detailed information on the cause of the error

        :return: The details of this ResponseErrorData.
        :rtype: list[Message]
        """
        return self._details

    @details.setter
    def details(self, details):
        # type: (list) -> None
        """Sets the details of this ResponseErrorData.

        collection of messages containing more detailed information on the cause of the error

        :param details: The details of this ResponseErrorData.
        :type: list[Message]
        """

        if details is not None:
            if not isinstance(details, list):
                raise TypeError("Invalid type for `details`, type has to be `list[Message]`")

        self._details = details

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
        if not isinstance(other, ResponseErrorData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
