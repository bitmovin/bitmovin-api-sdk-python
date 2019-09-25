# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.retry_hint import RetryHint
import pprint
import six


class ErrorDetails(object):
    @poscheck_model
    def __init__(self,
                 code=None,
                 category=None,
                 text=None,
                 retry_hint=None):
        # type: (int, string_types, string_types, RetryHint) -> None

        self._code = None
        self._category = None
        self._text = None
        self._retry_hint = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if category is not None:
            self.category = category
        if text is not None:
            self.text = text
        if retry_hint is not None:
            self.retry_hint = retry_hint

    @property
    def openapi_types(self):
        types = {
            'code': 'int',
            'category': 'string_types',
            'text': 'string_types',
            'retry_hint': 'RetryHint'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'code': 'code',
            'category': 'category',
            'text': 'text',
            'retry_hint': 'retryHint'
        }
        return attributes

    @property
    def code(self):
        # type: () -> int
        """Gets the code of this ErrorDetails.

        Specific error code (required)

        :return: The code of this ErrorDetails.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        # type: (int) -> None
        """Sets the code of this ErrorDetails.

        Specific error code (required)

        :param code: The code of this ErrorDetails.
        :type: int
        """

        if code is not None:
            if not isinstance(code, int):
                raise TypeError("Invalid type for `code`, type has to be `int`")

        self._code = code

    @property
    def category(self):
        # type: () -> string_types
        """Gets the category of this ErrorDetails.

        Error group name (required)

        :return: The category of this ErrorDetails.
        :rtype: string_types
        """
        return self._category

    @category.setter
    def category(self, category):
        # type: (string_types) -> None
        """Sets the category of this ErrorDetails.

        Error group name (required)

        :param category: The category of this ErrorDetails.
        :type: string_types
        """

        if category is not None:
            if not isinstance(category, string_types):
                raise TypeError("Invalid type for `category`, type has to be `string_types`")

        self._category = category

    @property
    def text(self):
        # type: () -> string_types
        """Gets the text of this ErrorDetails.

        Detailed error message (required)

        :return: The text of this ErrorDetails.
        :rtype: string_types
        """
        return self._text

    @text.setter
    def text(self, text):
        # type: (string_types) -> None
        """Sets the text of this ErrorDetails.

        Detailed error message (required)

        :param text: The text of this ErrorDetails.
        :type: string_types
        """

        if text is not None:
            if not isinstance(text, string_types):
                raise TypeError("Invalid type for `text`, type has to be `string_types`")

        self._text = text

    @property
    def retry_hint(self):
        # type: () -> RetryHint
        """Gets the retry_hint of this ErrorDetails.

        Information if the encoding could potentially succeed when retrying. (required)

        :return: The retry_hint of this ErrorDetails.
        :rtype: RetryHint
        """
        return self._retry_hint

    @retry_hint.setter
    def retry_hint(self, retry_hint):
        # type: (RetryHint) -> None
        """Sets the retry_hint of this ErrorDetails.

        Information if the encoding could potentially succeed when retrying. (required)

        :param retry_hint: The retry_hint of this ErrorDetails.
        :type: RetryHint
        """

        if retry_hint is not None:
            if not isinstance(retry_hint, RetryHint):
                raise TypeError("Invalid type for `retry_hint`, type has to be `RetryHint`")

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
        if not isinstance(other, ErrorDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
