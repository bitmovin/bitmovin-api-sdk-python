# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class SmoothStreamingRepresentation(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 encoding_id=None,
                 muxing_id=None,
                 media_file=None,
                 language=None,
                 track_name=None,
                 priority=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, string_types, string_types, string_types, string_types, int) -> None
        super(SmoothStreamingRepresentation, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._encoding_id = None
        self._muxing_id = None
        self._media_file = None
        self._language = None
        self._track_name = None
        self._priority = None
        self.discriminator = None

        if encoding_id is not None:
            self.encoding_id = encoding_id
        if muxing_id is not None:
            self.muxing_id = muxing_id
        if media_file is not None:
            self.media_file = media_file
        if language is not None:
            self.language = language
        if track_name is not None:
            self.track_name = track_name
        if priority is not None:
            self.priority = priority

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SmoothStreamingRepresentation, self), 'openapi_types'):
            types = getattr(super(SmoothStreamingRepresentation, self), 'openapi_types')

        types.update({
            'encoding_id': 'string_types',
            'muxing_id': 'string_types',
            'media_file': 'string_types',
            'language': 'string_types',
            'track_name': 'string_types',
            'priority': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SmoothStreamingRepresentation, self), 'attribute_map'):
            attributes = getattr(super(SmoothStreamingRepresentation, self), 'attribute_map')

        attributes.update({
            'encoding_id': 'encodingId',
            'muxing_id': 'muxingId',
            'media_file': 'mediaFile',
            'language': 'language',
            'track_name': 'trackName',
            'priority': 'priority'
        })
        return attributes

    @property
    def encoding_id(self):
        # type: () -> string_types
        """Gets the encoding_id of this SmoothStreamingRepresentation.

        Id of the encoding (required)

        :return: The encoding_id of this SmoothStreamingRepresentation.
        :rtype: string_types
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        # type: (string_types) -> None
        """Sets the encoding_id of this SmoothStreamingRepresentation.

        Id of the encoding (required)

        :param encoding_id: The encoding_id of this SmoothStreamingRepresentation.
        :type: string_types
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, string_types):
                raise TypeError("Invalid type for `encoding_id`, type has to be `string_types`")

        self._encoding_id = encoding_id

    @property
    def muxing_id(self):
        # type: () -> string_types
        """Gets the muxing_id of this SmoothStreamingRepresentation.

        Id of the muxing. (required)

        :return: The muxing_id of this SmoothStreamingRepresentation.
        :rtype: string_types
        """
        return self._muxing_id

    @muxing_id.setter
    def muxing_id(self, muxing_id):
        # type: (string_types) -> None
        """Sets the muxing_id of this SmoothStreamingRepresentation.

        Id of the muxing. (required)

        :param muxing_id: The muxing_id of this SmoothStreamingRepresentation.
        :type: string_types
        """

        if muxing_id is not None:
            if not isinstance(muxing_id, string_types):
                raise TypeError("Invalid type for `muxing_id`, type has to be `string_types`")

        self._muxing_id = muxing_id

    @property
    def media_file(self):
        # type: () -> string_types
        """Gets the media_file of this SmoothStreamingRepresentation.

        The Smooth Streaming ismv or isma file that will be referenced in the manifest. (required)

        :return: The media_file of this SmoothStreamingRepresentation.
        :rtype: string_types
        """
        return self._media_file

    @media_file.setter
    def media_file(self, media_file):
        # type: (string_types) -> None
        """Sets the media_file of this SmoothStreamingRepresentation.

        The Smooth Streaming ismv or isma file that will be referenced in the manifest. (required)

        :param media_file: The media_file of this SmoothStreamingRepresentation.
        :type: string_types
        """

        if media_file is not None:
            if not isinstance(media_file, string_types):
                raise TypeError("Invalid type for `media_file`, type has to be `string_types`")

        self._media_file = media_file

    @property
    def language(self):
        # type: () -> string_types
        """Gets the language of this SmoothStreamingRepresentation.

        Language of the MP4 file

        :return: The language of this SmoothStreamingRepresentation.
        :rtype: string_types
        """
        return self._language

    @language.setter
    def language(self, language):
        # type: (string_types) -> None
        """Sets the language of this SmoothStreamingRepresentation.

        Language of the MP4 file

        :param language: The language of this SmoothStreamingRepresentation.
        :type: string_types
        """

        if language is not None:
            if not isinstance(language, string_types):
                raise TypeError("Invalid type for `language`, type has to be `string_types`")

        self._language = language

    @property
    def track_name(self):
        # type: () -> string_types
        """Gets the track_name of this SmoothStreamingRepresentation.

        Track where this MP4 shoudl be added

        :return: The track_name of this SmoothStreamingRepresentation.
        :rtype: string_types
        """
        return self._track_name

    @track_name.setter
    def track_name(self, track_name):
        # type: (string_types) -> None
        """Sets the track_name of this SmoothStreamingRepresentation.

        Track where this MP4 shoudl be added

        :param track_name: The track_name of this SmoothStreamingRepresentation.
        :type: string_types
        """

        if track_name is not None:
            if not isinstance(track_name, string_types):
                raise TypeError("Invalid type for `track_name`, type has to be `string_types`")

        self._track_name = track_name

    @property
    def priority(self):
        # type: () -> int
        """Gets the priority of this SmoothStreamingRepresentation.

        Specifies the priority of this representation. In the manifest, representations will appear ordered by descending priority values.

        :return: The priority of this SmoothStreamingRepresentation.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        # type: (int) -> None
        """Sets the priority of this SmoothStreamingRepresentation.

        Specifies the priority of this representation. In the manifest, representations will appear ordered by descending priority values.

        :param priority: The priority of this SmoothStreamingRepresentation.
        :type: int
        """

        if priority is not None:
            if not isinstance(priority, int):
                raise TypeError("Invalid type for `priority`, type has to be `int`")

        self._priority = priority

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SmoothStreamingRepresentation, self), "to_dict"):
            result = super(SmoothStreamingRepresentation, self).to_dict()
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
        if not isinstance(other, SmoothStreamingRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
