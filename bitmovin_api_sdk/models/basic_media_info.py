# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class BasicMediaInfo(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 group_id=None,
                 language=None,
                 assoc_language=None,
                 name=None,
                 is_default=None,
                 autoselect=None,
                 characteristics=None):
        # type: (string_types, string_types, string_types, string_types, string_types, bool, bool, list[string_types]) -> None
        super(BasicMediaInfo, self).__init__(id_=id_)

        self._group_id = None
        self._language = None
        self._assoc_language = None
        self._name = None
        self._is_default = None
        self._autoselect = None
        self._characteristics = list()
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if language is not None:
            self.language = language
        if assoc_language is not None:
            self.assoc_language = assoc_language
        if name is not None:
            self.name = name
        if is_default is not None:
            self.is_default = is_default
        if autoselect is not None:
            self.autoselect = autoselect
        if characteristics is not None:
            self.characteristics = characteristics

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(BasicMediaInfo, self), 'openapi_types'):
            types = getattr(super(BasicMediaInfo, self), 'openapi_types')

        types.update({
            'group_id': 'string_types',
            'language': 'string_types',
            'assoc_language': 'string_types',
            'name': 'string_types',
            'is_default': 'bool',
            'autoselect': 'bool',
            'characteristics': 'list[string_types]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(BasicMediaInfo, self), 'attribute_map'):
            attributes = getattr(super(BasicMediaInfo, self), 'attribute_map')

        attributes.update({
            'group_id': 'groupId',
            'language': 'language',
            'assoc_language': 'assocLanguage',
            'name': 'name',
            'is_default': 'isDefault',
            'autoselect': 'autoselect',
            'characteristics': 'characteristics'
        })
        return attributes

    @property
    def group_id(self):
        # type: () -> string_types
        """Gets the group_id of this BasicMediaInfo.

        The value is a quoted-string which specifies the group to which the Rendition belongs. (required)

        :return: The group_id of this BasicMediaInfo.
        :rtype: string_types
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        # type: (string_types) -> None
        """Sets the group_id of this BasicMediaInfo.

        The value is a quoted-string which specifies the group to which the Rendition belongs. (required)

        :param group_id: The group_id of this BasicMediaInfo.
        :type: string_types
        """

        if group_id is not None:
            if not isinstance(group_id, string_types):
                raise TypeError("Invalid type for `group_id`, type has to be `string_types`")

        self._group_id = group_id

    @property
    def language(self):
        # type: () -> string_types
        """Gets the language of this BasicMediaInfo.

        Primary language in the rendition.

        :return: The language of this BasicMediaInfo.
        :rtype: string_types
        """
        return self._language

    @language.setter
    def language(self, language):
        # type: (string_types) -> None
        """Sets the language of this BasicMediaInfo.

        Primary language in the rendition.

        :param language: The language of this BasicMediaInfo.
        :type: string_types
        """

        if language is not None:
            if not isinstance(language, string_types):
                raise TypeError("Invalid type for `language`, type has to be `string_types`")

        self._language = language

    @property
    def assoc_language(self):
        # type: () -> string_types
        """Gets the assoc_language of this BasicMediaInfo.

        Identifies a language that is associated with the Rendition.

        :return: The assoc_language of this BasicMediaInfo.
        :rtype: string_types
        """
        return self._assoc_language

    @assoc_language.setter
    def assoc_language(self, assoc_language):
        # type: (string_types) -> None
        """Sets the assoc_language of this BasicMediaInfo.

        Identifies a language that is associated with the Rendition.

        :param assoc_language: The assoc_language of this BasicMediaInfo.
        :type: string_types
        """

        if assoc_language is not None:
            if not isinstance(assoc_language, string_types):
                raise TypeError("Invalid type for `assoc_language`, type has to be `string_types`")

        self._assoc_language = assoc_language

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this BasicMediaInfo.

        Human readable description of the rendition. (required)

        :return: The name of this BasicMediaInfo.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this BasicMediaInfo.

        Human readable description of the rendition. (required)

        :param name: The name of this BasicMediaInfo.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def is_default(self):
        # type: () -> bool
        """Gets the is_default of this BasicMediaInfo.

        If set to true, the client SHOULD play this Rendition of the content in the absence of information from the user.

        :return: The is_default of this BasicMediaInfo.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        # type: (bool) -> None
        """Sets the is_default of this BasicMediaInfo.

        If set to true, the client SHOULD play this Rendition of the content in the absence of information from the user.

        :param is_default: The is_default of this BasicMediaInfo.
        :type: bool
        """

        if is_default is not None:
            if not isinstance(is_default, bool):
                raise TypeError("Invalid type for `is_default`, type has to be `bool`")

        self._is_default = is_default

    @property
    def autoselect(self):
        # type: () -> bool
        """Gets the autoselect of this BasicMediaInfo.

        If set to true, the client MAY choose to play this Rendition in the absence of explicit user preference.

        :return: The autoselect of this BasicMediaInfo.
        :rtype: bool
        """
        return self._autoselect

    @autoselect.setter
    def autoselect(self, autoselect):
        # type: (bool) -> None
        """Sets the autoselect of this BasicMediaInfo.

        If set to true, the client MAY choose to play this Rendition in the absence of explicit user preference.

        :param autoselect: The autoselect of this BasicMediaInfo.
        :type: bool
        """

        if autoselect is not None:
            if not isinstance(autoselect, bool):
                raise TypeError("Invalid type for `autoselect`, type has to be `bool`")

        self._autoselect = autoselect

    @property
    def characteristics(self):
        # type: () -> list[string_types]
        """Gets the characteristics of this BasicMediaInfo.

        Contains Uniform Type Identifiers

        :return: The characteristics of this BasicMediaInfo.
        :rtype: list[string_types]
        """
        return self._characteristics

    @characteristics.setter
    def characteristics(self, characteristics):
        # type: (list) -> None
        """Sets the characteristics of this BasicMediaInfo.

        Contains Uniform Type Identifiers

        :param characteristics: The characteristics of this BasicMediaInfo.
        :type: list[string_types]
        """

        if characteristics is not None:
            if not isinstance(characteristics, list):
                raise TypeError("Invalid type for `characteristics`, type has to be `list[string_types]`")

        self._characteristics = characteristics

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(BasicMediaInfo, self), "to_dict"):
            result = super(BasicMediaInfo, self).to_dict()
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
        if not isinstance(other, BasicMediaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
