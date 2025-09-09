# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.muxing import Muxing
from bitmovin_api_sdk.models.stream_conditions_mode import StreamConditionsMode
from bitmovin_api_sdk.models.ts_muxing_configuration import TsMuxingConfiguration
import pprint
import six


class TsMuxing(Muxing):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 streams=None,
                 outputs=None,
                 avg_bitrate=None,
                 min_bitrate=None,
                 max_bitrate=None,
                 ignored_by=None,
                 stream_conditions_mode=None,
                 segment_length=None,
                 minimum_segment_length=None,
                 segment_naming=None,
                 segment_naming_template=None,
                 start_offset=None,
                 segments_muxed=None,
                 configuration=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[MuxingStream], list[EncodingOutput], int, int, int, list[Ignoring], StreamConditionsMode, float, float, string_types, string_types, int, int, TsMuxingConfiguration) -> None
        super(TsMuxing, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, streams=streams, outputs=outputs, avg_bitrate=avg_bitrate, min_bitrate=min_bitrate, max_bitrate=max_bitrate, ignored_by=ignored_by, stream_conditions_mode=stream_conditions_mode)

        self._segment_length = None
        self._minimum_segment_length = None
        self._segment_naming = None
        self._segment_naming_template = None
        self._start_offset = None
        self._segments_muxed = None
        self._configuration = None
        self.discriminator = None

        if segment_length is not None:
            self.segment_length = segment_length
        if minimum_segment_length is not None:
            self.minimum_segment_length = minimum_segment_length
        if segment_naming is not None:
            self.segment_naming = segment_naming
        if segment_naming_template is not None:
            self.segment_naming_template = segment_naming_template
        if start_offset is not None:
            self.start_offset = start_offset
        if segments_muxed is not None:
            self.segments_muxed = segments_muxed
        if configuration is not None:
            self.configuration = configuration

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(TsMuxing, self), 'openapi_types'):
            types = getattr(super(TsMuxing, self), 'openapi_types')

        types.update({
            'segment_length': 'float',
            'minimum_segment_length': 'float',
            'segment_naming': 'string_types',
            'segment_naming_template': 'string_types',
            'start_offset': 'int',
            'segments_muxed': 'int',
            'configuration': 'TsMuxingConfiguration'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(TsMuxing, self), 'attribute_map'):
            attributes = getattr(super(TsMuxing, self), 'attribute_map')

        attributes.update({
            'segment_length': 'segmentLength',
            'minimum_segment_length': 'minimumSegmentLength',
            'segment_naming': 'segmentNaming',
            'segment_naming_template': 'segmentNamingTemplate',
            'start_offset': 'startOffset',
            'segments_muxed': 'segmentsMuxed',
            'configuration': 'configuration'
        })
        return attributes

    @property
    def segment_length(self):
        # type: () -> float
        """Gets the segment_length of this TsMuxing.

        Length of the fragments in seconds

        :return: The segment_length of this TsMuxing.
        :rtype: float
        """
        return self._segment_length

    @segment_length.setter
    def segment_length(self, segment_length):
        # type: (float) -> None
        """Sets the segment_length of this TsMuxing.

        Length of the fragments in seconds

        :param segment_length: The segment_length of this TsMuxing.
        :type: float
        """

        if segment_length is not None:
            if not isinstance(segment_length, (float, int)):
                raise TypeError("Invalid type for `segment_length`, type has to be `float`")

        self._segment_length = segment_length

    @property
    def minimum_segment_length(self):
        # type: () -> float
        """Gets the minimum_segment_length of this TsMuxing.

        Prevents creation of very short segments (in seconds). If the last segment is shorter than minimumSegmentLength or there is a custom keyframe too close to a segment boundary, short segments will be omitted by removing segment boundaries, resulting in a segment of a size up to segmentLength + minimumSegmentLength.

        :return: The minimum_segment_length of this TsMuxing.
        :rtype: float
        """
        return self._minimum_segment_length

    @minimum_segment_length.setter
    def minimum_segment_length(self, minimum_segment_length):
        # type: (float) -> None
        """Sets the minimum_segment_length of this TsMuxing.

        Prevents creation of very short segments (in seconds). If the last segment is shorter than minimumSegmentLength or there is a custom keyframe too close to a segment boundary, short segments will be omitted by removing segment boundaries, resulting in a segment of a size up to segmentLength + minimumSegmentLength.

        :param minimum_segment_length: The minimum_segment_length of this TsMuxing.
        :type: float
        """

        if minimum_segment_length is not None:
            if not isinstance(minimum_segment_length, (float, int)):
                raise TypeError("Invalid type for `minimum_segment_length`, type has to be `float`")

        self._minimum_segment_length = minimum_segment_length

    @property
    def segment_naming(self):
        # type: () -> string_types
        """Gets the segment_naming of this TsMuxing.

        Segment naming policy

        :return: The segment_naming of this TsMuxing.
        :rtype: string_types
        """
        return self._segment_naming

    @segment_naming.setter
    def segment_naming(self, segment_naming):
        # type: (string_types) -> None
        """Sets the segment_naming of this TsMuxing.

        Segment naming policy

        :param segment_naming: The segment_naming of this TsMuxing.
        :type: string_types
        """

        if segment_naming is not None:
            if not isinstance(segment_naming, string_types):
                raise TypeError("Invalid type for `segment_naming`, type has to be `string_types`")

        self._segment_naming = segment_naming

    @property
    def segment_naming_template(self):
        # type: () -> string_types
        """Gets the segment_naming_template of this TsMuxing.

        Segment naming policy containing one or both of the following placeholders: - '{rand_chars:x}', which will be replaced by a random alphanumeric string of length x (default 32)   on each (re)start of the encoding. The resulting string will be copied to the segmentNaming property.   Intended to avoid re-use of segment names after restarting a live encoding. - '{segment_rand_chars:x}', which will be replaced by a random alphanumeric string of length x (default 32)   for each different segment. This is intended to avoid guessing segment URLs by replacing segment numbers.  If segmentNamingTemplate is set, segmentNaming must not be set. 

        :return: The segment_naming_template of this TsMuxing.
        :rtype: string_types
        """
        return self._segment_naming_template

    @segment_naming_template.setter
    def segment_naming_template(self, segment_naming_template):
        # type: (string_types) -> None
        """Sets the segment_naming_template of this TsMuxing.

        Segment naming policy containing one or both of the following placeholders: - '{rand_chars:x}', which will be replaced by a random alphanumeric string of length x (default 32)   on each (re)start of the encoding. The resulting string will be copied to the segmentNaming property.   Intended to avoid re-use of segment names after restarting a live encoding. - '{segment_rand_chars:x}', which will be replaced by a random alphanumeric string of length x (default 32)   for each different segment. This is intended to avoid guessing segment URLs by replacing segment numbers.  If segmentNamingTemplate is set, segmentNaming must not be set. 

        :param segment_naming_template: The segment_naming_template of this TsMuxing.
        :type: string_types
        """

        if segment_naming_template is not None:
            if not isinstance(segment_naming_template, string_types):
                raise TypeError("Invalid type for `segment_naming_template`, type has to be `string_types`")

        self._segment_naming_template = segment_naming_template

    @property
    def start_offset(self):
        # type: () -> int
        """Gets the start_offset of this TsMuxing.

        Offset of MPEG-TS timestamps in seconds. E.g., first packet will start with PTS 900,000 for a 10 seconds offset (90,000 MPEG-TS timescale).

        :return: The start_offset of this TsMuxing.
        :rtype: int
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        # type: (int) -> None
        """Sets the start_offset of this TsMuxing.

        Offset of MPEG-TS timestamps in seconds. E.g., first packet will start with PTS 900,000 for a 10 seconds offset (90,000 MPEG-TS timescale).

        :param start_offset: The start_offset of this TsMuxing.
        :type: int
        """

        if start_offset is not None:
            if not isinstance(start_offset, int):
                raise TypeError("Invalid type for `start_offset`, type has to be `int`")

        self._start_offset = start_offset

    @property
    def segments_muxed(self):
        # type: () -> int
        """Gets the segments_muxed of this TsMuxing.

        Number of segments which have been encoded

        :return: The segments_muxed of this TsMuxing.
        :rtype: int
        """
        return self._segments_muxed

    @segments_muxed.setter
    def segments_muxed(self, segments_muxed):
        # type: (int) -> None
        """Sets the segments_muxed of this TsMuxing.

        Number of segments which have been encoded

        :param segments_muxed: The segments_muxed of this TsMuxing.
        :type: int
        """

        if segments_muxed is not None:
            if not isinstance(segments_muxed, int):
                raise TypeError("Invalid type for `segments_muxed`, type has to be `int`")

        self._segments_muxed = segments_muxed

    @property
    def configuration(self):
        # type: () -> TsMuxingConfiguration
        """Gets the configuration of this TsMuxing.

        Advanced Configuration of the MPEG Transport Stream Parameters

        :return: The configuration of this TsMuxing.
        :rtype: TsMuxingConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        # type: (TsMuxingConfiguration) -> None
        """Sets the configuration of this TsMuxing.

        Advanced Configuration of the MPEG Transport Stream Parameters

        :param configuration: The configuration of this TsMuxing.
        :type: TsMuxingConfiguration
        """

        if configuration is not None:
            if not isinstance(configuration, TsMuxingConfiguration):
                raise TypeError("Invalid type for `configuration`, type has to be `TsMuxingConfiguration`")

        self._configuration = configuration

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(TsMuxing, self), "to_dict"):
            result = super(TsMuxing, self).to_dict()
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
        if not isinstance(other, TsMuxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
