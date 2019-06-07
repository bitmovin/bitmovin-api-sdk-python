# coding: utf-8
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class TimeSpan(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = {
            '_from': 'int',
            'to': 'int'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            '_from': 'from',
            'to': 'to'
        }
        return attributes

    def __init__(self, _from=None, to=None, *args, **kwargs):

        self.__from = None
        self._to = None
        self.discriminator = None

        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to

    @property
    def _from(self):
        """Gets the _from of this TimeSpan.

        Start offset of the time frame in milliseconds

        :return: The _from of this TimeSpan.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this TimeSpan.

        Start offset of the time frame in milliseconds

        :param _from: The _from of this TimeSpan.
        :type: int
        """

        if _from is not None:
            if not isinstance(_from, int):
                raise TypeError("Invalid type for `_from`, type has to be `int`")

        self.__from = _from


    @property
    def to(self):
        """Gets the to of this TimeSpan.

        End offset of the time frame in milliseconds

        :return: The to of this TimeSpan.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this TimeSpan.

        End offset of the time frame in milliseconds

        :param to: The to of this TimeSpan.
        :type: int
        """

        if to is not None:
            if not isinstance(to, int):
                raise TypeError("Invalid type for `to`, type has to be `int`")

        self._to = to

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(TimeSpan, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TimeSpan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
