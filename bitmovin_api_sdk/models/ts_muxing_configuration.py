# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.ts_program_clock_reference_configuration import TsProgramClockReferenceConfiguration
from bitmovin_api_sdk.models.ts_program_map_table_configuration import TsProgramMapTableConfiguration
import pprint
import six


class TsMuxingConfiguration(object):
    @poscheck_model
    def __init__(self,
                 program_number=None,
                 pmt=None,
                 pcr=None,
                 video_streams=None,
                 audio_streams=None):
        # type: (int, TsProgramMapTableConfiguration, TsProgramClockReferenceConfiguration, list[TsVideoStreamConfiguration], list[TsAudioStreamConfiguration]) -> None

        self._program_number = None
        self._pmt = None
        self._pcr = None
        self._video_streams = list()
        self._audio_streams = list()
        self.discriminator = None

        if program_number is not None:
            self.program_number = program_number
        if pmt is not None:
            self.pmt = pmt
        if pcr is not None:
            self.pcr = pcr
        if video_streams is not None:
            self.video_streams = video_streams
        if audio_streams is not None:
            self.audio_streams = audio_streams

    @property
    def openapi_types(self):
        types = {
            'program_number': 'int',
            'pmt': 'TsProgramMapTableConfiguration',
            'pcr': 'TsProgramClockReferenceConfiguration',
            'video_streams': 'list[TsVideoStreamConfiguration]',
            'audio_streams': 'list[TsAudioStreamConfiguration]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'program_number': 'programNumber',
            'pmt': 'pmt',
            'pcr': 'pcr',
            'video_streams': 'videoStreams',
            'audio_streams': 'audioStreams'
        }
        return attributes

    @property
    def program_number(self):
        # type: () -> int
        """Gets the program_number of this TsMuxingConfiguration.

        An integer value. Value for program_number field in the MPEG Transport Stream Program Map Table (PMT). The value zero is reserved for the NIT PID entry in the PAT.

        :return: The program_number of this TsMuxingConfiguration.
        :rtype: int
        """
        return self._program_number

    @program_number.setter
    def program_number(self, program_number):
        # type: (int) -> None
        """Sets the program_number of this TsMuxingConfiguration.

        An integer value. Value for program_number field in the MPEG Transport Stream Program Map Table (PMT). The value zero is reserved for the NIT PID entry in the PAT.

        :param program_number: The program_number of this TsMuxingConfiguration.
        :type: int
        """

        if program_number is not None:
            if program_number is not None and program_number > 65535:
                raise ValueError("Invalid value for `program_number`, must be a value less than or equal to `65535`")
            if program_number is not None and program_number < 1:
                raise ValueError("Invalid value for `program_number`, must be a value greater than or equal to `1`")
            if not isinstance(program_number, int):
                raise TypeError("Invalid type for `program_number`, type has to be `int`")

        self._program_number = program_number

    @property
    def pmt(self):
        # type: () -> TsProgramMapTableConfiguration
        """Gets the pmt of this TsMuxingConfiguration.


        :return: The pmt of this TsMuxingConfiguration.
        :rtype: TsProgramMapTableConfiguration
        """
        return self._pmt

    @pmt.setter
    def pmt(self, pmt):
        # type: (TsProgramMapTableConfiguration) -> None
        """Sets the pmt of this TsMuxingConfiguration.


        :param pmt: The pmt of this TsMuxingConfiguration.
        :type: TsProgramMapTableConfiguration
        """

        if pmt is not None:
            if not isinstance(pmt, TsProgramMapTableConfiguration):
                raise TypeError("Invalid type for `pmt`, type has to be `TsProgramMapTableConfiguration`")

        self._pmt = pmt

    @property
    def pcr(self):
        # type: () -> TsProgramClockReferenceConfiguration
        """Gets the pcr of this TsMuxingConfiguration.


        :return: The pcr of this TsMuxingConfiguration.
        :rtype: TsProgramClockReferenceConfiguration
        """
        return self._pcr

    @pcr.setter
    def pcr(self, pcr):
        # type: (TsProgramClockReferenceConfiguration) -> None
        """Sets the pcr of this TsMuxingConfiguration.


        :param pcr: The pcr of this TsMuxingConfiguration.
        :type: TsProgramClockReferenceConfiguration
        """

        if pcr is not None:
            if not isinstance(pcr, TsProgramClockReferenceConfiguration):
                raise TypeError("Invalid type for `pcr`, type has to be `TsProgramClockReferenceConfiguration`")

        self._pcr = pcr

    @property
    def video_streams(self):
        # type: () -> list[TsVideoStreamConfiguration]
        """Gets the video_streams of this TsMuxingConfiguration.


        :return: The video_streams of this TsMuxingConfiguration.
        :rtype: list[TsVideoStreamConfiguration]
        """
        return self._video_streams

    @video_streams.setter
    def video_streams(self, video_streams):
        # type: (list) -> None
        """Sets the video_streams of this TsMuxingConfiguration.


        :param video_streams: The video_streams of this TsMuxingConfiguration.
        :type: list[TsVideoStreamConfiguration]
        """

        if video_streams is not None:
            if not isinstance(video_streams, list):
                raise TypeError("Invalid type for `video_streams`, type has to be `list[TsVideoStreamConfiguration]`")

        self._video_streams = video_streams

    @property
    def audio_streams(self):
        # type: () -> list[TsAudioStreamConfiguration]
        """Gets the audio_streams of this TsMuxingConfiguration.


        :return: The audio_streams of this TsMuxingConfiguration.
        :rtype: list[TsAudioStreamConfiguration]
        """
        return self._audio_streams

    @audio_streams.setter
    def audio_streams(self, audio_streams):
        # type: (list) -> None
        """Sets the audio_streams of this TsMuxingConfiguration.


        :param audio_streams: The audio_streams of this TsMuxingConfiguration.
        :type: list[TsAudioStreamConfiguration]
        """

        if audio_streams is not None:
            if not isinstance(audio_streams, list):
                raise TypeError("Invalid type for `audio_streams`, type has to be `list[TsAudioStreamConfiguration]`")

        self._audio_streams = audio_streams

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
        if not isinstance(other, TsMuxingConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
