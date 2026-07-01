# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class LiveEncodingHeartbeatManifests(object):
    @poscheck_model
    def __init__(self,
                 hls=None):
        # type: (list[LiveEncodingHeartbeatHlsManifestStats]) -> None

        self._hls = list()
        self.discriminator = None

        if hls is not None:
            self.hls = hls

    @property
    def openapi_types(self):
        types = {
            'hls': 'list[LiveEncodingHeartbeatHlsManifestStats]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'hls': 'hls'
        }
        return attributes

    @property
    def hls(self):
        # type: () -> list[LiveEncodingHeartbeatHlsManifestStats]
        """Gets the hls of this LiveEncodingHeartbeatManifests.

        Per-manifest HLS update statistics; one entry per HLS manifest.

        :return: The hls of this LiveEncodingHeartbeatManifests.
        :rtype: list[LiveEncodingHeartbeatHlsManifestStats]
        """
        return self._hls

    @hls.setter
    def hls(self, hls):
        # type: (list) -> None
        """Sets the hls of this LiveEncodingHeartbeatManifests.

        Per-manifest HLS update statistics; one entry per HLS manifest.

        :param hls: The hls of this LiveEncodingHeartbeatManifests.
        :type: list[LiveEncodingHeartbeatHlsManifestStats]
        """

        if hls is not None:
            if not isinstance(hls, list):
                raise TypeError("Invalid type for `hls`, type has to be `list[LiveEncodingHeartbeatHlsManifestStats]`")

        self._hls = hls

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
        if not isinstance(other, LiveEncodingHeartbeatManifests):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
