# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class Credits(object):
    @poscheck_model
    def __init__(self,
                 persons=None,
                 songs=None):
        # type: (list[Person], list[Song]) -> None

        self._persons = list()
        self._songs = list()
        self.discriminator = None

        if persons is not None:
            self.persons = persons
        if songs is not None:
            self.songs = songs

    @property
    def openapi_types(self):
        types = {
            'persons': 'list[Person]',
            'songs': 'list[Song]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'persons': 'persons',
            'songs': 'songs'
        }
        return attributes

    @property
    def persons(self):
        # type: () -> list[Person]
        """Gets the persons of this Credits.


        :return: The persons of this Credits.
        :rtype: list[Person]
        """
        return self._persons

    @persons.setter
    def persons(self, persons):
        # type: (list) -> None
        """Sets the persons of this Credits.


        :param persons: The persons of this Credits.
        :type: list[Person]
        """

        if persons is not None:
            if not isinstance(persons, list):
                raise TypeError("Invalid type for `persons`, type has to be `list[Person]`")

        self._persons = persons

    @property
    def songs(self):
        # type: () -> list[Song]
        """Gets the songs of this Credits.


        :return: The songs of this Credits.
        :rtype: list[Song]
        """
        return self._songs

    @songs.setter
    def songs(self, songs):
        # type: (list) -> None
        """Sets the songs of this Credits.


        :param songs: The songs of this Credits.
        :type: list[Song]
        """

        if songs is not None:
            if not isinstance(songs, list):
                raise TypeError("Invalid type for `songs`, type has to be `list[Song]`")

        self._songs = songs

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
        if not isinstance(other, Credits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
