# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class FragmentedMuxingInformation(object):
    @poscheck_model
    def __init__(self,
                 mime_type=None,
                 file_size=None,
                 container_format=None,
                 container_bitrate=None,
                 duration=None,
                 video_tracks=None,
                 audio_tracks=None):
        # type: (string_types, int, string_types, int, float, list[MuxingInformationVideoTrack], list[MuxingInformationAudioTrack]) -> None

        self._mime_type = None
        self._file_size = None
        self._container_format = None
        self._container_bitrate = None
        self._duration = None
        self._video_tracks = list()
        self._audio_tracks = list()
        self.discriminator = None

        if mime_type is not None:
            self.mime_type = mime_type
        if file_size is not None:
            self.file_size = file_size
        if container_format is not None:
            self.container_format = container_format
        if container_bitrate is not None:
            self.container_bitrate = container_bitrate
        if duration is not None:
            self.duration = duration
        if video_tracks is not None:
            self.video_tracks = video_tracks
        if audio_tracks is not None:
            self.audio_tracks = audio_tracks

    @property
    def openapi_types(self):
        types = {
            'mime_type': 'string_types',
            'file_size': 'int',
            'container_format': 'string_types',
            'container_bitrate': 'int',
            'duration': 'float',
            'video_tracks': 'list[MuxingInformationVideoTrack]',
            'audio_tracks': 'list[MuxingInformationAudioTrack]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'mime_type': 'mimeType',
            'file_size': 'fileSize',
            'container_format': 'containerFormat',
            'container_bitrate': 'containerBitrate',
            'duration': 'duration',
            'video_tracks': 'videoTracks',
            'audio_tracks': 'audioTracks'
        }
        return attributes

    @property
    def mime_type(self):
        # type: () -> string_types
        """Gets the mime_type of this FragmentedMuxingInformation.

        The mime type of the muxing

        :return: The mime_type of this FragmentedMuxingInformation.
        :rtype: string_types
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        # type: (string_types) -> None
        """Sets the mime_type of this FragmentedMuxingInformation.

        The mime type of the muxing

        :param mime_type: The mime_type of this FragmentedMuxingInformation.
        :type: string_types
        """

        if mime_type is not None:
            if not isinstance(mime_type, string_types):
                raise TypeError("Invalid type for `mime_type`, type has to be `string_types`")

        self._mime_type = mime_type

    @property
    def file_size(self):
        # type: () -> int
        """Gets the file_size of this FragmentedMuxingInformation.

        The file size of the muxing in bytes

        :return: The file_size of this FragmentedMuxingInformation.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        # type: (int) -> None
        """Sets the file_size of this FragmentedMuxingInformation.

        The file size of the muxing in bytes

        :param file_size: The file_size of this FragmentedMuxingInformation.
        :type: int
        """

        if file_size is not None:
            if not isinstance(file_size, int):
                raise TypeError("Invalid type for `file_size`, type has to be `int`")

        self._file_size = file_size

    @property
    def container_format(self):
        # type: () -> string_types
        """Gets the container_format of this FragmentedMuxingInformation.

        The container format used

        :return: The container_format of this FragmentedMuxingInformation.
        :rtype: string_types
        """
        return self._container_format

    @container_format.setter
    def container_format(self, container_format):
        # type: (string_types) -> None
        """Sets the container_format of this FragmentedMuxingInformation.

        The container format used

        :param container_format: The container_format of this FragmentedMuxingInformation.
        :type: string_types
        """

        if container_format is not None:
            if not isinstance(container_format, string_types):
                raise TypeError("Invalid type for `container_format`, type has to be `string_types`")

        self._container_format = container_format

    @property
    def container_bitrate(self):
        # type: () -> int
        """Gets the container_bitrate of this FragmentedMuxingInformation.

        The bitrate of the container if available (tracks + container overhead)

        :return: The container_bitrate of this FragmentedMuxingInformation.
        :rtype: int
        """
        return self._container_bitrate

    @container_bitrate.setter
    def container_bitrate(self, container_bitrate):
        # type: (int) -> None
        """Sets the container_bitrate of this FragmentedMuxingInformation.

        The bitrate of the container if available (tracks + container overhead)

        :param container_bitrate: The container_bitrate of this FragmentedMuxingInformation.
        :type: int
        """

        if container_bitrate is not None:
            if not isinstance(container_bitrate, int):
                raise TypeError("Invalid type for `container_bitrate`, type has to be `int`")

        self._container_bitrate = container_bitrate

    @property
    def duration(self):
        # type: () -> float
        """Gets the duration of this FragmentedMuxingInformation.

        The duration of the container in seconds

        :return: The duration of this FragmentedMuxingInformation.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        # type: (float) -> None
        """Sets the duration of this FragmentedMuxingInformation.

        The duration of the container in seconds

        :param duration: The duration of this FragmentedMuxingInformation.
        :type: float
        """

        if duration is not None:
            if not isinstance(duration, (float, int)):
                raise TypeError("Invalid type for `duration`, type has to be `float`")

        self._duration = duration

    @property
    def video_tracks(self):
        # type: () -> list[MuxingInformationVideoTrack]
        """Gets the video_tracks of this FragmentedMuxingInformation.

        Information about the video tracks in the container

        :return: The video_tracks of this FragmentedMuxingInformation.
        :rtype: list[MuxingInformationVideoTrack]
        """
        return self._video_tracks

    @video_tracks.setter
    def video_tracks(self, video_tracks):
        # type: (list) -> None
        """Sets the video_tracks of this FragmentedMuxingInformation.

        Information about the video tracks in the container

        :param video_tracks: The video_tracks of this FragmentedMuxingInformation.
        :type: list[MuxingInformationVideoTrack]
        """

        if video_tracks is not None:
            if not isinstance(video_tracks, list):
                raise TypeError("Invalid type for `video_tracks`, type has to be `list[MuxingInformationVideoTrack]`")

        self._video_tracks = video_tracks

    @property
    def audio_tracks(self):
        # type: () -> list[MuxingInformationAudioTrack]
        """Gets the audio_tracks of this FragmentedMuxingInformation.

        Information about the audio tracks in the container

        :return: The audio_tracks of this FragmentedMuxingInformation.
        :rtype: list[MuxingInformationAudioTrack]
        """
        return self._audio_tracks

    @audio_tracks.setter
    def audio_tracks(self, audio_tracks):
        # type: (list) -> None
        """Sets the audio_tracks of this FragmentedMuxingInformation.

        Information about the audio tracks in the container

        :param audio_tracks: The audio_tracks of this FragmentedMuxingInformation.
        :type: list[MuxingInformationAudioTrack]
        """

        if audio_tracks is not None:
            if not isinstance(audio_tracks, list):
                raise TypeError("Invalid type for `audio_tracks`, type has to be `list[MuxingInformationAudioTrack]`")

        self._audio_tracks = audio_tracks

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
        if not isinstance(other, FragmentedMuxingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
