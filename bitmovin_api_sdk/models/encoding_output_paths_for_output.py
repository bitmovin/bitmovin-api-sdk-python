# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class EncodingOutputPathsForOutput(object):
    @poscheck_model
    def __init__(self,
                 dash_manifests=None,
                 hls_manifests=None,
                 smooth_manifests=None):
        # type: (list[EncodingOutputPathsDashManifest], list[EncodingOutputPathsHlsManifest], list[EncodingOutputPathsSmoothManifest]) -> None

        self._dash_manifests = list()
        self._hls_manifests = list()
        self._smooth_manifests = list()
        self.discriminator = None

        if dash_manifests is not None:
            self.dash_manifests = dash_manifests
        if hls_manifests is not None:
            self.hls_manifests = hls_manifests
        if smooth_manifests is not None:
            self.smooth_manifests = smooth_manifests

    @property
    def openapi_types(self):
        types = {
            'dash_manifests': 'list[EncodingOutputPathsDashManifest]',
            'hls_manifests': 'list[EncodingOutputPathsHlsManifest]',
            'smooth_manifests': 'list[EncodingOutputPathsSmoothManifest]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'dash_manifests': 'dashManifests',
            'hls_manifests': 'hlsManifests',
            'smooth_manifests': 'smoothManifests'
        }
        return attributes

    @property
    def dash_manifests(self):
        # type: () -> list[EncodingOutputPathsDashManifest]
        """Gets the dash_manifests of this EncodingOutputPathsForOutput.

        Output paths for Dash manifests

        :return: The dash_manifests of this EncodingOutputPathsForOutput.
        :rtype: list[EncodingOutputPathsDashManifest]
        """
        return self._dash_manifests

    @dash_manifests.setter
    def dash_manifests(self, dash_manifests):
        # type: (list) -> None
        """Sets the dash_manifests of this EncodingOutputPathsForOutput.

        Output paths for Dash manifests

        :param dash_manifests: The dash_manifests of this EncodingOutputPathsForOutput.
        :type: list[EncodingOutputPathsDashManifest]
        """

        if dash_manifests is not None:
            if not isinstance(dash_manifests, list):
                raise TypeError("Invalid type for `dash_manifests`, type has to be `list[EncodingOutputPathsDashManifest]`")

        self._dash_manifests = dash_manifests

    @property
    def hls_manifests(self):
        # type: () -> list[EncodingOutputPathsHlsManifest]
        """Gets the hls_manifests of this EncodingOutputPathsForOutput.

        Output paths for HLS manifests

        :return: The hls_manifests of this EncodingOutputPathsForOutput.
        :rtype: list[EncodingOutputPathsHlsManifest]
        """
        return self._hls_manifests

    @hls_manifests.setter
    def hls_manifests(self, hls_manifests):
        # type: (list) -> None
        """Sets the hls_manifests of this EncodingOutputPathsForOutput.

        Output paths for HLS manifests

        :param hls_manifests: The hls_manifests of this EncodingOutputPathsForOutput.
        :type: list[EncodingOutputPathsHlsManifest]
        """

        if hls_manifests is not None:
            if not isinstance(hls_manifests, list):
                raise TypeError("Invalid type for `hls_manifests`, type has to be `list[EncodingOutputPathsHlsManifest]`")

        self._hls_manifests = hls_manifests

    @property
    def smooth_manifests(self):
        # type: () -> list[EncodingOutputPathsSmoothManifest]
        """Gets the smooth_manifests of this EncodingOutputPathsForOutput.

        Output paths for Smooth manifests

        :return: The smooth_manifests of this EncodingOutputPathsForOutput.
        :rtype: list[EncodingOutputPathsSmoothManifest]
        """
        return self._smooth_manifests

    @smooth_manifests.setter
    def smooth_manifests(self, smooth_manifests):
        # type: (list) -> None
        """Sets the smooth_manifests of this EncodingOutputPathsForOutput.

        Output paths for Smooth manifests

        :param smooth_manifests: The smooth_manifests of this EncodingOutputPathsForOutput.
        :type: list[EncodingOutputPathsSmoothManifest]
        """

        if smooth_manifests is not None:
            if not isinstance(smooth_manifests, list):
                raise TypeError("Invalid type for `smooth_manifests`, type has to be `list[EncodingOutputPathsSmoothManifest]`")

        self._smooth_manifests = smooth_manifests

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
        if not isinstance(other, EncodingOutputPathsForOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
