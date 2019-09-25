# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.basic_media_info import BasicMediaInfo
import pprint
import six


class SegmentsMediaInfo(BasicMediaInfo):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 group_id=None,
                 language=None,
                 assoc_language=None,
                 name=None,
                 is_default=None,
                 autoselect=None,
                 characteristics=None,
                 segment_path=None,
                 encoding_id=None,
                 stream_id=None,
                 muxing_id=None,
                 drm_id=None,
                 start_segment_number=None,
                 end_segment_number=None):
        # type: (string_types, string_types, string_types, string_types, string_types, bool, bool, list[string_types], string_types, string_types, string_types, string_types, string_types, int, int) -> None
        super(SegmentsMediaInfo, self).__init__(id_=id_, group_id=group_id, language=language, assoc_language=assoc_language, name=name, is_default=is_default, autoselect=autoselect, characteristics=characteristics)

        self._segment_path = None
        self._encoding_id = None
        self._stream_id = None
        self._muxing_id = None
        self._drm_id = None
        self._start_segment_number = None
        self._end_segment_number = None
        self.discriminator = None

        if segment_path is not None:
            self.segment_path = segment_path
        if encoding_id is not None:
            self.encoding_id = encoding_id
        if stream_id is not None:
            self.stream_id = stream_id
        if muxing_id is not None:
            self.muxing_id = muxing_id
        if drm_id is not None:
            self.drm_id = drm_id
        if start_segment_number is not None:
            self.start_segment_number = start_segment_number
        if end_segment_number is not None:
            self.end_segment_number = end_segment_number

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SegmentsMediaInfo, self), 'openapi_types'):
            types = getattr(super(SegmentsMediaInfo, self), 'openapi_types')

        types.update({
            'segment_path': 'string_types',
            'encoding_id': 'string_types',
            'stream_id': 'string_types',
            'muxing_id': 'string_types',
            'drm_id': 'string_types',
            'start_segment_number': 'int',
            'end_segment_number': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SegmentsMediaInfo, self), 'attribute_map'):
            attributes = getattr(super(SegmentsMediaInfo, self), 'attribute_map')

        attributes.update({
            'segment_path': 'segmentPath',
            'encoding_id': 'encodingId',
            'stream_id': 'streamId',
            'muxing_id': 'muxingId',
            'drm_id': 'drmId',
            'start_segment_number': 'startSegmentNumber',
            'end_segment_number': 'endSegmentNumber'
        })
        return attributes

    @property
    def segment_path(self):
        # type: () -> string_types
        """Gets the segment_path of this SegmentsMediaInfo.

        Path to segments. (required)

        :return: The segment_path of this SegmentsMediaInfo.
        :rtype: string_types
        """
        return self._segment_path

    @segment_path.setter
    def segment_path(self, segment_path):
        # type: (string_types) -> None
        """Sets the segment_path of this SegmentsMediaInfo.

        Path to segments. (required)

        :param segment_path: The segment_path of this SegmentsMediaInfo.
        :type: string_types
        """

        if segment_path is not None:
            if not isinstance(segment_path, string_types):
                raise TypeError("Invalid type for `segment_path`, type has to be `string_types`")

        self._segment_path = segment_path

    @property
    def encoding_id(self):
        # type: () -> string_types
        """Gets the encoding_id of this SegmentsMediaInfo.

        Id of the encoding. (required)

        :return: The encoding_id of this SegmentsMediaInfo.
        :rtype: string_types
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        # type: (string_types) -> None
        """Sets the encoding_id of this SegmentsMediaInfo.

        Id of the encoding. (required)

        :param encoding_id: The encoding_id of this SegmentsMediaInfo.
        :type: string_types
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, string_types):
                raise TypeError("Invalid type for `encoding_id`, type has to be `string_types`")

        self._encoding_id = encoding_id

    @property
    def stream_id(self):
        # type: () -> string_types
        """Gets the stream_id of this SegmentsMediaInfo.

        Id of the stream. (required)

        :return: The stream_id of this SegmentsMediaInfo.
        :rtype: string_types
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        # type: (string_types) -> None
        """Sets the stream_id of this SegmentsMediaInfo.

        Id of the stream. (required)

        :param stream_id: The stream_id of this SegmentsMediaInfo.
        :type: string_types
        """

        if stream_id is not None:
            if not isinstance(stream_id, string_types):
                raise TypeError("Invalid type for `stream_id`, type has to be `string_types`")

        self._stream_id = stream_id

    @property
    def muxing_id(self):
        # type: () -> string_types
        """Gets the muxing_id of this SegmentsMediaInfo.

        Id of the muxing. (required)

        :return: The muxing_id of this SegmentsMediaInfo.
        :rtype: string_types
        """
        return self._muxing_id

    @muxing_id.setter
    def muxing_id(self, muxing_id):
        # type: (string_types) -> None
        """Sets the muxing_id of this SegmentsMediaInfo.

        Id of the muxing. (required)

        :param muxing_id: The muxing_id of this SegmentsMediaInfo.
        :type: string_types
        """

        if muxing_id is not None:
            if not isinstance(muxing_id, string_types):
                raise TypeError("Invalid type for `muxing_id`, type has to be `string_types`")

        self._muxing_id = muxing_id

    @property
    def drm_id(self):
        # type: () -> string_types
        """Gets the drm_id of this SegmentsMediaInfo.

        Id of the DRM.

        :return: The drm_id of this SegmentsMediaInfo.
        :rtype: string_types
        """
        return self._drm_id

    @drm_id.setter
    def drm_id(self, drm_id):
        # type: (string_types) -> None
        """Sets the drm_id of this SegmentsMediaInfo.

        Id of the DRM.

        :param drm_id: The drm_id of this SegmentsMediaInfo.
        :type: string_types
        """

        if drm_id is not None:
            if not isinstance(drm_id, string_types):
                raise TypeError("Invalid type for `drm_id`, type has to be `string_types`")

        self._drm_id = drm_id

    @property
    def start_segment_number(self):
        # type: () -> int
        """Gets the start_segment_number of this SegmentsMediaInfo.

        Number of the first segment. Default is 0.

        :return: The start_segment_number of this SegmentsMediaInfo.
        :rtype: int
        """
        return self._start_segment_number

    @start_segment_number.setter
    def start_segment_number(self, start_segment_number):
        # type: (int) -> None
        """Sets the start_segment_number of this SegmentsMediaInfo.

        Number of the first segment. Default is 0.

        :param start_segment_number: The start_segment_number of this SegmentsMediaInfo.
        :type: int
        """

        if start_segment_number is not None:
            if not isinstance(start_segment_number, int):
                raise TypeError("Invalid type for `start_segment_number`, type has to be `int`")

        self._start_segment_number = start_segment_number

    @property
    def end_segment_number(self):
        # type: () -> int
        """Gets the end_segment_number of this SegmentsMediaInfo.

        Number of the last segment. Default is the last one that was encoded.

        :return: The end_segment_number of this SegmentsMediaInfo.
        :rtype: int
        """
        return self._end_segment_number

    @end_segment_number.setter
    def end_segment_number(self, end_segment_number):
        # type: (int) -> None
        """Sets the end_segment_number of this SegmentsMediaInfo.

        Number of the last segment. Default is the last one that was encoded.

        :param end_segment_number: The end_segment_number of this SegmentsMediaInfo.
        :type: int
        """

        if end_segment_number is not None:
            if not isinstance(end_segment_number, int):
                raise TypeError("Invalid type for `end_segment_number`, type has to be `int`")

        self._end_segment_number = end_segment_number

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SegmentsMediaInfo, self), "to_dict"):
            result = super(SegmentsMediaInfo, self).to_dict()
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
        if not isinstance(other, SegmentsMediaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
