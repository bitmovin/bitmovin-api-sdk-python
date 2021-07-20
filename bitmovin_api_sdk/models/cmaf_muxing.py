# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.muxing import Muxing
from bitmovin_api_sdk.models.stream_conditions_mode import StreamConditionsMode
import pprint
import six


class CmafMuxing(Muxing):
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
                 segment_naming=None,
                 segment_naming_template=None,
                 init_segment_name=None,
                 init_segment_name_template=None,
                 segments_muxed=None,
                 frames_per_cmaf_chunk=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[MuxingStream], list[EncodingOutput], int, int, int, list[Ignoring], StreamConditionsMode, float, string_types, string_types, string_types, string_types, int, int) -> None
        super(CmafMuxing, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, streams=streams, outputs=outputs, avg_bitrate=avg_bitrate, min_bitrate=min_bitrate, max_bitrate=max_bitrate, ignored_by=ignored_by, stream_conditions_mode=stream_conditions_mode)

        self._segment_length = None
        self._segment_naming = None
        self._segment_naming_template = None
        self._init_segment_name = None
        self._init_segment_name_template = None
        self._segments_muxed = None
        self._frames_per_cmaf_chunk = None
        self.discriminator = None

        if segment_length is not None:
            self.segment_length = segment_length
        if segment_naming is not None:
            self.segment_naming = segment_naming
        if segment_naming_template is not None:
            self.segment_naming_template = segment_naming_template
        if init_segment_name is not None:
            self.init_segment_name = init_segment_name
        if init_segment_name_template is not None:
            self.init_segment_name_template = init_segment_name_template
        if segments_muxed is not None:
            self.segments_muxed = segments_muxed
        if frames_per_cmaf_chunk is not None:
            self.frames_per_cmaf_chunk = frames_per_cmaf_chunk

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(CmafMuxing, self), 'openapi_types'):
            types = getattr(super(CmafMuxing, self), 'openapi_types')

        types.update({
            'segment_length': 'float',
            'segment_naming': 'string_types',
            'segment_naming_template': 'string_types',
            'init_segment_name': 'string_types',
            'init_segment_name_template': 'string_types',
            'segments_muxed': 'int',
            'frames_per_cmaf_chunk': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(CmafMuxing, self), 'attribute_map'):
            attributes = getattr(super(CmafMuxing, self), 'attribute_map')

        attributes.update({
            'segment_length': 'segmentLength',
            'segment_naming': 'segmentNaming',
            'segment_naming_template': 'segmentNamingTemplate',
            'init_segment_name': 'initSegmentName',
            'init_segment_name_template': 'initSegmentNameTemplate',
            'segments_muxed': 'segmentsMuxed',
            'frames_per_cmaf_chunk': 'framesPerCmafChunk'
        })
        return attributes

    @property
    def segment_length(self):
        # type: () -> float
        """Gets the segment_length of this CmafMuxing.

        Length of the fragments in seconds (required)

        :return: The segment_length of this CmafMuxing.
        :rtype: float
        """
        return self._segment_length

    @segment_length.setter
    def segment_length(self, segment_length):
        # type: (float) -> None
        """Sets the segment_length of this CmafMuxing.

        Length of the fragments in seconds (required)

        :param segment_length: The segment_length of this CmafMuxing.
        :type: float
        """

        if segment_length is not None:
            if not isinstance(segment_length, (float, int)):
                raise TypeError("Invalid type for `segment_length`, type has to be `float`")

        self._segment_length = segment_length

    @property
    def segment_naming(self):
        # type: () -> string_types
        """Gets the segment_naming of this CmafMuxing.

        Segment naming policy

        :return: The segment_naming of this CmafMuxing.
        :rtype: string_types
        """
        return self._segment_naming

    @segment_naming.setter
    def segment_naming(self, segment_naming):
        # type: (string_types) -> None
        """Sets the segment_naming of this CmafMuxing.

        Segment naming policy

        :param segment_naming: The segment_naming of this CmafMuxing.
        :type: string_types
        """

        if segment_naming is not None:
            if not isinstance(segment_naming, string_types):
                raise TypeError("Invalid type for `segment_naming`, type has to be `string_types`")

        self._segment_naming = segment_naming

    @property
    def segment_naming_template(self):
        # type: () -> string_types
        """Gets the segment_naming_template of this CmafMuxing.

        Segment naming policy containing a placeholder of the format '{rand_chars:x}', which will be replaced by a random alphanumeric string of length x (default 32) on each (re)start of the encoding. The resulting string will be copied to the segmentNaming property. Intended to avoid re-use of segment names after restarting a live encoding. If segmentNamingTemplate is set, segmentNaming must not be set.

        :return: The segment_naming_template of this CmafMuxing.
        :rtype: string_types
        """
        return self._segment_naming_template

    @segment_naming_template.setter
    def segment_naming_template(self, segment_naming_template):
        # type: (string_types) -> None
        """Sets the segment_naming_template of this CmafMuxing.

        Segment naming policy containing a placeholder of the format '{rand_chars:x}', which will be replaced by a random alphanumeric string of length x (default 32) on each (re)start of the encoding. The resulting string will be copied to the segmentNaming property. Intended to avoid re-use of segment names after restarting a live encoding. If segmentNamingTemplate is set, segmentNaming must not be set.

        :param segment_naming_template: The segment_naming_template of this CmafMuxing.
        :type: string_types
        """

        if segment_naming_template is not None:
            if not isinstance(segment_naming_template, string_types):
                raise TypeError("Invalid type for `segment_naming_template`, type has to be `string_types`")

        self._segment_naming_template = segment_naming_template

    @property
    def init_segment_name(self):
        # type: () -> string_types
        """Gets the init_segment_name of this CmafMuxing.

        Init segment name

        :return: The init_segment_name of this CmafMuxing.
        :rtype: string_types
        """
        return self._init_segment_name

    @init_segment_name.setter
    def init_segment_name(self, init_segment_name):
        # type: (string_types) -> None
        """Sets the init_segment_name of this CmafMuxing.

        Init segment name

        :param init_segment_name: The init_segment_name of this CmafMuxing.
        :type: string_types
        """

        if init_segment_name is not None:
            if not isinstance(init_segment_name, string_types):
                raise TypeError("Invalid type for `init_segment_name`, type has to be `string_types`")

        self._init_segment_name = init_segment_name

    @property
    def init_segment_name_template(self):
        # type: () -> string_types
        """Gets the init_segment_name_template of this CmafMuxing.

        Segment naming policy containing a placeholder of the format '{rand_chars:x}', which will be replaced by a random alphanumeric string of length x (default 32) on each (re)start of the encoding. The resulting string will be copied to the initSegmentName property. Intended to avoid re-use of segment names after restarting a live encoding. If initSegmentNameTemplate is set, initSegmentName must not be set.

        :return: The init_segment_name_template of this CmafMuxing.
        :rtype: string_types
        """
        return self._init_segment_name_template

    @init_segment_name_template.setter
    def init_segment_name_template(self, init_segment_name_template):
        # type: (string_types) -> None
        """Sets the init_segment_name_template of this CmafMuxing.

        Segment naming policy containing a placeholder of the format '{rand_chars:x}', which will be replaced by a random alphanumeric string of length x (default 32) on each (re)start of the encoding. The resulting string will be copied to the initSegmentName property. Intended to avoid re-use of segment names after restarting a live encoding. If initSegmentNameTemplate is set, initSegmentName must not be set.

        :param init_segment_name_template: The init_segment_name_template of this CmafMuxing.
        :type: string_types
        """

        if init_segment_name_template is not None:
            if not isinstance(init_segment_name_template, string_types):
                raise TypeError("Invalid type for `init_segment_name_template`, type has to be `string_types`")

        self._init_segment_name_template = init_segment_name_template

    @property
    def segments_muxed(self):
        # type: () -> int
        """Gets the segments_muxed of this CmafMuxing.

        Number of segments which have been encoded

        :return: The segments_muxed of this CmafMuxing.
        :rtype: int
        """
        return self._segments_muxed

    @segments_muxed.setter
    def segments_muxed(self, segments_muxed):
        # type: (int) -> None
        """Sets the segments_muxed of this CmafMuxing.

        Number of segments which have been encoded

        :param segments_muxed: The segments_muxed of this CmafMuxing.
        :type: int
        """

        if segments_muxed is not None:
            if not isinstance(segments_muxed, int):
                raise TypeError("Invalid type for `segments_muxed`, type has to be `int`")

        self._segments_muxed = segments_muxed

    @property
    def frames_per_cmaf_chunk(self):
        # type: () -> int
        """Gets the frames_per_cmaf_chunk of this CmafMuxing.

        Number of media frames per CMAF chunk. Defaults to: Length of a segment in frames. Minimum: 1. Maximum: Length of a segment in frames.

        :return: The frames_per_cmaf_chunk of this CmafMuxing.
        :rtype: int
        """
        return self._frames_per_cmaf_chunk

    @frames_per_cmaf_chunk.setter
    def frames_per_cmaf_chunk(self, frames_per_cmaf_chunk):
        # type: (int) -> None
        """Sets the frames_per_cmaf_chunk of this CmafMuxing.

        Number of media frames per CMAF chunk. Defaults to: Length of a segment in frames. Minimum: 1. Maximum: Length of a segment in frames.

        :param frames_per_cmaf_chunk: The frames_per_cmaf_chunk of this CmafMuxing.
        :type: int
        """

        if frames_per_cmaf_chunk is not None:
            if not isinstance(frames_per_cmaf_chunk, int):
                raise TypeError("Invalid type for `frames_per_cmaf_chunk`, type has to be `int`")

        self._frames_per_cmaf_chunk = frames_per_cmaf_chunk

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(CmafMuxing, self), "to_dict"):
            result = super(CmafMuxing, self).to_dict()
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
        if not isinstance(other, CmafMuxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
