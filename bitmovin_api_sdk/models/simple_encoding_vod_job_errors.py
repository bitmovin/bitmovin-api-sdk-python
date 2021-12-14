# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class SimpleEncodingVodJobErrors(object):
    @poscheck_model
    def __init__(self,
                 error_code=None,
                 message=None,
                 details=None):
        # type: (string_types, string_types, string_types) -> None

        self._error_code = None
        self._message = None
        self._details = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if message is not None:
            self.message = message
        if details is not None:
            self.details = details

    @property
    def openapi_types(self):
        types = {
            'error_code': 'string_types',
            'message': 'string_types',
            'details': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'error_code': 'errorCode',
            'message': 'message',
            'details': 'details'
        }
        return attributes

    @property
    def error_code(self):
        # type: () -> string_types
        """Gets the error_code of this SimpleEncodingVodJobErrors.

        Stable code that identifies the error type.

        :return: The error_code of this SimpleEncodingVodJobErrors.
        :rtype: string_types
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        # type: (string_types) -> None
        """Sets the error_code of this SimpleEncodingVodJobErrors.

        Stable code that identifies the error type.

        :param error_code: The error_code of this SimpleEncodingVodJobErrors.
        :type: string_types
        """

        if error_code is not None:
            if not isinstance(error_code, string_types):
                raise TypeError("Invalid type for `error_code`, type has to be `string_types`")

        self._error_code = error_code

    @property
    def message(self):
        # type: () -> string_types
        """Gets the message of this SimpleEncodingVodJobErrors.

        Human readable description of the error.

        :return: The message of this SimpleEncodingVodJobErrors.
        :rtype: string_types
        """
        return self._message

    @message.setter
    def message(self, message):
        # type: (string_types) -> None
        """Sets the message of this SimpleEncodingVodJobErrors.

        Human readable description of the error.

        :param message: The message of this SimpleEncodingVodJobErrors.
        :type: string_types
        """

        if message is not None:
            if not isinstance(message, string_types):
                raise TypeError("Invalid type for `message`, type has to be `string_types`")

        self._message = message

    @property
    def details(self):
        # type: () -> string_types
        """Gets the details of this SimpleEncodingVodJobErrors.

        Additional details of the error if available.

        :return: The details of this SimpleEncodingVodJobErrors.
        :rtype: string_types
        """
        return self._details

    @details.setter
    def details(self, details):
        # type: (string_types) -> None
        """Sets the details of this SimpleEncodingVodJobErrors.

        Additional details of the error if available.

        :param details: The details of this SimpleEncodingVodJobErrors.
        :type: string_types
        """

        if details is not None:
            if not isinstance(details, string_types):
                raise TypeError("Invalid type for `details`, type has to be `string_types`")

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
        if not isinstance(other, SimpleEncodingVodJobErrors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
