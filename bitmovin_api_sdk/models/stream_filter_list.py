# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class StreamFilterList(object):
    @poscheck_model
    def __init__(self,
                 filters=None):
        # type: (list[StreamFilter]) -> None

        self._filters = list()
        self.discriminator = None

        if filters is not None:
            self.filters = filters

    @property
    def openapi_types(self):
        types = {
            'filters': 'list[StreamFilter]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'filters': 'filters'
        }
        return attributes

    @property
    def filters(self):
        # type: () -> list[StreamFilter]
        """Gets the filters of this StreamFilterList.

        List of stream filters (required)

        :return: The filters of this StreamFilterList.
        :rtype: list[StreamFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        # type: (list) -> None
        """Sets the filters of this StreamFilterList.

        List of stream filters (required)

        :param filters: The filters of this StreamFilterList.
        :type: list[StreamFilter]
        """

        if filters is not None:
            if not isinstance(filters, list):
                raise TypeError("Invalid type for `filters`, type has to be `list[StreamFilter]`")

        self._filters = filters

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
        if not isinstance(other, StreamFilterList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
