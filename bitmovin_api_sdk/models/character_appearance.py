# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.age_range import AgeRange
import pprint
import six


class CharacterAppearance(object):
    @poscheck_model
    def __init__(self,
                 summary=None,
                 gender=None,
                 approximate_age=None,
                 hair_color=None,
                 hair_style=None,
                 hair_fullness=None,
                 facial_hair=None,
                 physical_build=None,
                 distinguishing_features=None,
                 clothing=None):
        # type: (string_types, string_types, AgeRange, string_types, string_types, string_types, string_types, string_types, string_types, string_types) -> None

        self._summary = None
        self._gender = None
        self._approximate_age = None
        self._hair_color = None
        self._hair_style = None
        self._hair_fullness = None
        self._facial_hair = None
        self._physical_build = None
        self._distinguishing_features = None
        self._clothing = None
        self.discriminator = None

        if summary is not None:
            self.summary = summary
        if gender is not None:
            self.gender = gender
        if approximate_age is not None:
            self.approximate_age = approximate_age
        if hair_color is not None:
            self.hair_color = hair_color
        if hair_style is not None:
            self.hair_style = hair_style
        if hair_fullness is not None:
            self.hair_fullness = hair_fullness
        if facial_hair is not None:
            self.facial_hair = facial_hair
        if physical_build is not None:
            self.physical_build = physical_build
        if distinguishing_features is not None:
            self.distinguishing_features = distinguishing_features
        if clothing is not None:
            self.clothing = clothing

    @property
    def openapi_types(self):
        types = {
            'summary': 'string_types',
            'gender': 'string_types',
            'approximate_age': 'AgeRange',
            'hair_color': 'string_types',
            'hair_style': 'string_types',
            'hair_fullness': 'string_types',
            'facial_hair': 'string_types',
            'physical_build': 'string_types',
            'distinguishing_features': 'string_types',
            'clothing': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'summary': 'summary',
            'gender': 'gender',
            'approximate_age': 'approximateAge',
            'hair_color': 'hairColor',
            'hair_style': 'hairStyle',
            'hair_fullness': 'hairFullness',
            'facial_hair': 'facialHair',
            'physical_build': 'physicalBuild',
            'distinguishing_features': 'distinguishingFeatures',
            'clothing': 'clothing'
        }
        return attributes

    @property
    def summary(self):
        # type: () -> string_types
        """Gets the summary of this CharacterAppearance.


        :return: The summary of this CharacterAppearance.
        :rtype: string_types
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        # type: (string_types) -> None
        """Sets the summary of this CharacterAppearance.


        :param summary: The summary of this CharacterAppearance.
        :type: string_types
        """

        if summary is not None:
            if not isinstance(summary, string_types):
                raise TypeError("Invalid type for `summary`, type has to be `string_types`")

        self._summary = summary

    @property
    def gender(self):
        # type: () -> string_types
        """Gets the gender of this CharacterAppearance.


        :return: The gender of this CharacterAppearance.
        :rtype: string_types
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        # type: (string_types) -> None
        """Sets the gender of this CharacterAppearance.


        :param gender: The gender of this CharacterAppearance.
        :type: string_types
        """

        if gender is not None:
            if not isinstance(gender, string_types):
                raise TypeError("Invalid type for `gender`, type has to be `string_types`")

        self._gender = gender

    @property
    def approximate_age(self):
        # type: () -> AgeRange
        """Gets the approximate_age of this CharacterAppearance.

        The approximate age range of the character

        :return: The approximate_age of this CharacterAppearance.
        :rtype: AgeRange
        """
        return self._approximate_age

    @approximate_age.setter
    def approximate_age(self, approximate_age):
        # type: (AgeRange) -> None
        """Sets the approximate_age of this CharacterAppearance.

        The approximate age range of the character

        :param approximate_age: The approximate_age of this CharacterAppearance.
        :type: AgeRange
        """

        if approximate_age is not None:
            if not isinstance(approximate_age, AgeRange):
                raise TypeError("Invalid type for `approximate_age`, type has to be `AgeRange`")

        self._approximate_age = approximate_age

    @property
    def hair_color(self):
        # type: () -> string_types
        """Gets the hair_color of this CharacterAppearance.


        :return: The hair_color of this CharacterAppearance.
        :rtype: string_types
        """
        return self._hair_color

    @hair_color.setter
    def hair_color(self, hair_color):
        # type: (string_types) -> None
        """Sets the hair_color of this CharacterAppearance.


        :param hair_color: The hair_color of this CharacterAppearance.
        :type: string_types
        """

        if hair_color is not None:
            if not isinstance(hair_color, string_types):
                raise TypeError("Invalid type for `hair_color`, type has to be `string_types`")

        self._hair_color = hair_color

    @property
    def hair_style(self):
        # type: () -> string_types
        """Gets the hair_style of this CharacterAppearance.


        :return: The hair_style of this CharacterAppearance.
        :rtype: string_types
        """
        return self._hair_style

    @hair_style.setter
    def hair_style(self, hair_style):
        # type: (string_types) -> None
        """Sets the hair_style of this CharacterAppearance.


        :param hair_style: The hair_style of this CharacterAppearance.
        :type: string_types
        """

        if hair_style is not None:
            if not isinstance(hair_style, string_types):
                raise TypeError("Invalid type for `hair_style`, type has to be `string_types`")

        self._hair_style = hair_style

    @property
    def hair_fullness(self):
        # type: () -> string_types
        """Gets the hair_fullness of this CharacterAppearance.


        :return: The hair_fullness of this CharacterAppearance.
        :rtype: string_types
        """
        return self._hair_fullness

    @hair_fullness.setter
    def hair_fullness(self, hair_fullness):
        # type: (string_types) -> None
        """Sets the hair_fullness of this CharacterAppearance.


        :param hair_fullness: The hair_fullness of this CharacterAppearance.
        :type: string_types
        """

        if hair_fullness is not None:
            if not isinstance(hair_fullness, string_types):
                raise TypeError("Invalid type for `hair_fullness`, type has to be `string_types`")

        self._hair_fullness = hair_fullness

    @property
    def facial_hair(self):
        # type: () -> string_types
        """Gets the facial_hair of this CharacterAppearance.


        :return: The facial_hair of this CharacterAppearance.
        :rtype: string_types
        """
        return self._facial_hair

    @facial_hair.setter
    def facial_hair(self, facial_hair):
        # type: (string_types) -> None
        """Sets the facial_hair of this CharacterAppearance.


        :param facial_hair: The facial_hair of this CharacterAppearance.
        :type: string_types
        """

        if facial_hair is not None:
            if not isinstance(facial_hair, string_types):
                raise TypeError("Invalid type for `facial_hair`, type has to be `string_types`")

        self._facial_hair = facial_hair

    @property
    def physical_build(self):
        # type: () -> string_types
        """Gets the physical_build of this CharacterAppearance.


        :return: The physical_build of this CharacterAppearance.
        :rtype: string_types
        """
        return self._physical_build

    @physical_build.setter
    def physical_build(self, physical_build):
        # type: (string_types) -> None
        """Sets the physical_build of this CharacterAppearance.


        :param physical_build: The physical_build of this CharacterAppearance.
        :type: string_types
        """

        if physical_build is not None:
            if not isinstance(physical_build, string_types):
                raise TypeError("Invalid type for `physical_build`, type has to be `string_types`")

        self._physical_build = physical_build

    @property
    def distinguishing_features(self):
        # type: () -> string_types
        """Gets the distinguishing_features of this CharacterAppearance.


        :return: The distinguishing_features of this CharacterAppearance.
        :rtype: string_types
        """
        return self._distinguishing_features

    @distinguishing_features.setter
    def distinguishing_features(self, distinguishing_features):
        # type: (string_types) -> None
        """Sets the distinguishing_features of this CharacterAppearance.


        :param distinguishing_features: The distinguishing_features of this CharacterAppearance.
        :type: string_types
        """

        if distinguishing_features is not None:
            if not isinstance(distinguishing_features, string_types):
                raise TypeError("Invalid type for `distinguishing_features`, type has to be `string_types`")

        self._distinguishing_features = distinguishing_features

    @property
    def clothing(self):
        # type: () -> string_types
        """Gets the clothing of this CharacterAppearance.


        :return: The clothing of this CharacterAppearance.
        :rtype: string_types
        """
        return self._clothing

    @clothing.setter
    def clothing(self, clothing):
        # type: (string_types) -> None
        """Sets the clothing of this CharacterAppearance.


        :param clothing: The clothing of this CharacterAppearance.
        :type: string_types
        """

        if clothing is not None:
            if not isinstance(clothing, string_types):
                raise TypeError("Invalid type for `clothing`, type has to be `string_types`")

        self._clothing = clothing

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
        if not isinstance(other, CharacterAppearance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
