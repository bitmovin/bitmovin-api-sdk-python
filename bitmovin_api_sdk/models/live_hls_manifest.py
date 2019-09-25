# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class LiveHlsManifest(object):
    @poscheck_model
    def __init__(self,
                 manifest_id=None,
                 timeshift=None,
                 live_edge_offset=None,
                 insert_program_date_time=None):
        # type: (string_types, float, float, bool) -> None

        self._manifest_id = None
        self._timeshift = None
        self._live_edge_offset = None
        self._insert_program_date_time = None
        self.discriminator = None

        if manifest_id is not None:
            self.manifest_id = manifest_id
        if timeshift is not None:
            self.timeshift = timeshift
        if live_edge_offset is not None:
            self.live_edge_offset = live_edge_offset
        if insert_program_date_time is not None:
            self.insert_program_date_time = insert_program_date_time

    @property
    def openapi_types(self):
        types = {
            'manifest_id': 'string_types',
            'timeshift': 'float',
            'live_edge_offset': 'float',
            'insert_program_date_time': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'manifest_id': 'manifestId',
            'timeshift': 'timeshift',
            'live_edge_offset': 'liveEdgeOffset',
            'insert_program_date_time': 'insertProgramDateTime'
        }
        return attributes

    @property
    def manifest_id(self):
        # type: () -> string_types
        """Gets the manifest_id of this LiveHlsManifest.

        HLS manifest ids (required)

        :return: The manifest_id of this LiveHlsManifest.
        :rtype: string_types
        """
        return self._manifest_id

    @manifest_id.setter
    def manifest_id(self, manifest_id):
        # type: (string_types) -> None
        """Sets the manifest_id of this LiveHlsManifest.

        HLS manifest ids (required)

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

        Timeshift in seconds

        :return: The timeshift of this LiveHlsManifest.
        :rtype: float
        """
        return self._timeshift

    @timeshift.setter
    def timeshift(self, timeshift):
        # type: (float) -> None
        """Sets the timeshift of this LiveHlsManifest.

        Timeshift in seconds

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
