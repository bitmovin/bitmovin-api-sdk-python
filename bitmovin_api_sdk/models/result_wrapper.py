# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class ResultWrapper(object):
    @poscheck_model
    def __init__(self,
                 result=None):
        # type: (object) -> None

        self._result = None
        self.discriminator = None

        if result is not None:
            self.result = result

    @property
    def openapi_types(self):
        types = {
            'result': 'object'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'result': 'result'
        }
        return attributes

    @property
    def result(self):
        # type: () -> object
        """Gets the result of this ResultWrapper.


        :return: The result of this ResultWrapper.
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        # type: (object) -> None
        """Sets the result of this ResultWrapper.


        :param result: The result of this ResultWrapper.
        :type: object
        """

        if result is not None:
            if not isinstance(result, object):
                raise TypeError("Invalid type for `result`, type has to be `object`")

        self._result = result

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
        if not isinstance(other, ResultWrapper):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
