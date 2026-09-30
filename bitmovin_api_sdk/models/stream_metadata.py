# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class StreamMetadata(object):
    @poscheck_model
    def __init__(self,
                 language=None,
                 label=None,
                 label_language=None,
                 switching_set_id=None):
        # type: (string_types, string_types, string_types, string_types) -> None

        self._language = None
        self._label = None
        self._label_language = None
        self._switching_set_id = None
        self.discriminator = None

        if language is not None:
            self.language = language
        if label is not None:
            self.label = label
        if label_language is not None:
            self.label_language = label_language
        if switching_set_id is not None:
            self.switching_set_id = switching_set_id

    @property
    def openapi_types(self):
        types = {
            'language': 'string_types',
            'label': 'string_types',
            'label_language': 'string_types',
            'switching_set_id': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'language': 'language',
            'label': 'label',
            'label_language': 'labelLanguage',
            'switching_set_id': 'switchingSetId'
        }
        return attributes

    @property
    def language(self):
        # type: () -> string_types
        """Gets the language of this StreamMetadata.

        Language of the media contained in the stream, given as an ISO 639-2 code or a BCP 47 tag, for example 'eng' or 'en-US'. If the value is not set, then no metadata tag is set for the media stream.

        :return: The language of this StreamMetadata.
        :rtype: string_types
        """
        return self._language

    @language.setter
    def language(self, language):
        # type: (string_types) -> None
        """Sets the language of this StreamMetadata.

        Language of the media contained in the stream, given as an ISO 639-2 code or a BCP 47 tag, for example 'eng' or 'en-US'. If the value is not set, then no metadata tag is set for the media stream.

        :param language: The language of this StreamMetadata.
        :type: string_types
        """

        if language is not None:
            if not isinstance(language, string_types):
                raise TypeError("Invalid type for `language`, type has to be `string_types`")

        self._language = language

    @property
    def label(self):
        # type: () -> string_types
        """Gets the label of this StreamMetadata.

        Display name of the Stream, for example to tell apart multiple audio tracks that share the same language. For CMAF muxings it is written as a 'labl' box (ISO/IEC 14496-12) into the user data of the track. Downstream packagers use it for the Label element in DASH manifests and the NAME attribute of EXT-X-MEDIA tags in HLS playlists. If the value is not set, no label is written. Use 'labelLanguage' to declare which language the label itself is written in.

        :return: The label of this StreamMetadata.
        :rtype: string_types
        """
        return self._label

    @label.setter
    def label(self, label):
        # type: (string_types) -> None
        """Sets the label of this StreamMetadata.

        Display name of the Stream, for example to tell apart multiple audio tracks that share the same language. For CMAF muxings it is written as a 'labl' box (ISO/IEC 14496-12) into the user data of the track. Downstream packagers use it for the Label element in DASH manifests and the NAME attribute of EXT-X-MEDIA tags in HLS playlists. If the value is not set, no label is written. Use 'labelLanguage' to declare which language the label itself is written in.

        :param label: The label of this StreamMetadata.
        :type: string_types
        """

        if label is not None:
            if label is not None and len(label) > 255:
                raise ValueError("Invalid value for `label`, length must be less than or equal to `255`")
            if not isinstance(label, string_types):
                raise TypeError("Invalid type for `label`, type has to be `string_types`")

        self._label = label

    @property
    def label_language(self):
        # type: () -> string_types
        """Gets the label_language of this StreamMetadata.

        Language the 'label' itself is written in, which is not necessarily the language of the media. A Spanish audio track can carry an English label, for example. For CMAF muxings it is written into the 'labl' box next to the label, and downstream packagers use it for the lang attribute of the Label element in DASH manifests. The value is written as given and downstream packagers expose it unchanged, so set a BCP 47 tag such as 'en' when the manifest should carry that form. The value has to be shaped like a BCP 47 tag: a primary subtag of two or three letters, optionally followed by subtags of up to eight letters or digits, each separated by a hyphen, for example 'en', 'en-US' or 'es-419'. If the value is not set and a label is set, 'language' is used as given, for example 'eng'. Without either, the label language is written as 'und' (undetermined). HLS playlists are not affected, as EXT-X-MEDIA has no equivalent attribute.

        :return: The label_language of this StreamMetadata.
        :rtype: string_types
        """
        return self._label_language

    @label_language.setter
    def label_language(self, label_language):
        # type: (string_types) -> None
        """Sets the label_language of this StreamMetadata.

        Language the 'label' itself is written in, which is not necessarily the language of the media. A Spanish audio track can carry an English label, for example. For CMAF muxings it is written into the 'labl' box next to the label, and downstream packagers use it for the lang attribute of the Label element in DASH manifests. The value is written as given and downstream packagers expose it unchanged, so set a BCP 47 tag such as 'en' when the manifest should carry that form. The value has to be shaped like a BCP 47 tag: a primary subtag of two or three letters, optionally followed by subtags of up to eight letters or digits, each separated by a hyphen, for example 'en', 'en-US' or 'es-419'. If the value is not set and a label is set, 'language' is used as given, for example 'eng'. Without either, the label language is written as 'und' (undetermined). HLS playlists are not affected, as EXT-X-MEDIA has no equivalent attribute.

        :param label_language: The label_language of this StreamMetadata.
        :type: string_types
        """

        if label_language is not None:
            if label_language is not None and len(label_language) > 35:
                raise ValueError("Invalid value for `label_language`, length must be less than or equal to `35`")
            if not isinstance(label_language, string_types):
                raise TypeError("Invalid type for `label_language`, type has to be `string_types`")

        self._label_language = label_language

    @property
    def switching_set_id(self):
        # type: () -> string_types
        """Gets the switching_set_id of this StreamMetadata.

        Identifier of the switching set the Stream belongs to. For CMAF muxings it is written as a 'kind' box with schemeURI urn:dashif:ingest:switchingset_id (DASH-IF Live Media Ingest) into the user data of the track. Downstream packagers group tracks with the same identifier into one switching set and use it in segment URLs. Only letters, digits, hyphens and underscores are allowed. If the value is not set and a label is set, an identifier is derived from the properties of the Stream, including the label. Without a label, no identifier is written. Set it explicitly when segment URLs have to stay stable across configuration updates.

        :return: The switching_set_id of this StreamMetadata.
        :rtype: string_types
        """
        return self._switching_set_id

    @switching_set_id.setter
    def switching_set_id(self, switching_set_id):
        # type: (string_types) -> None
        """Sets the switching_set_id of this StreamMetadata.

        Identifier of the switching set the Stream belongs to. For CMAF muxings it is written as a 'kind' box with schemeURI urn:dashif:ingest:switchingset_id (DASH-IF Live Media Ingest) into the user data of the track. Downstream packagers group tracks with the same identifier into one switching set and use it in segment URLs. Only letters, digits, hyphens and underscores are allowed. If the value is not set and a label is set, an identifier is derived from the properties of the Stream, including the label. Without a label, no identifier is written. Set it explicitly when segment URLs have to stay stable across configuration updates.

        :param switching_set_id: The switching_set_id of this StreamMetadata.
        :type: string_types
        """

        if switching_set_id is not None:
            if switching_set_id is not None and len(switching_set_id) > 64:
                raise ValueError("Invalid value for `switching_set_id`, length must be less than or equal to `64`")
            if not isinstance(switching_set_id, string_types):
                raise TypeError("Invalid type for `switching_set_id`, type has to be `string_types`")

        self._switching_set_id = switching_set_id

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
        if not isinstance(other, StreamMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
