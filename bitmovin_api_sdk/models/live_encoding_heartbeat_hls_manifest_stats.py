# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.live_encoding_heartbeat_manifest_update_latency_stats import LiveEncodingHeartbeatManifestUpdateLatencyStats
import pprint
import six


class LiveEncodingHeartbeatHlsManifestStats(object):
    @poscheck_model
    def __init__(self,
                 manifest_id=None,
                 manifest_update_latency_stats=None,
                 manifest_updates=None):
        # type: (string_types, LiveEncodingHeartbeatManifestUpdateLatencyStats, list[LiveEncodingHeartbeatManifestUpdate]) -> None

        self._manifest_id = None
        self._manifest_update_latency_stats = None
        self._manifest_updates = list()
        self.discriminator = None

        if manifest_id is not None:
            self.manifest_id = manifest_id
        if manifest_update_latency_stats is not None:
            self.manifest_update_latency_stats = manifest_update_latency_stats
        if manifest_updates is not None:
            self.manifest_updates = manifest_updates

    @property
    def openapi_types(self):
        types = {
            'manifest_id': 'string_types',
            'manifest_update_latency_stats': 'LiveEncodingHeartbeatManifestUpdateLatencyStats',
            'manifest_updates': 'list[LiveEncodingHeartbeatManifestUpdate]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'manifest_id': 'manifestId',
            'manifest_update_latency_stats': 'manifestUpdateLatencyStats',
            'manifest_updates': 'manifestUpdates'
        }
        return attributes

    @property
    def manifest_id(self):
        # type: () -> string_types
        """Gets the manifest_id of this LiveEncodingHeartbeatHlsManifestStats.

        Id of the HLS manifest these statistics belong to.

        :return: The manifest_id of this LiveEncodingHeartbeatHlsManifestStats.
        :rtype: string_types
        """
        return self._manifest_id

    @manifest_id.setter
    def manifest_id(self, manifest_id):
        # type: (string_types) -> None
        """Sets the manifest_id of this LiveEncodingHeartbeatHlsManifestStats.

        Id of the HLS manifest these statistics belong to.

        :param manifest_id: The manifest_id of this LiveEncodingHeartbeatHlsManifestStats.
        :type: string_types
        """

        if manifest_id is not None:
            if not isinstance(manifest_id, string_types):
                raise TypeError("Invalid type for `manifest_id`, type has to be `string_types`")

        self._manifest_id = manifest_id

    @property
    def manifest_update_latency_stats(self):
        # type: () -> LiveEncodingHeartbeatManifestUpdateLatencyStats
        """Gets the manifest_update_latency_stats of this LiveEncodingHeartbeatHlsManifestStats.

        Aggregate latency statistics over recorded manifest updates.

        :return: The manifest_update_latency_stats of this LiveEncodingHeartbeatHlsManifestStats.
        :rtype: LiveEncodingHeartbeatManifestUpdateLatencyStats
        """
        return self._manifest_update_latency_stats

    @manifest_update_latency_stats.setter
    def manifest_update_latency_stats(self, manifest_update_latency_stats):
        # type: (LiveEncodingHeartbeatManifestUpdateLatencyStats) -> None
        """Sets the manifest_update_latency_stats of this LiveEncodingHeartbeatHlsManifestStats.

        Aggregate latency statistics over recorded manifest updates.

        :param manifest_update_latency_stats: The manifest_update_latency_stats of this LiveEncodingHeartbeatHlsManifestStats.
        :type: LiveEncodingHeartbeatManifestUpdateLatencyStats
        """

        if manifest_update_latency_stats is not None:
            if not isinstance(manifest_update_latency_stats, LiveEncodingHeartbeatManifestUpdateLatencyStats):
                raise TypeError("Invalid type for `manifest_update_latency_stats`, type has to be `LiveEncodingHeartbeatManifestUpdateLatencyStats`")

        self._manifest_update_latency_stats = manifest_update_latency_stats

    @property
    def manifest_updates(self):
        # type: () -> list[LiveEncodingHeartbeatManifestUpdate]
        """Gets the manifest_updates of this LiveEncodingHeartbeatHlsManifestStats.

        Per-manifest outlier-only (high-latency) manifest updates, ordered newest to oldest.

        :return: The manifest_updates of this LiveEncodingHeartbeatHlsManifestStats.
        :rtype: list[LiveEncodingHeartbeatManifestUpdate]
        """
        return self._manifest_updates

    @manifest_updates.setter
    def manifest_updates(self, manifest_updates):
        # type: (list) -> None
        """Sets the manifest_updates of this LiveEncodingHeartbeatHlsManifestStats.

        Per-manifest outlier-only (high-latency) manifest updates, ordered newest to oldest.

        :param manifest_updates: The manifest_updates of this LiveEncodingHeartbeatHlsManifestStats.
        :type: list[LiveEncodingHeartbeatManifestUpdate]
        """

        if manifest_updates is not None:
            if not isinstance(manifest_updates, list):
                raise TypeError("Invalid type for `manifest_updates`, type has to be `list[LiveEncodingHeartbeatManifestUpdate]`")

        self._manifest_updates = manifest_updates

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
        if not isinstance(other, LiveEncodingHeartbeatHlsManifestStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
