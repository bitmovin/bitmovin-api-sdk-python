# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dolby_vision_muxing_configuration import DolbyVisionMuxingConfiguration
from bitmovin_api_sdk.models.fragmented_mp4_muxing_manifest_type import FragmentedMp4MuxingManifestType
from bitmovin_api_sdk.models.muxing import Muxing
from bitmovin_api_sdk.models.stream_conditions_mode import StreamConditionsMode
from bitmovin_api_sdk.models.time_code import TimeCode
import pprint
import six


class Mp4Muxing(Muxing):
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
                 filename=None,
                 fragment_duration=None,
                 time_code=None,
                 fragmented_mp4_muxing_manifest_type=None,
                 dolby_vision_configuration=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[MuxingStream], list[EncodingOutput], int, int, int, list[Ignoring], StreamConditionsMode, string_types, int, TimeCode, FragmentedMp4MuxingManifestType, DolbyVisionMuxingConfiguration) -> None
        super(Mp4Muxing, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, streams=streams, outputs=outputs, avg_bitrate=avg_bitrate, min_bitrate=min_bitrate, max_bitrate=max_bitrate, ignored_by=ignored_by, stream_conditions_mode=stream_conditions_mode)

        self._filename = None
        self._fragment_duration = None
        self._time_code = None
        self._fragmented_mp4_muxing_manifest_type = None
        self._dolby_vision_configuration = None
        self.discriminator = None

        if filename is not None:
            self.filename = filename
        if fragment_duration is not None:
            self.fragment_duration = fragment_duration
        if time_code is not None:
            self.time_code = time_code
        if fragmented_mp4_muxing_manifest_type is not None:
            self.fragmented_mp4_muxing_manifest_type = fragmented_mp4_muxing_manifest_type
        if dolby_vision_configuration is not None:
            self.dolby_vision_configuration = dolby_vision_configuration

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Mp4Muxing, self), 'openapi_types'):
            types = getattr(super(Mp4Muxing, self), 'openapi_types')

        types.update({
            'filename': 'string_types',
            'fragment_duration': 'int',
            'time_code': 'TimeCode',
            'fragmented_mp4_muxing_manifest_type': 'FragmentedMp4MuxingManifestType',
            'dolby_vision_configuration': 'DolbyVisionMuxingConfiguration'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Mp4Muxing, self), 'attribute_map'):
            attributes = getattr(super(Mp4Muxing, self), 'attribute_map')

        attributes.update({
            'filename': 'filename',
            'fragment_duration': 'fragmentDuration',
            'time_code': 'timeCode',
            'fragmented_mp4_muxing_manifest_type': 'fragmentedMP4MuxingManifestType',
            'dolby_vision_configuration': 'dolbyVisionConfiguration'
        })
        return attributes

    @property
    def filename(self):
        # type: () -> string_types
        """Gets the filename of this Mp4Muxing.

        Name of the output file (either `filename` or `name` is required, prefer `filename`)

        :return: The filename of this Mp4Muxing.
        :rtype: string_types
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        # type: (string_types) -> None
        """Sets the filename of this Mp4Muxing.

        Name of the output file (either `filename` or `name` is required, prefer `filename`)

        :param filename: The filename of this Mp4Muxing.
        :type: string_types
        """

        if filename is not None:
            if not isinstance(filename, string_types):
                raise TypeError("Invalid type for `filename`, type has to be `string_types`")

        self._filename = filename

    @property
    def fragment_duration(self):
        # type: () -> int
        """Gets the fragment_duration of this Mp4Muxing.

         Duration of fragments in milliseconds. Required for Fragmented MP4 Muxing (for Smooth Streaming or DASH On-Demand). Not setting this will result in unfragmented mp4.

        :return: The fragment_duration of this Mp4Muxing.
        :rtype: int
        """
        return self._fragment_duration

    @fragment_duration.setter
    def fragment_duration(self, fragment_duration):
        # type: (int) -> None
        """Sets the fragment_duration of this Mp4Muxing.

         Duration of fragments in milliseconds. Required for Fragmented MP4 Muxing (for Smooth Streaming or DASH On-Demand). Not setting this will result in unfragmented mp4.

        :param fragment_duration: The fragment_duration of this Mp4Muxing.
        :type: int
        """

        if fragment_duration is not None:
            if not isinstance(fragment_duration, int):
                raise TypeError("Invalid type for `fragment_duration`, type has to be `int`")

        self._fragment_duration = fragment_duration

    @property
    def time_code(self):
        # type: () -> TimeCode
        """Gets the time_code of this Mp4Muxing.


        :return: The time_code of this Mp4Muxing.
        :rtype: TimeCode
        """
        return self._time_code

    @time_code.setter
    def time_code(self, time_code):
        # type: (TimeCode) -> None
        """Sets the time_code of this Mp4Muxing.


        :param time_code: The time_code of this Mp4Muxing.
        :type: TimeCode
        """

        if time_code is not None:
            if not isinstance(time_code, TimeCode):
                raise TypeError("Invalid type for `time_code`, type has to be `TimeCode`")

        self._time_code = time_code

    @property
    def fragmented_mp4_muxing_manifest_type(self):
        # type: () -> FragmentedMp4MuxingManifestType
        """Gets the fragmented_mp4_muxing_manifest_type of this Mp4Muxing.


        :return: The fragmented_mp4_muxing_manifest_type of this Mp4Muxing.
        :rtype: FragmentedMp4MuxingManifestType
        """
        return self._fragmented_mp4_muxing_manifest_type

    @fragmented_mp4_muxing_manifest_type.setter
    def fragmented_mp4_muxing_manifest_type(self, fragmented_mp4_muxing_manifest_type):
        # type: (FragmentedMp4MuxingManifestType) -> None
        """Sets the fragmented_mp4_muxing_manifest_type of this Mp4Muxing.


        :param fragmented_mp4_muxing_manifest_type: The fragmented_mp4_muxing_manifest_type of this Mp4Muxing.
        :type: FragmentedMp4MuxingManifestType
        """

        if fragmented_mp4_muxing_manifest_type is not None:
            if not isinstance(fragmented_mp4_muxing_manifest_type, FragmentedMp4MuxingManifestType):
                raise TypeError("Invalid type for `fragmented_mp4_muxing_manifest_type`, type has to be `FragmentedMp4MuxingManifestType`")

        self._fragmented_mp4_muxing_manifest_type = fragmented_mp4_muxing_manifest_type

    @property
    def dolby_vision_configuration(self):
        # type: () -> DolbyVisionMuxingConfiguration
        """Gets the dolby_vision_configuration of this Mp4Muxing.

        Dolby Vision specific configuration

        :return: The dolby_vision_configuration of this Mp4Muxing.
        :rtype: DolbyVisionMuxingConfiguration
        """
        return self._dolby_vision_configuration

    @dolby_vision_configuration.setter
    def dolby_vision_configuration(self, dolby_vision_configuration):
        # type: (DolbyVisionMuxingConfiguration) -> None
        """Sets the dolby_vision_configuration of this Mp4Muxing.

        Dolby Vision specific configuration

        :param dolby_vision_configuration: The dolby_vision_configuration of this Mp4Muxing.
        :type: DolbyVisionMuxingConfiguration
        """

        if dolby_vision_configuration is not None:
            if not isinstance(dolby_vision_configuration, DolbyVisionMuxingConfiguration):
                raise TypeError("Invalid type for `dolby_vision_configuration`, type has to be `DolbyVisionMuxingConfiguration`")

        self._dolby_vision_configuration = dolby_vision_configuration

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Mp4Muxing, self), "to_dict"):
            result = super(Mp4Muxing, self).to_dict()
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
        if not isinstance(other, Mp4Muxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
