# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.muxing import Muxing
from bitmovin_api_sdk.models.stream_conditions_mode import StreamConditionsMode
import pprint
import six


class SegmentedRawMuxing(Muxing):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 streams=None,
                 outputs=None,
                 avg_bitrate=None,
                 min_bitrate=None,
                 max_bitrate=None,
                 ignored_by=None,
                 stream_conditions_mode=None,
                 segment_length=None,
                 segment_naming=None,
                 segments_muxed=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, list[MuxingStream], list[EncodingOutput], int, int, int, list[Ignoring], StreamConditionsMode, float, string_types, int) -> None
        super(SegmentedRawMuxing, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_, streams=streams, outputs=outputs, avg_bitrate=avg_bitrate, min_bitrate=min_bitrate, max_bitrate=max_bitrate, ignored_by=ignored_by, stream_conditions_mode=stream_conditions_mode)

        self._segment_length = None
        self._segment_naming = None
        self._segments_muxed = None
        self.discriminator = None

        if segment_length is not None:
            self.segment_length = segment_length
        if segment_naming is not None:
            self.segment_naming = segment_naming
        if segments_muxed is not None:
            self.segments_muxed = segments_muxed

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SegmentedRawMuxing, self), 'openapi_types'):
            types = getattr(super(SegmentedRawMuxing, self), 'openapi_types')

        types.update({
            'segment_length': 'float',
            'segment_naming': 'string_types',
            'segments_muxed': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SegmentedRawMuxing, self), 'attribute_map'):
            attributes = getattr(super(SegmentedRawMuxing, self), 'attribute_map')

        attributes.update({
            'segment_length': 'segmentLength',
            'segment_naming': 'segmentNaming',
            'segments_muxed': 'segmentsMuxed'
        })
        return attributes

    @property
    def segment_length(self):
        # type: () -> float
        """Gets the segment_length of this SegmentedRawMuxing.

        Length of the fragments in seconds (required)

        :return: The segment_length of this SegmentedRawMuxing.
        :rtype: float
        """
        return self._segment_length

    @segment_length.setter
    def segment_length(self, segment_length):
        # type: (float) -> None
        """Sets the segment_length of this SegmentedRawMuxing.

        Length of the fragments in seconds (required)

        :param segment_length: The segment_length of this SegmentedRawMuxing.
        :type: float
        """

        if segment_length is not None:
            if not isinstance(segment_length, (float, int)):
                raise TypeError("Invalid type for `segment_length`, type has to be `float`")

        self._segment_length = segment_length

    @property
    def segment_naming(self):
        # type: () -> string_types
        """Gets the segment_naming of this SegmentedRawMuxing.

        Segment naming policy (required)

        :return: The segment_naming of this SegmentedRawMuxing.
        :rtype: string_types
        """
        return self._segment_naming

    @segment_naming.setter
    def segment_naming(self, segment_naming):
        # type: (string_types) -> None
        """Sets the segment_naming of this SegmentedRawMuxing.

        Segment naming policy (required)

        :param segment_naming: The segment_naming of this SegmentedRawMuxing.
        :type: string_types
        """

        if segment_naming is not None:
            if not isinstance(segment_naming, string_types):
                raise TypeError("Invalid type for `segment_naming`, type has to be `string_types`")

        self._segment_naming = segment_naming

    @property
    def segments_muxed(self):
        # type: () -> int
        """Gets the segments_muxed of this SegmentedRawMuxing.

        Number of segments which have been encoded

        :return: The segments_muxed of this SegmentedRawMuxing.
        :rtype: int
        """
        return self._segments_muxed

    @segments_muxed.setter
    def segments_muxed(self, segments_muxed):
        # type: (int) -> None
        """Sets the segments_muxed of this SegmentedRawMuxing.

        Number of segments which have been encoded

        :param segments_muxed: The segments_muxed of this SegmentedRawMuxing.
        :type: int
        """

        if segments_muxed is not None:
            if not isinstance(segments_muxed, int):
                raise TypeError("Invalid type for `segments_muxed`, type has to be `int`")

        self._segments_muxed = segments_muxed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SegmentedRawMuxing, self), "to_dict"):
            result = super(SegmentedRawMuxing, self).to_dict()
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
        if not isinstance(other, SegmentedRawMuxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
