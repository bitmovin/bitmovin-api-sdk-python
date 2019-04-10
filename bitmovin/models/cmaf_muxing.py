# coding: utf-8

from bitmovin.models.encoding_output import EncodingOutput
from bitmovin.models.fmp4_muxing import Fmp4Muxing
from bitmovin.models.ignoring import Ignoring
from bitmovin.models.muxing_stream import MuxingStream
from bitmovin.models.stream_conditions_mode import StreamConditionsMode
import pprint
import six
from datetime import datetime
from enum import Enum


class CmafMuxing(Fmp4Muxing):
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
            'frames_per_cmaf_chunk': 'object'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(CmafMuxing, self).attribute_map
        attributes.update({
            'frames_per_cmaf_chunk': 'framesPerCmafChunk'
        })
        return attributes

    def __init__(self, frames_per_cmaf_chunk=None, *args, **kwargs):
        super(CmafMuxing, self).__init__(*args, **kwargs)

        self._frames_per_cmaf_chunk = None
        self.discriminator = None

        if frames_per_cmaf_chunk is not None:
            self.frames_per_cmaf_chunk = frames_per_cmaf_chunk

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
