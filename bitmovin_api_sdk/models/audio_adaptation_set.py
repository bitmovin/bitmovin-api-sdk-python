# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.adaptation_set import AdaptationSet
import pprint
import six


class AudioAdaptationSet(AdaptationSet):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 custom_attributes=None,
                 roles=None,
                 accessibilities=None,
                 labels=None,
                 lang=None):
        # type: (string_types, list[CustomAttribute], list[AdaptationSetRole], list[Accessibility], list[Label], string_types) -> None
        super(AudioAdaptationSet, self).__init__(id_=id_, custom_attributes=custom_attributes, roles=roles, accessibilities=accessibilities, labels=labels)

        self._lang = None
        self.discriminator = None

        if lang is not None:
            self.lang = lang

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AudioAdaptationSet, self), 'openapi_types'):
            types = getattr(super(AudioAdaptationSet, self), 'openapi_types')

        types.update({
            'lang': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AudioAdaptationSet, self), 'attribute_map'):
            attributes = getattr(super(AudioAdaptationSet, self), 'attribute_map')

        attributes.update({
            'lang': 'lang'
        })
        return attributes

    @property
    def lang(self):
        # type: () -> string_types
        """Gets the lang of this AudioAdaptationSet.

        ISO 639-1 (Alpha-2) code identifying the language of the audio adaptation set (required)

        :return: The lang of this AudioAdaptationSet.
        :rtype: string_types
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        # type: (string_types) -> None
        """Sets the lang of this AudioAdaptationSet.

        ISO 639-1 (Alpha-2) code identifying the language of the audio adaptation set (required)

        :param lang: The lang of this AudioAdaptationSet.
        :type: string_types
        """

        if lang is not None:
            if not isinstance(lang, string_types):
                raise TypeError("Invalid type for `lang`, type has to be `string_types`")

        self._lang = lang

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AudioAdaptationSet, self), "to_dict"):
            result = super(AudioAdaptationSet, self).to_dict()
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
        if not isinstance(other, AudioAdaptationSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
