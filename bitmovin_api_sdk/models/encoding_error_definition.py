# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.error_retry_hint import ErrorRetryHint
import pprint
import six


class EncodingErrorDefinition(object):
    @poscheck_model
    def __init__(self,
                 code=None,
                 category=None,
                 message=None,
                 description=None,
                 retry_hint=None):
        # type: (int, string_types, string_types, string_types, ErrorRetryHint) -> None

        self._code = None
        self._category = None
        self._message = None
        self._description = None
        self._retry_hint = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if category is not None:
            self.category = category
        if message is not None:
            self.message = message
        if description is not None:
            self.description = description
        if retry_hint is not None:
            self.retry_hint = retry_hint

    @property
    def openapi_types(self):
        types = {
            'code': 'int',
            'category': 'string_types',
            'message': 'string_types',
            'description': 'string_types',
            'retry_hint': 'ErrorRetryHint'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'code': 'code',
            'category': 'category',
            'message': 'message',
            'description': 'description',
            'retry_hint': 'retryHint'
        }
        return attributes

    @property
    def code(self):
        # type: () -> int
        """Gets the code of this EncodingErrorDefinition.

        The error code.

        :return: The code of this EncodingErrorDefinition.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        # type: (int) -> None
        """Sets the code of this EncodingErrorDefinition.

        The error code.

        :param code: The code of this EncodingErrorDefinition.
        :type: int
        """

        if code is not None:
            if not isinstance(code, int):
                raise TypeError("Invalid type for `code`, type has to be `int`")

        self._code = code

    @property
    def category(self):
        # type: () -> string_types
        """Gets the category of this EncodingErrorDefinition.

        The error category.

        :return: The category of this EncodingErrorDefinition.
        :rtype: string_types
        """
        return self._category

    @category.setter
    def category(self, category):
        # type: (string_types) -> None
        """Sets the category of this EncodingErrorDefinition.

        The error category.

        :param category: The category of this EncodingErrorDefinition.
        :type: string_types
        """

        if category is not None:
            if not isinstance(category, string_types):
                raise TypeError("Invalid type for `category`, type has to be `string_types`")

        self._category = category

    @property
    def message(self):
        # type: () -> string_types
        """Gets the message of this EncodingErrorDefinition.

        The error message, optional. Can include placeholders like {1}, {2} which are replaced with the respective dependency when the error is thrown.

        :return: The message of this EncodingErrorDefinition.
        :rtype: string_types
        """
        return self._message

    @message.setter
    def message(self, message):
        # type: (string_types) -> None
        """Sets the message of this EncodingErrorDefinition.

        The error message, optional. Can include placeholders like {1}, {2} which are replaced with the respective dependency when the error is thrown.

        :param message: The message of this EncodingErrorDefinition.
        :type: string_types
        """

        if message is not None:
            if not isinstance(message, string_types):
                raise TypeError("Invalid type for `message`, type has to be `string_types`")

        self._message = message

    @property
    def description(self):
        # type: () -> string_types
        """Gets the description of this EncodingErrorDefinition.

        The returned error description.

        :return: The description of this EncodingErrorDefinition.
        :rtype: string_types
        """
        return self._description

    @description.setter
    def description(self, description):
        # type: (string_types) -> None
        """Sets the description of this EncodingErrorDefinition.

        The returned error description.

        :param description: The description of this EncodingErrorDefinition.
        :type: string_types
        """

        if description is not None:
            if not isinstance(description, string_types):
                raise TypeError("Invalid type for `description`, type has to be `string_types`")

        self._description = description

    @property
    def retry_hint(self):
        # type: () -> ErrorRetryHint
        """Gets the retry_hint of this EncodingErrorDefinition.

        Indicates if the call that caused the error should be retried.

        :return: The retry_hint of this EncodingErrorDefinition.
        :rtype: ErrorRetryHint
        """
        return self._retry_hint

    @retry_hint.setter
    def retry_hint(self, retry_hint):
        # type: (ErrorRetryHint) -> None
        """Sets the retry_hint of this EncodingErrorDefinition.

        Indicates if the call that caused the error should be retried.

        :param retry_hint: The retry_hint of this EncodingErrorDefinition.
        :type: ErrorRetryHint
        """

        if retry_hint is not None:
            if not isinstance(retry_hint, ErrorRetryHint):
                raise TypeError("Invalid type for `retry_hint`, type has to be `ErrorRetryHint`")

        self._retry_hint = retry_hint

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
        if not isinstance(other, EncodingErrorDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
