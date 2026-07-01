# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class LiveEncodingHeartbeatManifestUpdate(object):
    @poscheck_model
    def __init__(self,
                 manifest_update_wall_clock_time=None,
                 latest_media_presentation_time=None,
                 manifest_update_latency=None):
        # type: (datetime, datetime, int) -> None

        self._manifest_update_wall_clock_time = None
        self._latest_media_presentation_time = None
        self._manifest_update_latency = None
        self.discriminator = None

        if manifest_update_wall_clock_time is not None:
            self.manifest_update_wall_clock_time = manifest_update_wall_clock_time
        if latest_media_presentation_time is not None:
            self.latest_media_presentation_time = latest_media_presentation_time
        if manifest_update_latency is not None:
            self.manifest_update_latency = manifest_update_latency

    @property
    def openapi_types(self):
        types = {
            'manifest_update_wall_clock_time': 'datetime',
            'latest_media_presentation_time': 'datetime',
            'manifest_update_latency': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'manifest_update_wall_clock_time': 'manifestUpdateWallClockTime',
            'latest_media_presentation_time': 'latestMediaPresentationTime',
            'manifest_update_latency': 'manifestUpdateLatency'
        }
        return attributes

    @property
    def manifest_update_wall_clock_time(self):
        # type: () -> datetime
        """Gets the manifest_update_wall_clock_time of this LiveEncodingHeartbeatManifestUpdate.

        Wall-clock time the media-advancing manifest update occured, returned as UTC in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The manifest_update_wall_clock_time of this LiveEncodingHeartbeatManifestUpdate.
        :rtype: datetime
        """
        return self._manifest_update_wall_clock_time

    @manifest_update_wall_clock_time.setter
    def manifest_update_wall_clock_time(self, manifest_update_wall_clock_time):
        # type: (datetime) -> None
        """Sets the manifest_update_wall_clock_time of this LiveEncodingHeartbeatManifestUpdate.

        Wall-clock time the media-advancing manifest update occured, returned as UTC in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param manifest_update_wall_clock_time: The manifest_update_wall_clock_time of this LiveEncodingHeartbeatManifestUpdate.
        :type: datetime
        """

        if manifest_update_wall_clock_time is not None:
            if not isinstance(manifest_update_wall_clock_time, datetime):
                raise TypeError("Invalid type for `manifest_update_wall_clock_time`, type has to be `datetime`")

        self._manifest_update_wall_clock_time = manifest_update_wall_clock_time

    @property
    def latest_media_presentation_time(self):
        # type: () -> datetime
        """Gets the latest_media_presentation_time of this LiveEncodingHeartbeatManifestUpdate.

        Latest media presentation time across renditions (min of all playlists' stream progress), returned as UTC in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The latest_media_presentation_time of this LiveEncodingHeartbeatManifestUpdate.
        :rtype: datetime
        """
        return self._latest_media_presentation_time

    @latest_media_presentation_time.setter
    def latest_media_presentation_time(self, latest_media_presentation_time):
        # type: (datetime) -> None
        """Sets the latest_media_presentation_time of this LiveEncodingHeartbeatManifestUpdate.

        Latest media presentation time across renditions (min of all playlists' stream progress), returned as UTC in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param latest_media_presentation_time: The latest_media_presentation_time of this LiveEncodingHeartbeatManifestUpdate.
        :type: datetime
        """

        if latest_media_presentation_time is not None:
            if not isinstance(latest_media_presentation_time, datetime):
                raise TypeError("Invalid type for `latest_media_presentation_time`, type has to be `datetime`")

        self._latest_media_presentation_time = latest_media_presentation_time

    @property
    def manifest_update_latency(self):
        # type: () -> int
        """Gets the manifest_update_latency of this LiveEncodingHeartbeatManifestUpdate.

        Manifest update latency in milliseconds (elapsed wall-clock minus media-time advanced).

        :return: The manifest_update_latency of this LiveEncodingHeartbeatManifestUpdate.
        :rtype: int
        """
        return self._manifest_update_latency

    @manifest_update_latency.setter
    def manifest_update_latency(self, manifest_update_latency):
        # type: (int) -> None
        """Sets the manifest_update_latency of this LiveEncodingHeartbeatManifestUpdate.

        Manifest update latency in milliseconds (elapsed wall-clock minus media-time advanced).

        :param manifest_update_latency: The manifest_update_latency of this LiveEncodingHeartbeatManifestUpdate.
        :type: int
        """

        if manifest_update_latency is not None:
            if not isinstance(manifest_update_latency, int):
                raise TypeError("Invalid type for `manifest_update_latency`, type has to be `int`")

        self._manifest_update_latency = manifest_update_latency

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
        if not isinstance(other, LiveEncodingHeartbeatManifestUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
