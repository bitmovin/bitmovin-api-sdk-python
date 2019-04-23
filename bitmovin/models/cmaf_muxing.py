# coding: utf-8

from bitmovin.models.encoding_output import EncodingOutput
from bitmovin.models.ignoring import Ignoring
from bitmovin.models.muxing import Muxing
from bitmovin.models.muxing_stream import MuxingStream
from bitmovin.models.stream_conditions_mode import StreamConditionsMode
import pprint
import six
from datetime import datetime
from enum import Enum


class CmafMuxing(Muxing):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(CmafMuxing, self).openapi_types
        types.update({
            'segment_length': 'float',
            'segment_naming': 'str',
            'segment_naming_template': 'str',
            'init_segment_name': 'str',
            'init_segment_name_template': 'str',
            'segments_muxed': 'int',
            'frames_per_cmaf_chunk': 'object'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(CmafMuxing, self).attribute_map
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

    def __init__(self, segment_length=None, segment_naming=None, segment_naming_template=None, init_segment_name=None, init_segment_name_template=None, segments_muxed=None, frames_per_cmaf_chunk=None, *args, **kwargs):
        super(CmafMuxing, self).__init__(*args, **kwargs)

        self._segment_length = None
        self._segment_naming = None
        self._segment_naming_template = None
        self._init_segment_name = None
        self._init_segment_name_template = None
        self._segments_muxed = None
        self._frames_per_cmaf_chunk = None
        self.discriminator = None

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
    def segment_length(self):
        """Gets the segment_length of this CmafMuxing.

        Length of the fragments in seconds

        :return: The segment_length of this CmafMuxing.
        :rtype: float
        """
        return self._segment_length

    @segment_length.setter
    def segment_length(self, segment_length):
        """Sets the segment_length of this CmafMuxing.

        Length of the fragments in seconds

        :param segment_length: The segment_length of this CmafMuxing.
        :type: float
        """

        if segment_length is not None:
            if not isinstance(segment_length, float):
                raise TypeError("Invalid type for `segment_length`, type has to be `float`")

            self._segment_length = segment_length


    @property
    def segment_naming(self):
        """Gets the segment_naming of this CmafMuxing.

        Segment naming policy

        :return: The segment_naming of this CmafMuxing.
        :rtype: str
        """
        return self._segment_naming

    @segment_naming.setter
    def segment_naming(self, segment_naming):
        """Sets the segment_naming of this CmafMuxing.

        Segment naming policy

        :param segment_naming: The segment_naming of this CmafMuxing.
        :type: str
        """

        if segment_naming is not None:
            if not isinstance(segment_naming, str):
                raise TypeError("Invalid type for `segment_naming`, type has to be `str`")

            self._segment_naming = segment_naming


    @property
    def segment_naming_template(self):
        """Gets the segment_naming_template of this CmafMuxing.

        Segment naming policy with placeholders which will be replaced during the encoding. The result will be saved in segmentNaming. {rand:4} gets replaced with an alphanumeric string of length specified after the colon. Defaults to 32. If this field is set, segmentNaming must not be specified.

        :return: The segment_naming_template of this CmafMuxing.
        :rtype: str
        """
        return self._segment_naming_template

    @segment_naming_template.setter
    def segment_naming_template(self, segment_naming_template):
        """Sets the segment_naming_template of this CmafMuxing.

        Segment naming policy with placeholders which will be replaced during the encoding. The result will be saved in segmentNaming. {rand:4} gets replaced with an alphanumeric string of length specified after the colon. Defaults to 32. If this field is set, segmentNaming must not be specified.

        :param segment_naming_template: The segment_naming_template of this CmafMuxing.
        :type: str
        """

        if segment_naming_template is not None:
            if not isinstance(segment_naming_template, str):
                raise TypeError("Invalid type for `segment_naming_template`, type has to be `str`")

            self._segment_naming_template = segment_naming_template


    @property
    def init_segment_name(self):
        """Gets the init_segment_name of this CmafMuxing.

        Init segment name

        :return: The init_segment_name of this CmafMuxing.
        :rtype: str
        """
        return self._init_segment_name

    @init_segment_name.setter
    def init_segment_name(self, init_segment_name):
        """Sets the init_segment_name of this CmafMuxing.

        Init segment name

        :param init_segment_name: The init_segment_name of this CmafMuxing.
        :type: str
        """

        if init_segment_name is not None:
            if not isinstance(init_segment_name, str):
                raise TypeError("Invalid type for `init_segment_name`, type has to be `str`")

            self._init_segment_name = init_segment_name


    @property
    def init_segment_name_template(self):
        """Gets the init_segment_name_template of this CmafMuxing.

        Segment naming policy with placeholders which will be replaced during the encoding, similar to segmentNamingTemplate. The result will be saved in initSegmentName. If this field is set, initSegmentName must not be specified and segmentNamingTemplate should be set. 

        :return: The init_segment_name_template of this CmafMuxing.
        :rtype: str
        """
        return self._init_segment_name_template

    @init_segment_name_template.setter
    def init_segment_name_template(self, init_segment_name_template):
        """Sets the init_segment_name_template of this CmafMuxing.

        Segment naming policy with placeholders which will be replaced during the encoding, similar to segmentNamingTemplate. The result will be saved in initSegmentName. If this field is set, initSegmentName must not be specified and segmentNamingTemplate should be set. 

        :param init_segment_name_template: The init_segment_name_template of this CmafMuxing.
        :type: str
        """

        if init_segment_name_template is not None:
            if not isinstance(init_segment_name_template, str):
                raise TypeError("Invalid type for `init_segment_name_template`, type has to be `str`")

            self._init_segment_name_template = init_segment_name_template


    @property
    def segments_muxed(self):
        """Gets the segments_muxed of this CmafMuxing.

        Number of segments which have been encoded

        :return: The segments_muxed of this CmafMuxing.
        :rtype: int
        """
        return self._segments_muxed

    @segments_muxed.setter
    def segments_muxed(self, segments_muxed):
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
        """Gets the frames_per_cmaf_chunk of this CmafMuxing.

        Number of media frames per CMAF chunk. Defaults to: Length of a segment in frames. Minimum: 1. Maximum: Length of a segment in frames.

        :return: The frames_per_cmaf_chunk of this CmafMuxing.
        :rtype: object
        """
        return self._frames_per_cmaf_chunk

    @frames_per_cmaf_chunk.setter
    def frames_per_cmaf_chunk(self, frames_per_cmaf_chunk):
        """Sets the frames_per_cmaf_chunk of this CmafMuxing.

        Number of media frames per CMAF chunk. Defaults to: Length of a segment in frames. Minimum: 1. Maximum: Length of a segment in frames.

        :param frames_per_cmaf_chunk: The frames_per_cmaf_chunk of this CmafMuxing.
        :type: object
        """

        if frames_per_cmaf_chunk is not None:
            if not isinstance(frames_per_cmaf_chunk, object):
                raise TypeError("Invalid type for `frames_per_cmaf_chunk`, type has to be `object`")

            self._frames_per_cmaf_chunk = frames_per_cmaf_chunk

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(CmafMuxing, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(CmafMuxing, dict):
                for key, value in self.items():
                    result[key] = value

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
