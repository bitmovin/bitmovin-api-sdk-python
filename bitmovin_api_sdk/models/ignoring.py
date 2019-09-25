# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.ignored_by import IgnoredBy
import pprint
import six


class Ignoring(object):
    @poscheck_model
    def __init__(self,
                 ignored_by=None,
                 ignored_by_description=None):
        # type: (IgnoredBy, string_types) -> None

        self._ignored_by = None
        self._ignored_by_description = None
        self.discriminator = None

        if ignored_by is not None:
            self.ignored_by = ignored_by
        if ignored_by_description is not None:
            self.ignored_by_description = ignored_by_description

    @property
    def openapi_types(self):
        types = {
            'ignored_by': 'IgnoredBy',
            'ignored_by_description': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'ignored_by': 'ignoredBy',
            'ignored_by_description': 'ignoredByDescription'
        }
        return attributes

    @property
    def ignored_by(self):
        # type: () -> IgnoredBy
        """Gets the ignored_by of this Ignoring.


        :return: The ignored_by of this Ignoring.
        :rtype: IgnoredBy
        """
        return self._ignored_by

    @ignored_by.setter
    def ignored_by(self, ignored_by):
        # type: (IgnoredBy) -> None
        """Sets the ignored_by of this Ignoring.


        :param ignored_by: The ignored_by of this Ignoring.
        :type: IgnoredBy
        """

        if ignored_by is not None:
            if not isinstance(ignored_by, IgnoredBy):
                raise TypeError("Invalid type for `ignored_by`, type has to be `IgnoredBy`")

        self._ignored_by = ignored_by

    @property
    def ignored_by_description(self):
        # type: () -> string_types
        """Gets the ignored_by_description of this Ignoring.

        Describes why ignoredBy has been set to its current value.

        :return: The ignored_by_description of this Ignoring.
        :rtype: string_types
        """
        return self._ignored_by_description

    @ignored_by_description.setter
    def ignored_by_description(self, ignored_by_description):
        # type: (string_types) -> None
        """Sets the ignored_by_description of this Ignoring.

        Describes why ignoredBy has been set to its current value.

        :param ignored_by_description: The ignored_by_description of this Ignoring.
        :type: string_types
        """

        if ignored_by_description is not None:
            if not isinstance(ignored_by_description, string_types):
                raise TypeError("Invalid type for `ignored_by_description`, type has to be `string_types`")

        self._ignored_by_description = ignored_by_description

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
        if not isinstance(other, Ignoring):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
