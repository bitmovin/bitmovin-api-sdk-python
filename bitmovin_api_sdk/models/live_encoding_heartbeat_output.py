# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.live_encoding_heartbeat_manifests import LiveEncodingHeartbeatManifests
from bitmovin_api_sdk.models.live_encoding_heartbeat_segments import LiveEncodingHeartbeatSegments
import pprint
import six


class LiveEncodingHeartbeatOutput(object):
    @poscheck_model
    def __init__(self,
                 manifests=None,
                 segments=None):
        # type: (LiveEncodingHeartbeatManifests, LiveEncodingHeartbeatSegments) -> None

        self._manifests = None
        self._segments = None
        self.discriminator = None

        if manifests is not None:
            self.manifests = manifests
        if segments is not None:
            self.segments = segments

    @property
    def openapi_types(self):
        types = {
            'manifests': 'LiveEncodingHeartbeatManifests',
            'segments': 'LiveEncodingHeartbeatSegments'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'manifests': 'manifests',
            'segments': 'segments'
        }
        return attributes

    @property
    def manifests(self):
        # type: () -> LiveEncodingHeartbeatManifests
        """Gets the manifests of this LiveEncodingHeartbeatOutput.

        Manifest statistics for the live encoding output.

        :return: The manifests of this LiveEncodingHeartbeatOutput.
        :rtype: LiveEncodingHeartbeatManifests
        """
        return self._manifests

    @manifests.setter
    def manifests(self, manifests):
        # type: (LiveEncodingHeartbeatManifests) -> None
        """Sets the manifests of this LiveEncodingHeartbeatOutput.

        Manifest statistics for the live encoding output.

        :param manifests: The manifests of this LiveEncodingHeartbeatOutput.
        :type: LiveEncodingHeartbeatManifests
        """

        if manifests is not None:
            if not isinstance(manifests, LiveEncodingHeartbeatManifests):
                raise TypeError("Invalid type for `manifests`, type has to be `LiveEncodingHeartbeatManifests`")

        self._manifests = manifests

    @property
    def segments(self):
        # type: () -> LiveEncodingHeartbeatSegments
        """Gets the segments of this LiveEncodingHeartbeatOutput.

        Segment processing statistics for the live encoding output.

        :return: The segments of this LiveEncodingHeartbeatOutput.
        :rtype: LiveEncodingHeartbeatSegments
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        # type: (LiveEncodingHeartbeatSegments) -> None
        """Sets the segments of this LiveEncodingHeartbeatOutput.

        Segment processing statistics for the live encoding output.

        :param segments: The segments of this LiveEncodingHeartbeatOutput.
        :type: LiveEncodingHeartbeatSegments
        """

        if segments is not None:
            if not isinstance(segments, LiveEncodingHeartbeatSegments):
                raise TypeError("Invalid type for `segments`, type has to be `LiveEncodingHeartbeatSegments`")

        self._segments = segments

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
        if not isinstance(other, LiveEncodingHeartbeatOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
