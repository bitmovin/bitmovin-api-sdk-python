# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsErrorDetailsResponse(object):
    @poscheck_model
    def __init__(self,
                 error_details=None):
        # type: (list[AnalyticsErrorDetail]) -> None

        self._error_details = list()
        self.discriminator = None

        if error_details is not None:
            self.error_details = error_details

    @property
    def openapi_types(self):
        types = {
            'error_details': 'list[AnalyticsErrorDetail]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'error_details': 'errorDetails'
        }
        return attributes

    @property
    def error_details(self):
        # type: () -> list[AnalyticsErrorDetail]
        """Gets the error_details of this AnalyticsErrorDetailsResponse.


        :return: The error_details of this AnalyticsErrorDetailsResponse.
        :rtype: list[AnalyticsErrorDetail]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        # type: (list) -> None
        """Sets the error_details of this AnalyticsErrorDetailsResponse.


        :param error_details: The error_details of this AnalyticsErrorDetailsResponse.
        :type: list[AnalyticsErrorDetail]
        """

        if error_details is not None:
            if not isinstance(error_details, list):
                raise TypeError("Invalid type for `error_details`, type has to be `list[AnalyticsErrorDetail]`")

        self._error_details = error_details

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
        if not isinstance(other, AnalyticsErrorDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
