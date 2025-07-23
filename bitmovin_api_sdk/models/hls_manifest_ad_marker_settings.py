# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class HlsManifestAdMarkerSettings(object):
    @poscheck_model
    def __init__(self,
                 enabled_marker_types=None,
                 disable_preannouncing=None):
        # type: (list[HlsManifestAdMarkerType], bool) -> None

        self._enabled_marker_types = list()
        self._disable_preannouncing = None
        self.discriminator = None

        if enabled_marker_types is not None:
            self.enabled_marker_types = enabled_marker_types
        if disable_preannouncing is not None:
            self.disable_preannouncing = disable_preannouncing

    @property
    def openapi_types(self):
        types = {
            'enabled_marker_types': 'list[HlsManifestAdMarkerType]',
            'disable_preannouncing': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'enabled_marker_types': 'enabledMarkerTypes',
            'disable_preannouncing': 'disablePreannouncing'
        }
        return attributes

    @property
    def enabled_marker_types(self):
        # type: () -> list[HlsManifestAdMarkerType]
        """Gets the enabled_marker_types of this HlsManifestAdMarkerSettings.

        Ad marker types that will be inserted. More than one type is possible.  - EXT_X_CUE_OUT_IN: Ad markers will be inserted using `#EXT-X-CUE-OUT` and `#EXT-X-CUE-IN` tags - EXT_OATCLS_SCTE35: Ad markers will be inserted using `#EXT-OATCLS-SCTE35` tags. They contain the base64 encoded raw bytes of the original SCTE-35 trigger. - EXT_X_SPLICEPOINT_SCTE35: Ad markers will be inserted using `#EXT-X-SPLICEPOINT-SCTE35` tags. They contain the base64 encoded raw bytes of the original SCTE-35 trigger. - EXT_X_DATERANGE: Ad markers will be inserted using `#EXT-X-DATERANGE` tags. They contain the ID, start timestamp and hex encoded raw bytes of the original SCTE-35 trigger. - EXT_X_SCTE35: Ad markers will be inserted using `#EXT-X-SCTE35` tags. They contain the base64 encoded raw bytes of the original SCTE-35 trigger. 

        :return: The enabled_marker_types of this HlsManifestAdMarkerSettings.
        :rtype: list[HlsManifestAdMarkerType]
        """
        return self._enabled_marker_types

    @enabled_marker_types.setter
    def enabled_marker_types(self, enabled_marker_types):
        # type: (list) -> None
        """Sets the enabled_marker_types of this HlsManifestAdMarkerSettings.

        Ad marker types that will be inserted. More than one type is possible.  - EXT_X_CUE_OUT_IN: Ad markers will be inserted using `#EXT-X-CUE-OUT` and `#EXT-X-CUE-IN` tags - EXT_OATCLS_SCTE35: Ad markers will be inserted using `#EXT-OATCLS-SCTE35` tags. They contain the base64 encoded raw bytes of the original SCTE-35 trigger. - EXT_X_SPLICEPOINT_SCTE35: Ad markers will be inserted using `#EXT-X-SPLICEPOINT-SCTE35` tags. They contain the base64 encoded raw bytes of the original SCTE-35 trigger. - EXT_X_DATERANGE: Ad markers will be inserted using `#EXT-X-DATERANGE` tags. They contain the ID, start timestamp and hex encoded raw bytes of the original SCTE-35 trigger. - EXT_X_SCTE35: Ad markers will be inserted using `#EXT-X-SCTE35` tags. They contain the base64 encoded raw bytes of the original SCTE-35 trigger. 

        :param enabled_marker_types: The enabled_marker_types of this HlsManifestAdMarkerSettings.
        :type: list[HlsManifestAdMarkerType]
        """

        if enabled_marker_types is not None:
            if not isinstance(enabled_marker_types, list):
                raise TypeError("Invalid type for `enabled_marker_types`, type has to be `list[HlsManifestAdMarkerType]`")

        self._enabled_marker_types = enabled_marker_types

    @property
    def disable_preannouncing(self):
        # type: () -> bool
        """Gets the disable_preannouncing of this HlsManifestAdMarkerSettings.

        Certain tags, such as EXT_X_DATERANGE, may be preannounced in the HLS manifest. This means they are inserted as early as possible, before the actual ad break begins or ends. Preannouncing helps clients anticipate upcoming splice points, but may cause compatibility issues with some downstream consumers (e.g., AWS MediaTailor SSAI). When this setting is enabled, preannouncing of tags is disabled, and tags are inserted at the segment corresponding to the event's splice time. 

        :return: The disable_preannouncing of this HlsManifestAdMarkerSettings.
        :rtype: bool
        """
        return self._disable_preannouncing

    @disable_preannouncing.setter
    def disable_preannouncing(self, disable_preannouncing):
        # type: (bool) -> None
        """Sets the disable_preannouncing of this HlsManifestAdMarkerSettings.

        Certain tags, such as EXT_X_DATERANGE, may be preannounced in the HLS manifest. This means they are inserted as early as possible, before the actual ad break begins or ends. Preannouncing helps clients anticipate upcoming splice points, but may cause compatibility issues with some downstream consumers (e.g., AWS MediaTailor SSAI). When this setting is enabled, preannouncing of tags is disabled, and tags are inserted at the segment corresponding to the event's splice time. 

        :param disable_preannouncing: The disable_preannouncing of this HlsManifestAdMarkerSettings.
        :type: bool
        """

        if disable_preannouncing is not None:
            if not isinstance(disable_preannouncing, bool):
                raise TypeError("Invalid type for `disable_preannouncing`, type has to be `bool`")

        self._disable_preannouncing = disable_preannouncing

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
        if not isinstance(other, HlsManifestAdMarkerSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
