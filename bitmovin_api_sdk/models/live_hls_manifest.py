# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.hls_manifest_ad_marker_settings import HlsManifestAdMarkerSettings
from bitmovin_api_sdk.models.program_date_time_settings import ProgramDateTimeSettings
import pprint
import six


class LiveHlsManifest(object):
    @poscheck_model
    def __init__(self,
                 manifest_id=None,
                 timeshift=None,
                 live_edge_offset=None,
                 insert_program_date_time=None,
                 program_date_time_settings=None,
                 ad_marker_settings=None):
        # type: (string_types, float, float, bool, ProgramDateTimeSettings, HlsManifestAdMarkerSettings) -> None

        self._manifest_id = None
        self._timeshift = None
        self._live_edge_offset = None
        self._insert_program_date_time = None
        self._program_date_time_settings = None
        self._ad_marker_settings = None
        self.discriminator = None

        if manifest_id is not None:
            self.manifest_id = manifest_id
        if timeshift is not None:
            self.timeshift = timeshift
        if live_edge_offset is not None:
            self.live_edge_offset = live_edge_offset
        if insert_program_date_time is not None:
            self.insert_program_date_time = insert_program_date_time
        if program_date_time_settings is not None:
            self.program_date_time_settings = program_date_time_settings
        if ad_marker_settings is not None:
            self.ad_marker_settings = ad_marker_settings

    @property
    def openapi_types(self):
        types = {
            'manifest_id': 'string_types',
            'timeshift': 'float',
            'live_edge_offset': 'float',
            'insert_program_date_time': 'bool',
            'program_date_time_settings': 'ProgramDateTimeSettings',
            'ad_marker_settings': 'HlsManifestAdMarkerSettings'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'manifest_id': 'manifestId',
            'timeshift': 'timeshift',
            'live_edge_offset': 'liveEdgeOffset',
            'insert_program_date_time': 'insertProgramDateTime',
            'program_date_time_settings': 'programDateTimeSettings',
            'ad_marker_settings': 'adMarkerSettings'
        }
        return attributes

    @property
    def manifest_id(self):
        # type: () -> string_types
        """Gets the manifest_id of this LiveHlsManifest.

        HLS manifest id (required)

        :return: The manifest_id of this LiveHlsManifest.
        :rtype: string_types
        """
        return self._manifest_id

    @manifest_id.setter
    def manifest_id(self, manifest_id):
        # type: (string_types) -> None
        """Sets the manifest_id of this LiveHlsManifest.

        HLS manifest id (required)

        :param manifest_id: The manifest_id of this LiveHlsManifest.
        :type: string_types
        """

        if manifest_id is not None:
            if not isinstance(manifest_id, string_types):
                raise TypeError("Invalid type for `manifest_id`, type has to be `string_types`")

        self._manifest_id = manifest_id

    @property
    def timeshift(self):
        # type: () -> float
        """Gets the timeshift of this LiveHlsManifest.

        Timeshift in seconds. We recommend to use a timeshift value not greater than 3 hours (10800.0 seconds). Longer values could negatively impact the manifest update frequency. 

        :return: The timeshift of this LiveHlsManifest.
        :rtype: float
        """
        return self._timeshift

    @timeshift.setter
    def timeshift(self, timeshift):
        # type: (float) -> None
        """Sets the timeshift of this LiveHlsManifest.

        Timeshift in seconds. We recommend to use a timeshift value not greater than 3 hours (10800.0 seconds). Longer values could negatively impact the manifest update frequency. 

        :param timeshift: The timeshift of this LiveHlsManifest.
        :type: float
        """

        if timeshift is not None:
            if not isinstance(timeshift, (float, int)):
                raise TypeError("Invalid type for `timeshift`, type has to be `float`")

        self._timeshift = timeshift

    @property
    def live_edge_offset(self):
        # type: () -> float
        """Gets the live_edge_offset of this LiveHlsManifest.

        Live edge offset in seconds

        :return: The live_edge_offset of this LiveHlsManifest.
        :rtype: float
        """
        return self._live_edge_offset

    @live_edge_offset.setter
    def live_edge_offset(self, live_edge_offset):
        # type: (float) -> None
        """Sets the live_edge_offset of this LiveHlsManifest.

        Live edge offset in seconds

        :param live_edge_offset: The live_edge_offset of this LiveHlsManifest.
        :type: float
        """

        if live_edge_offset is not None:
            if not isinstance(live_edge_offset, (float, int)):
                raise TypeError("Invalid type for `live_edge_offset`, type has to be `float`")

        self._live_edge_offset = live_edge_offset

    @property
    def insert_program_date_time(self):
        # type: () -> bool
        """Gets the insert_program_date_time of this LiveHlsManifest.

        Specifies if the EXT-X-PROGRAM-DATETIME tag will be included

        :return: The insert_program_date_time of this LiveHlsManifest.
        :rtype: bool
        """
        return self._insert_program_date_time

    @insert_program_date_time.setter
    def insert_program_date_time(self, insert_program_date_time):
        # type: (bool) -> None
        """Sets the insert_program_date_time of this LiveHlsManifest.

        Specifies if the EXT-X-PROGRAM-DATETIME tag will be included

        :param insert_program_date_time: The insert_program_date_time of this LiveHlsManifest.
        :type: bool
        """

        if insert_program_date_time is not None:
            if not isinstance(insert_program_date_time, bool):
                raise TypeError("Invalid type for `insert_program_date_time`, type has to be `bool`")

        self._insert_program_date_time = insert_program_date_time

    @property
    def program_date_time_settings(self):
        # type: () -> ProgramDateTimeSettings
        """Gets the program_date_time_settings of this LiveHlsManifest.

        Configuration for the EXT-X-PROGRAM-DATETIME tag

        :return: The program_date_time_settings of this LiveHlsManifest.
        :rtype: ProgramDateTimeSettings
        """
        return self._program_date_time_settings

    @program_date_time_settings.setter
    def program_date_time_settings(self, program_date_time_settings):
        # type: (ProgramDateTimeSettings) -> None
        """Sets the program_date_time_settings of this LiveHlsManifest.

        Configuration for the EXT-X-PROGRAM-DATETIME tag

        :param program_date_time_settings: The program_date_time_settings of this LiveHlsManifest.
        :type: ProgramDateTimeSettings
        """

        if program_date_time_settings is not None:
            if not isinstance(program_date_time_settings, ProgramDateTimeSettings):
                raise TypeError("Invalid type for `program_date_time_settings`, type has to be `ProgramDateTimeSettings`")

        self._program_date_time_settings = program_date_time_settings

    @property
    def ad_marker_settings(self):
        # type: () -> HlsManifestAdMarkerSettings
        """Gets the ad_marker_settings of this LiveHlsManifest.

        Configuration for tags related to ad markers (e.g. Scte35)

        :return: The ad_marker_settings of this LiveHlsManifest.
        :rtype: HlsManifestAdMarkerSettings
        """
        return self._ad_marker_settings

    @ad_marker_settings.setter
    def ad_marker_settings(self, ad_marker_settings):
        # type: (HlsManifestAdMarkerSettings) -> None
        """Sets the ad_marker_settings of this LiveHlsManifest.

        Configuration for tags related to ad markers (e.g. Scte35)

        :param ad_marker_settings: The ad_marker_settings of this LiveHlsManifest.
        :type: HlsManifestAdMarkerSettings
        """

        if ad_marker_settings is not None:
            if not isinstance(ad_marker_settings, HlsManifestAdMarkerSettings):
                raise TypeError("Invalid type for `ad_marker_settings`, type has to be `HlsManifestAdMarkerSettings`")

        self._ad_marker_settings = ad_marker_settings

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
        if not isinstance(other, LiveHlsManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
