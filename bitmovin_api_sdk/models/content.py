# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class Content(object):
    @poscheck_model
    def __init__(self,
                 characters=None,
                 objects=None,
                 settings=None):
        # type: (list[Character], list[SceneObject], list[Setting]) -> None

        self._characters = list()
        self._objects = list()
        self._settings = list()
        self.discriminator = None

        if characters is not None:
            self.characters = characters
        if objects is not None:
            self.objects = objects
        if settings is not None:
            self.settings = settings

    @property
    def openapi_types(self):
        types = {
            'characters': 'list[Character]',
            'objects': 'list[SceneObject]',
            'settings': 'list[Setting]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'characters': 'characters',
            'objects': 'objects',
            'settings': 'settings'
        }
        return attributes

    @property
    def characters(self):
        # type: () -> list[Character]
        """Gets the characters of this Content.


        :return: The characters of this Content.
        :rtype: list[Character]
        """
        return self._characters

    @characters.setter
    def characters(self, characters):
        # type: (list) -> None
        """Sets the characters of this Content.


        :param characters: The characters of this Content.
        :type: list[Character]
        """

        if characters is not None:
            if not isinstance(characters, list):
                raise TypeError("Invalid type for `characters`, type has to be `list[Character]`")

        self._characters = characters

    @property
    def objects(self):
        # type: () -> list[SceneObject]
        """Gets the objects of this Content.


        :return: The objects of this Content.
        :rtype: list[SceneObject]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        # type: (list) -> None
        """Sets the objects of this Content.


        :param objects: The objects of this Content.
        :type: list[SceneObject]
        """

        if objects is not None:
            if not isinstance(objects, list):
                raise TypeError("Invalid type for `objects`, type has to be `list[SceneObject]`")

        self._objects = objects

    @property
    def settings(self):
        # type: () -> list[Setting]
        """Gets the settings of this Content.


        :return: The settings of this Content.
        :rtype: list[Setting]
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        # type: (list) -> None
        """Sets the settings of this Content.


        :param settings: The settings of this Content.
        :type: list[Setting]
        """

        if settings is not None:
            if not isinstance(settings, list):
                raise TypeError("Invalid type for `settings`, type has to be `list[Setting]`")

        self._settings = settings

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
        if not isinstance(other, Content):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
