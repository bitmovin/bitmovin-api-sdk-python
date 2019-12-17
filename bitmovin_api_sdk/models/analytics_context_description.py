# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsContextDescription(object):
    @poscheck_model
    def __init__(self,
                 label=None,
                 description=None):
        # type: (string_types, string_types) -> None

        self._label = None
        self._description = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if description is not None:
            self.description = description

    @property
    def openapi_types(self):
        types = {
            'label': 'string_types',
            'description': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'label': 'label',
            'description': 'description'
        }
        return attributes

    @property
    def label(self):
        # type: () -> string_types
        """Gets the label of this AnalyticsContextDescription.


        :return: The label of this AnalyticsContextDescription.
        :rtype: string_types
        """
        return self._label

    @label.setter
    def label(self, label):
        # type: (string_types) -> None
        """Sets the label of this AnalyticsContextDescription.


        :param label: The label of this AnalyticsContextDescription.
        :type: string_types
        """

        if label is not None:
            if not isinstance(label, string_types):
                raise TypeError("Invalid type for `label`, type has to be `string_types`")

        self._label = label

    @property
    def description(self):
        # type: () -> string_types
        """Gets the description of this AnalyticsContextDescription.


        :return: The description of this AnalyticsContextDescription.
        :rtype: string_types
        """
        return self._description

    @description.setter
    def description(self, description):
        # type: (string_types) -> None
        """Sets the description of this AnalyticsContextDescription.


        :param description: The description of this AnalyticsContextDescription.
        :type: string_types
        """

        if description is not None:
            if not isinstance(description, string_types):
                raise TypeError("Invalid type for `description`, type has to be `string_types`")

        self._description = description

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
        if not isinstance(other, AnalyticsContextDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
