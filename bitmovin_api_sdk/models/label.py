# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class Label(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 lang=None,
                 value=None):
        # type: (int, string_types, string_types) -> None

        self._id = None
        self._lang = None
        self._value = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if lang is not None:
            self.lang = lang
        if value is not None:
            self.value = value

    @property
    def openapi_types(self):
        types = {
            'id': 'int',
            'lang': 'string_types',
            'value': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'lang': 'lang',
            'value': 'value'
        }
        return attributes

    @property
    def id(self):
        # type: () -> int
        """Gets the id of this Label.

        Identifier of the label.

        :return: The id of this Label.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (int) -> None
        """Sets the id of this Label.

        Identifier of the label.

        :param id_: The id of this Label.
        :type: int
        """

        if id_ is not None:
            if id_ is not None and id_ < 0:
                raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")
            if not isinstance(id_, int):
                raise TypeError("Invalid type for `id`, type has to be `int`")

        self._id = id_

    @property
    def lang(self):
        # type: () -> string_types
        """Gets the lang of this Label.

        Specifies the language of the label.

        :return: The lang of this Label.
        :rtype: string_types
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        # type: (string_types) -> None
        """Sets the lang of this Label.

        Specifies the language of the label.

        :param lang: The lang of this Label.
        :type: string_types
        """

        if lang is not None:
            if not isinstance(lang, string_types):
                raise TypeError("Invalid type for `lang`, type has to be `string_types`")

        self._lang = lang

    @property
    def value(self):
        # type: () -> string_types
        """Gets the value of this Label.

        Content of the label. (required)

        :return: The value of this Label.
        :rtype: string_types
        """
        return self._value

    @value.setter
    def value(self, value):
        # type: (string_types) -> None
        """Sets the value of this Label.

        Content of the label. (required)

        :param value: The value of this Label.
        :type: string_types
        """

        if value is not None:
            if not isinstance(value, string_types):
                raise TypeError("Invalid type for `value`, type has to be `string_types`")

        self._value = value

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
        if not isinstance(other, Label):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
