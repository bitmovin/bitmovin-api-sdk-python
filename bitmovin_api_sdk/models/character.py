# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.character_appearance import CharacterAppearance
import pprint
import six


class Character(object):
    @poscheck_model
    def __init__(self,
                 character_appearance=None,
                 name=None,
                 played_by=None,
                 description=None):
        # type: (CharacterAppearance, string_types, string_types, string_types) -> None

        self._character_appearance = None
        self._name = None
        self._played_by = None
        self._description = None
        self.discriminator = None

        if character_appearance is not None:
            self.character_appearance = character_appearance
        if name is not None:
            self.name = name
        if played_by is not None:
            self.played_by = played_by
        if description is not None:
            self.description = description

    @property
    def openapi_types(self):
        types = {
            'character_appearance': 'CharacterAppearance',
            'name': 'string_types',
            'played_by': 'string_types',
            'description': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'character_appearance': 'characterAppearance',
            'name': 'name',
            'played_by': 'playedBy',
            'description': 'description'
        }
        return attributes

    @property
    def character_appearance(self):
        # type: () -> CharacterAppearance
        """Gets the character_appearance of this Character.


        :return: The character_appearance of this Character.
        :rtype: CharacterAppearance
        """
        return self._character_appearance

    @character_appearance.setter
    def character_appearance(self, character_appearance):
        # type: (CharacterAppearance) -> None
        """Sets the character_appearance of this Character.


        :param character_appearance: The character_appearance of this Character.
        :type: CharacterAppearance
        """

        if character_appearance is not None:
            if not isinstance(character_appearance, CharacterAppearance):
                raise TypeError("Invalid type for `character_appearance`, type has to be `CharacterAppearance`")

        self._character_appearance = character_appearance

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this Character.


        :return: The name of this Character.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this Character.


        :param name: The name of this Character.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def played_by(self):
        # type: () -> string_types
        """Gets the played_by of this Character.


        :return: The played_by of this Character.
        :rtype: string_types
        """
        return self._played_by

    @played_by.setter
    def played_by(self, played_by):
        # type: (string_types) -> None
        """Sets the played_by of this Character.


        :param played_by: The played_by of this Character.
        :type: string_types
        """

        if played_by is not None:
            if not isinstance(played_by, string_types):
                raise TypeError("Invalid type for `played_by`, type has to be `string_types`")

        self._played_by = played_by

    @property
    def description(self):
        # type: () -> string_types
        """Gets the description of this Character.


        :return: The description of this Character.
        :rtype: string_types
        """
        return self._description

    @description.setter
    def description(self, description):
        # type: (string_types) -> None
        """Sets the description of this Character.


        :param description: The description of this Character.
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
        if not isinstance(other, Character):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
