# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsLicenseErrorDetailsConfig(object):
    @poscheck_model
    def __init__(self,
                 enabled=None,
                 network_explorer_enabled=None):
        # type: (bool, bool) -> None

        self._enabled = None
        self._network_explorer_enabled = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if network_explorer_enabled is not None:
            self.network_explorer_enabled = network_explorer_enabled

    @property
    def openapi_types(self):
        types = {
            'enabled': 'bool',
            'network_explorer_enabled': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'enabled': 'enabled',
            'network_explorer_enabled': 'networkExplorerEnabled'
        }
        return attributes

    @property
    def enabled(self):
        # type: () -> bool
        """Gets the enabled of this AnalyticsLicenseErrorDetailsConfig.

        Are error details enabled on the license

        :return: The enabled of this AnalyticsLicenseErrorDetailsConfig.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        # type: (bool) -> None
        """Sets the enabled of this AnalyticsLicenseErrorDetailsConfig.

        Are error details enabled on the license

        :param enabled: The enabled of this AnalyticsLicenseErrorDetailsConfig.
        :type: bool
        """

        if enabled is not None:
            if not isinstance(enabled, bool):
                raise TypeError("Invalid type for `enabled`, type has to be `bool`")

        self._enabled = enabled

    @property
    def network_explorer_enabled(self):
        # type: () -> bool
        """Gets the network_explorer_enabled of this AnalyticsLicenseErrorDetailsConfig.

        Is network explorer feature enabled for the license

        :return: The network_explorer_enabled of this AnalyticsLicenseErrorDetailsConfig.
        :rtype: bool
        """
        return self._network_explorer_enabled

    @network_explorer_enabled.setter
    def network_explorer_enabled(self, network_explorer_enabled):
        # type: (bool) -> None
        """Sets the network_explorer_enabled of this AnalyticsLicenseErrorDetailsConfig.

        Is network explorer feature enabled for the license

        :param network_explorer_enabled: The network_explorer_enabled of this AnalyticsLicenseErrorDetailsConfig.
        :type: bool
        """

        if network_explorer_enabled is not None:
            if not isinstance(network_explorer_enabled, bool):
                raise TypeError("Invalid type for `network_explorer_enabled`, type has to be `bool`")

        self._network_explorer_enabled = network_explorer_enabled

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
        if not isinstance(other, AnalyticsLicenseErrorDetailsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
