# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.progressive_muxing_information import ProgressiveMuxingInformation
import pprint
import six


class ProgressiveTsMuxingInformation(ProgressiveMuxingInformation):
    @poscheck_model
    def __init__(self,
                 mime_type=None,
                 file_size=None,
                 container_format=None,
                 container_bitrate=None,
                 duration=None,
                 video_tracks=None,
                 audio_tracks=None,
                 byte_ranges=None):
        # type: (string_types, int, string_types, int, float, list[MuxingInformationVideoTrack], list[MuxingInformationAudioTrack], list[ProgressiveTsMuxingInformationByteRanges]) -> None
        super(ProgressiveTsMuxingInformation, self).__init__(mime_type=mime_type, file_size=file_size, container_format=container_format, container_bitrate=container_bitrate, duration=duration, video_tracks=video_tracks, audio_tracks=audio_tracks)

        self._byte_ranges = list()
        self.discriminator = None

        if byte_ranges is not None:
            self.byte_ranges = byte_ranges

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(ProgressiveTsMuxingInformation, self), 'openapi_types'):
            types = getattr(super(ProgressiveTsMuxingInformation, self), 'openapi_types')

        types.update({
            'byte_ranges': 'list[ProgressiveTsMuxingInformationByteRanges]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(ProgressiveTsMuxingInformation, self), 'attribute_map'):
            attributes = getattr(super(ProgressiveTsMuxingInformation, self), 'attribute_map')

        attributes.update({
            'byte_ranges': 'byteRanges'
        })
        return attributes

    @property
    def byte_ranges(self):
        # type: () -> list[ProgressiveTsMuxingInformationByteRanges]
        """Gets the byte_ranges of this ProgressiveTsMuxingInformation.

        Byte ranges for the segments within the TS file

        :return: The byte_ranges of this ProgressiveTsMuxingInformation.
        :rtype: list[ProgressiveTsMuxingInformationByteRanges]
        """
        return self._byte_ranges

    @byte_ranges.setter
    def byte_ranges(self, byte_ranges):
        # type: (list) -> None
        """Sets the byte_ranges of this ProgressiveTsMuxingInformation.

        Byte ranges for the segments within the TS file

        :param byte_ranges: The byte_ranges of this ProgressiveTsMuxingInformation.
        :type: list[ProgressiveTsMuxingInformationByteRanges]
        """

        if byte_ranges is not None:
            if not isinstance(byte_ranges, list):
                raise TypeError("Invalid type for `byte_ranges`, type has to be `list[ProgressiveTsMuxingInformationByteRanges]`")

        self._byte_ranges = byte_ranges

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(ProgressiveTsMuxingInformation, self), "to_dict"):
            result = super(ProgressiveTsMuxingInformation, self).to_dict()
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
        if not isinstance(other, ProgressiveTsMuxingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
