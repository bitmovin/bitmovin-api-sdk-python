# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.muxing import Muxing
from bitmovin_api_sdk.models.pts_align_mode import PTSAlignMode
from bitmovin_api_sdk.models.stream_conditions_mode import StreamConditionsMode
import pprint
import six


class Fmp4Muxing(Muxing):
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
                 init_segment_name=None,
                 init_segment_name_template=None,
                 write_duration_per_sample=None,
                 signal_scte35_as_emsg=None,
                 segments_muxed=None,
                 pts_align_mode=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[MuxingStream], list[EncodingOutput], int, int, int, list[Ignoring], StreamConditionsMode, float, float, string_types, string_types, string_types, string_types, bool, bool, int, PTSAlignMode) -> None
        super(Fmp4Muxing, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, streams=streams, outputs=outputs, avg_bitrate=avg_bitrate, min_bitrate=min_bitrate, max_bitrate=max_bitrate, ignored_by=ignored_by, stream_conditions_mode=stream_conditions_mode)

        self._segment_length = None
        self._minimum_segment_length = None
        self._segment_naming = None
        self._segment_naming_template = None
        self._init_segment_name = None
        self._init_segment_name_template = None
        self._write_duration_per_sample = None
        self._signal_scte35_as_emsg = None
        self._segments_muxed = None
        self._pts_align_mode = None
        self.discriminator = None

        if segment_length is not None:
            self.segment_length = segment_length
        if minimum_segment_length is not None:
            self.minimum_segment_length = minimum_segment_length
        if segment_naming is not None:
            self.segment_naming = segment_naming
        if segment_naming_template is not None:
            self.segment_naming_template = segment_naming_template
        if init_segment_name is not None:
            self.init_segment_name = init_segment_name
        if init_segment_name_template is not None:
            self.init_segment_name_template = init_segment_name_template
        if write_duration_per_sample is not None:
            self.write_duration_per_sample = write_duration_per_sample
        if signal_scte35_as_emsg is not None:
            self.signal_scte35_as_emsg = signal_scte35_as_emsg
        if segments_muxed is not None:
            self.segments_muxed = segments_muxed
        if pts_align_mode is not None:
            self.pts_align_mode = pts_align_mode

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Fmp4Muxing, self), 'openapi_types'):
            types = getattr(super(Fmp4Muxing, self), 'openapi_types')

        types.update({
            'segment_length': 'float',
            'minimum_segment_length': 'float',
            'segment_naming': 'string_types',
            'segment_naming_template': 'string_types',
            'init_segment_name': 'string_types',
            'init_segment_name_template': 'string_types',
            'write_duration_per_sample': 'bool',
            'signal_scte35_as_emsg': 'bool',
            'segments_muxed': 'int',
            'pts_align_mode': 'PTSAlignMode'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Fmp4Muxing, self), 'attribute_map'):
            attributes = getattr(super(Fmp4Muxing, self), 'attribute_map')

        attributes.update({
            'segment_length': 'segmentLength',
            'minimum_segment_length': 'minimumSegmentLength',
            'segment_naming': 'segmentNaming',
            'segment_naming_template': 'segmentNamingTemplate',
            'init_segment_name': 'initSegmentName',
            'init_segment_name_template': 'initSegmentNameTemplate',
            'write_duration_per_sample': 'writeDurationPerSample',
            'signal_scte35_as_emsg': 'signalScte35AsEmsg',
            'segments_muxed': 'segmentsMuxed',
            'pts_align_mode': 'ptsAlignMode'
        })
        return attributes

    @property
    def segment_length(self):
        # type: () -> float
        """Gets the segment_length of this Fmp4Muxing.

        Length of the fragments in seconds (required)

        :return: The segment_length of this Fmp4Muxing.
        :rtype: float
        """
        return self._segment_length

    @segment_length.setter
    def segment_length(self, segment_length):
        # type: (float) -> None
        """Sets the segment_length of this Fmp4Muxing.

        Length of the fragments in seconds (required)

        :param segment_length: The segment_length of this Fmp4Muxing.
        :type: float
        """

        if segment_length is not None:
            if not isinstance(segment_length, (float, int)):
                raise TypeError("Invalid type for `segment_length`, type has to be `float`")

        self._segment_length = segment_length

    @property
    def minimum_segment_length(self):
        # type: () -> float
        """Gets the minimum_segment_length of this Fmp4Muxing.

        Prevents creation of very short segments (in seconds). If the last segment is shorter than minimumSegmentLength or there is a custom keyframe too close to a segment boundary, short segments will be omitted by removing segment boundaries, resulting in a segment of a size up to segmentLength + minimumSegmentLength.

        :return: The minimum_segment_length of this Fmp4Muxing.
        :rtype: float
        """
        return self._minimum_segment_length

    @minimum_segment_length.setter
    def minimum_segment_length(self, minimum_segment_length):
        # type: (float) -> None
        """Sets the minimum_segment_length of this Fmp4Muxing.

        Prevents creation of very short segments (in seconds). If the last segment is shorter than minimumSegmentLength or there is a custom keyframe too close to a segment boundary, short segments will be omitted by removing segment boundaries, resulting in a segment of a size up to segmentLength + minimumSegmentLength.

        :param minimum_segment_length: The minimum_segment_length of this Fmp4Muxing.
        :type: float
        """

        if minimum_segment_length is not None:
            if not isinstance(minimum_segment_length, (float, int)):
                raise TypeError("Invalid type for `minimum_segment_length`, type has to be `float`")

        self._minimum_segment_length = minimum_segment_length

    @property
    def segment_naming(self):
        # type: () -> string_types
        """Gets the segment_naming of this Fmp4Muxing.

        Segment naming policy

        :return: The segment_naming of this Fmp4Muxing.
        :rtype: string_types
        """
        return self._segment_naming

    @segment_naming.setter
    def segment_naming(self, segment_naming):
        # type: (string_types) -> None
        """Sets the segment_naming of this Fmp4Muxing.

        Segment naming policy

        :param segment_naming: The segment_naming of this Fmp4Muxing.
        :type: string_types
        """

        if segment_naming is not None:
            if not isinstance(segment_naming, string_types):
                raise TypeError("Invalid type for `segment_naming`, type has to be `string_types`")

        self._segment_naming = segment_naming

    @property
    def segment_naming_template(self):
        # type: () -> string_types
        """Gets the segment_naming_template of this Fmp4Muxing.

        Segment naming policy containing one or both of the following placeholders: - '{rand_chars:x}', which will be replaced by a random alphanumeric string of length x (default 32)   on each (re)start of the encoding. The resulting string will be copied to the segmentNaming property.   Intended to avoid re-use of segment names after restarting a live encoding. - '{segment_rand_chars:x}', which will be replaced by a random alphanumeric string of length x (default 32)   for each different segment. This is intended to avoid guessing segment URLs by replacing segment numbers.  If segmentNamingTemplate is set, segmentNaming must not be set. 

        :return: The segment_naming_template of this Fmp4Muxing.
        :rtype: string_types
        """
        return self._segment_naming_template

    @segment_naming_template.setter
    def segment_naming_template(self, segment_naming_template):
        # type: (string_types) -> None
        """Sets the segment_naming_template of this Fmp4Muxing.

        Segment naming policy containing one or both of the following placeholders: - '{rand_chars:x}', which will be replaced by a random alphanumeric string of length x (default 32)   on each (re)start of the encoding. The resulting string will be copied to the segmentNaming property.   Intended to avoid re-use of segment names after restarting a live encoding. - '{segment_rand_chars:x}', which will be replaced by a random alphanumeric string of length x (default 32)   for each different segment. This is intended to avoid guessing segment URLs by replacing segment numbers.  If segmentNamingTemplate is set, segmentNaming must not be set. 

        :param segment_naming_template: The segment_naming_template of this Fmp4Muxing.
        :type: string_types
        """

        if segment_naming_template is not None:
            if not isinstance(segment_naming_template, string_types):
                raise TypeError("Invalid type for `segment_naming_template`, type has to be `string_types`")

        self._segment_naming_template = segment_naming_template

    @property
    def init_segment_name(self):
        # type: () -> string_types
        """Gets the init_segment_name of this Fmp4Muxing.

        Init segment name

        :return: The init_segment_name of this Fmp4Muxing.
        :rtype: string_types
        """
        return self._init_segment_name

    @init_segment_name.setter
    def init_segment_name(self, init_segment_name):
        # type: (string_types) -> None
        """Sets the init_segment_name of this Fmp4Muxing.

        Init segment name

        :param init_segment_name: The init_segment_name of this Fmp4Muxing.
        :type: string_types
        """

        if init_segment_name is not None:
            if not isinstance(init_segment_name, string_types):
                raise TypeError("Invalid type for `init_segment_name`, type has to be `string_types`")

        self._init_segment_name = init_segment_name

    @property
    def init_segment_name_template(self):
        # type: () -> string_types
        """Gets the init_segment_name_template of this Fmp4Muxing.

        Segment naming policy containing a placeholder of the format '{rand_chars:x}', which will be replaced by a random alphanumeric string of length x (default 32) on each (re)start of the encoding. The resulting string will be copied to the initSegmentName property. Intended to avoid re-use of segment names after restarting a live encoding. If initSegmentNameTemplate is set, initSegmentName must not be set.

        :return: The init_segment_name_template of this Fmp4Muxing.
        :rtype: string_types
        """
        return self._init_segment_name_template

    @init_segment_name_template.setter
    def init_segment_name_template(self, init_segment_name_template):
        # type: (string_types) -> None
        """Sets the init_segment_name_template of this Fmp4Muxing.

        Segment naming policy containing a placeholder of the format '{rand_chars:x}', which will be replaced by a random alphanumeric string of length x (default 32) on each (re)start of the encoding. The resulting string will be copied to the initSegmentName property. Intended to avoid re-use of segment names after restarting a live encoding. If initSegmentNameTemplate is set, initSegmentName must not be set.

        :param init_segment_name_template: The init_segment_name_template of this Fmp4Muxing.
        :type: string_types
        """

        if init_segment_name_template is not None:
            if not isinstance(init_segment_name_template, string_types):
                raise TypeError("Invalid type for `init_segment_name_template`, type has to be `string_types`")

        self._init_segment_name_template = init_segment_name_template

    @property
    def write_duration_per_sample(self):
        # type: () -> bool
        """Gets the write_duration_per_sample of this Fmp4Muxing.

        Writes the duration per sample into the sample entry in the Track Fragment Run Box. This could help to fix playback issues on legacy players. Enabling this flag increases the muxing overhead by 4 bytes per sample/frame.

        :return: The write_duration_per_sample of this Fmp4Muxing.
        :rtype: bool
        """
        return self._write_duration_per_sample

    @write_duration_per_sample.setter
    def write_duration_per_sample(self, write_duration_per_sample):
        # type: (bool) -> None
        """Sets the write_duration_per_sample of this Fmp4Muxing.

        Writes the duration per sample into the sample entry in the Track Fragment Run Box. This could help to fix playback issues on legacy players. Enabling this flag increases the muxing overhead by 4 bytes per sample/frame.

        :param write_duration_per_sample: The write_duration_per_sample of this Fmp4Muxing.
        :type: bool
        """

        if write_duration_per_sample is not None:
            if not isinstance(write_duration_per_sample, bool):
                raise TypeError("Invalid type for `write_duration_per_sample`, type has to be `bool`")

        self._write_duration_per_sample = write_duration_per_sample

    @property
    def signal_scte35_as_emsg(self):
        # type: () -> bool
        """Gets the signal_scte35_as_emsg of this Fmp4Muxing.

        Insert scte35 triggers as emsg boxes into the fMP4 segments.

        :return: The signal_scte35_as_emsg of this Fmp4Muxing.
        :rtype: bool
        """
        return self._signal_scte35_as_emsg

    @signal_scte35_as_emsg.setter
    def signal_scte35_as_emsg(self, signal_scte35_as_emsg):
        # type: (bool) -> None
        """Sets the signal_scte35_as_emsg of this Fmp4Muxing.

        Insert scte35 triggers as emsg boxes into the fMP4 segments.

        :param signal_scte35_as_emsg: The signal_scte35_as_emsg of this Fmp4Muxing.
        :type: bool
        """

        if signal_scte35_as_emsg is not None:
            if not isinstance(signal_scte35_as_emsg, bool):
                raise TypeError("Invalid type for `signal_scte35_as_emsg`, type has to be `bool`")

        self._signal_scte35_as_emsg = signal_scte35_as_emsg

    @property
    def segments_muxed(self):
        # type: () -> int
        """Gets the segments_muxed of this Fmp4Muxing.

        Number of segments which have been encoded

        :return: The segments_muxed of this Fmp4Muxing.
        :rtype: int
        """
        return self._segments_muxed

    @segments_muxed.setter
    def segments_muxed(self, segments_muxed):
        # type: (int) -> None
        """Sets the segments_muxed of this Fmp4Muxing.

        Number of segments which have been encoded

        :param segments_muxed: The segments_muxed of this Fmp4Muxing.
        :type: int
        """

        if segments_muxed is not None:
            if not isinstance(segments_muxed, int):
                raise TypeError("Invalid type for `segments_muxed`, type has to be `int`")

        self._segments_muxed = segments_muxed

    @property
    def pts_align_mode(self):
        # type: () -> PTSAlignMode
        """Gets the pts_align_mode of this Fmp4Muxing.

        Alignment mode for composition / presentation timestamps (CTS/PTS). Only applies to h.264 and h.265

        :return: The pts_align_mode of this Fmp4Muxing.
        :rtype: PTSAlignMode
        """
        return self._pts_align_mode

    @pts_align_mode.setter
    def pts_align_mode(self, pts_align_mode):
        # type: (PTSAlignMode) -> None
        """Sets the pts_align_mode of this Fmp4Muxing.

        Alignment mode for composition / presentation timestamps (CTS/PTS). Only applies to h.264 and h.265

        :param pts_align_mode: The pts_align_mode of this Fmp4Muxing.
        :type: PTSAlignMode
        """

        if pts_align_mode is not None:
            if not isinstance(pts_align_mode, PTSAlignMode):
                raise TypeError("Invalid type for `pts_align_mode`, type has to be `PTSAlignMode`")

        self._pts_align_mode = pts_align_mode

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Fmp4Muxing, self), "to_dict"):
            result = super(Fmp4Muxing, self).to_dict()
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
        if not isinstance(other, Fmp4Muxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
