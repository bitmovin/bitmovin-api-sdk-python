# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class LiveDashManifest(object):
    @poscheck_model
    def __init__(self,
                 manifest_id=None,
                 timeshift=None,
                 live_edge_offset=None):
        # type: (string_types, float, float) -> None

        self._manifest_id = None
        self._timeshift = None
        self._live_edge_offset = None
        self.discriminator = None

        if manifest_id is not None:
            self.manifest_id = manifest_id
        if timeshift is not None:
            self.timeshift = timeshift
        if live_edge_offset is not None:
            self.live_edge_offset = live_edge_offset

    @property
    def openapi_types(self):
        types = {
            'manifest_id': 'string_types',
            'timeshift': 'float',
            'live_edge_offset': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'manifest_id': 'manifestId',
            'timeshift': 'timeshift',
            'live_edge_offset': 'liveEdgeOffset'
        }
        return attributes

    @property
    def manifest_id(self):
        # type: () -> string_types
        """Gets the manifest_id of this LiveDashManifest.

        Dash manifest ids (required)

        :return: The manifest_id of this LiveDashManifest.
        :rtype: string_types
        """
        return self._manifest_id

    @manifest_id.setter
    def manifest_id(self, manifest_id):
        # type: (string_types) -> None
        """Sets the manifest_id of this LiveDashManifest.

        Dash manifest ids (required)

        :param manifest_id: The manifest_id of this LiveDashManifest.
        :type: string_types
        """

        if manifest_id is not None:
            if not isinstance(manifest_id, string_types):
                raise TypeError("Invalid type for `manifest_id`, type has to be `string_types`")

        self._manifest_id = manifest_id

    @property
    def timeshift(self):
        # type: () -> float
        """Gets the timeshift of this LiveDashManifest.

        Timeshift in seconds

        :return: The timeshift of this LiveDashManifest.
        :rtype: float
        """
        return self._timeshift

    @timeshift.setter
    def timeshift(self, timeshift):
        # type: (float) -> None
        """Sets the timeshift of this LiveDashManifest.

        Timeshift in seconds

        :param timeshift: The timeshift of this LiveDashManifest.
        :type: float
        """

        if timeshift is not None:
            if not isinstance(timeshift, (float, int)):
                raise TypeError("Invalid type for `timeshift`, type has to be `float`")

        self._timeshift = timeshift

    @property
    def live_edge_offset(self):
        # type: () -> float
        """Gets the live_edge_offset of this LiveDashManifest.

        Live edge offset in seconds

        :return: The live_edge_offset of this LiveDashManifest.
        :rtype: float
        """
        return self._live_edge_offset

    @live_edge_offset.setter
    def live_edge_offset(self, live_edge_offset):
        # type: (float) -> None
        """Sets the live_edge_offset of this LiveDashManifest.

        Live edge offset in seconds

        :param live_edge_offset: The live_edge_offset of this LiveDashManifest.
        :type: float
        """

        if live_edge_offset is not None:
            if not isinstance(live_edge_offset, (float, int)):
                raise TypeError("Invalid type for `live_edge_offset`, type has to be `float`")

        self._live_edge_offset = live_edge_offset

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
                result[self.attribute_map.get(attr)] = [x.to_dict() if hasattr(x, "to_dict") else x for x in value]
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
        if not isinstance(other, LiveDashManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
