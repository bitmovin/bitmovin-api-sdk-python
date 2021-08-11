# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsErrorData(object):
    @poscheck_model
    def __init__(self,
                 exception_message=None,
                 additional_data=None,
                 exception_stacktrace=None):
        # type: (string_types, string_types, list[string_types]) -> None

        self._exception_message = None
        self._additional_data = None
        self._exception_stacktrace = list()
        self.discriminator = None

        if exception_message is not None:
            self.exception_message = exception_message
        if additional_data is not None:
            self.additional_data = additional_data
        if exception_stacktrace is not None:
            self.exception_stacktrace = exception_stacktrace

    @property
    def openapi_types(self):
        types = {
            'exception_message': 'string_types',
            'additional_data': 'string_types',
            'exception_stacktrace': 'list[string_types]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'exception_message': 'exceptionMessage',
            'additional_data': 'additionalData',
            'exception_stacktrace': 'exceptionStacktrace'
        }
        return attributes

    @property
    def exception_message(self):
        # type: () -> string_types
        """Gets the exception_message of this AnalyticsErrorData.

        Exception message

        :return: The exception_message of this AnalyticsErrorData.
        :rtype: string_types
        """
        return self._exception_message

    @exception_message.setter
    def exception_message(self, exception_message):
        # type: (string_types) -> None
        """Sets the exception_message of this AnalyticsErrorData.

        Exception message

        :param exception_message: The exception_message of this AnalyticsErrorData.
        :type: string_types
        """

        if exception_message is not None:
            if not isinstance(exception_message, string_types):
                raise TypeError("Invalid type for `exception_message`, type has to be `string_types`")

        self._exception_message = exception_message

    @property
    def additional_data(self):
        # type: () -> string_types
        """Gets the additional_data of this AnalyticsErrorData.

        Additional error data

        :return: The additional_data of this AnalyticsErrorData.
        :rtype: string_types
        """
        return self._additional_data

    @additional_data.setter
    def additional_data(self, additional_data):
        # type: (string_types) -> None
        """Sets the additional_data of this AnalyticsErrorData.

        Additional error data

        :param additional_data: The additional_data of this AnalyticsErrorData.
        :type: string_types
        """

        if additional_data is not None:
            if not isinstance(additional_data, string_types):
                raise TypeError("Invalid type for `additional_data`, type has to be `string_types`")

        self._additional_data = additional_data

    @property
    def exception_stacktrace(self):
        # type: () -> list[string_types]
        """Gets the exception_stacktrace of this AnalyticsErrorData.


        :return: The exception_stacktrace of this AnalyticsErrorData.
        :rtype: list[string_types]
        """
        return self._exception_stacktrace

    @exception_stacktrace.setter
    def exception_stacktrace(self, exception_stacktrace):
        # type: (list) -> None
        """Sets the exception_stacktrace of this AnalyticsErrorData.


        :param exception_stacktrace: The exception_stacktrace of this AnalyticsErrorData.
        :type: list[string_types]
        """

        if exception_stacktrace is not None:
            if not isinstance(exception_stacktrace, list):
                raise TypeError("Invalid type for `exception_stacktrace`, type has to be `list[string_types]`")

        self._exception_stacktrace = exception_stacktrace

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
        if not isinstance(other, AnalyticsErrorData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
