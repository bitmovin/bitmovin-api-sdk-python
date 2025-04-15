# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class Rating(object):
    @poscheck_model
    def __init__(self,
                 region=None,
                 system=None,
                 rating=None):
        # type: (string_types, string_types, string_types) -> None

        self._region = None
        self._system = None
        self._rating = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if system is not None:
            self.system = system
        if rating is not None:
            self.rating = rating

    @property
    def openapi_types(self):
        types = {
            'region': 'string_types',
            'system': 'string_types',
            'rating': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'region': 'region',
            'system': 'system',
            'rating': 'rating'
        }
        return attributes

    @property
    def region(self):
        # type: () -> string_types
        """Gets the region of this Rating.


        :return: The region of this Rating.
        :rtype: string_types
        """
        return self._region

    @region.setter
    def region(self, region):
        # type: (string_types) -> None
        """Sets the region of this Rating.


        :param region: The region of this Rating.
        :type: string_types
        """

        if region is not None:
            if not isinstance(region, string_types):
                raise TypeError("Invalid type for `region`, type has to be `string_types`")

        self._region = region

    @property
    def system(self):
        # type: () -> string_types
        """Gets the system of this Rating.


        :return: The system of this Rating.
        :rtype: string_types
        """
        return self._system

    @system.setter
    def system(self, system):
        # type: (string_types) -> None
        """Sets the system of this Rating.


        :param system: The system of this Rating.
        :type: string_types
        """

        if system is not None:
            if not isinstance(system, string_types):
                raise TypeError("Invalid type for `system`, type has to be `string_types`")

        self._system = system

    @property
    def rating(self):
        # type: () -> string_types
        """Gets the rating of this Rating.


        :return: The rating of this Rating.
        :rtype: string_types
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        # type: (string_types) -> None
        """Sets the rating of this Rating.


        :param rating: The rating of this Rating.
        :type: string_types
        """

        if rating is not None:
            if not isinstance(rating, string_types):
                raise TypeError("Invalid type for `rating`, type has to be `string_types`")

        self._rating = rating

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
        if not isinstance(other, Rating):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
