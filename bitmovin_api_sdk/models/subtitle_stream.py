# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.media_stream import MediaStream
import pprint
import six


class SubtitleStream(MediaStream):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 position=None,
                 duration=None,
                 codec=None,
                 language=None,
                 hearing_impaired=None):
        # type: (string_types, int, float, string_types, string_types, bool) -> None
        super(SubtitleStream, self).__init__(id_=id_, position=position, duration=duration, codec=codec)

        self._language = None
        self._hearing_impaired = None
        self.discriminator = None

        if language is not None:
            self.language = language
        if hearing_impaired is not None:
            self.hearing_impaired = hearing_impaired

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SubtitleStream, self), 'openapi_types'):
            types = getattr(super(SubtitleStream, self), 'openapi_types')

        types.update({
            'language': 'string_types',
            'hearing_impaired': 'bool'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SubtitleStream, self), 'attribute_map'):
            attributes = getattr(super(SubtitleStream, self), 'attribute_map')

        attributes.update({
            'language': 'language',
            'hearing_impaired': 'hearingImpaired'
        })
        return attributes

    @property
    def language(self):
        # type: () -> string_types
        """Gets the language of this SubtitleStream.

        Language of the stream

        :return: The language of this SubtitleStream.
        :rtype: string_types
        """
        return self._language

    @language.setter
    def language(self, language):
        # type: (string_types) -> None
        """Sets the language of this SubtitleStream.

        Language of the stream

        :param language: The language of this SubtitleStream.
        :type: string_types
        """

        if language is not None:
            if not isinstance(language, string_types):
                raise TypeError("Invalid type for `language`, type has to be `string_types`")

        self._language = language

    @property
    def hearing_impaired(self):
        # type: () -> bool
        """Gets the hearing_impaired of this SubtitleStream.

        Hearing impaired support

        :return: The hearing_impaired of this SubtitleStream.
        :rtype: bool
        """
        return self._hearing_impaired

    @hearing_impaired.setter
    def hearing_impaired(self, hearing_impaired):
        # type: (bool) -> None
        """Sets the hearing_impaired of this SubtitleStream.

        Hearing impaired support

        :param hearing_impaired: The hearing_impaired of this SubtitleStream.
        :type: bool
        """

        if hearing_impaired is not None:
            if not isinstance(hearing_impaired, bool):
                raise TypeError("Invalid type for `hearing_impaired`, type has to be `bool`")

        self._hearing_impaired = hearing_impaired

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SubtitleStream, self), "to_dict"):
            result = super(SubtitleStream, self).to_dict()
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
        if not isinstance(other, SubtitleStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
