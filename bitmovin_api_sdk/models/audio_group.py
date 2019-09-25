# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AudioGroup(object):
    @poscheck_model
    def __init__(self,
                 name=None,
                 priority=None):
        # type: (string_types, int) -> None

        self._name = None
        self._priority = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if priority is not None:
            self.priority = priority

    @property
    def openapi_types(self):
        types = {
            'name': 'string_types',
            'priority': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'name': 'name',
            'priority': 'priority'
        }
        return attributes

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this AudioGroup.

        Name of the audio group (required)

        :return: The name of this AudioGroup.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this AudioGroup.

        Name of the audio group (required)

        :param name: The name of this AudioGroup.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def priority(self):
        # type: () -> int
        """Gets the priority of this AudioGroup.

        Priority of the audio group (required)

        :return: The priority of this AudioGroup.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        # type: (int) -> None
        """Sets the priority of this AudioGroup.

        Priority of the audio group (required)

        :param priority: The priority of this AudioGroup.
        :type: int
        """

        if priority is not None:
            if priority is not None and priority > 100:
                raise ValueError("Invalid value for `priority`, must be a value less than or equal to `100`")
            if priority is not None and priority < 0:
                raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `0`")
            if not isinstance(priority, int):
                raise TypeError("Invalid type for `priority`, type has to be `int`")

        self._priority = priority

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
        if not isinstance(other, AudioGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
