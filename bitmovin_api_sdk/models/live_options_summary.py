# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.live_options_entry import LiveOptionsEntry
import pprint
import six


class LiveOptionsSummary(object):
    @poscheck_model
    def __init__(self,
                 hd=None):
        # type: (LiveOptionsEntry) -> None

        self._hd = None
        self.discriminator = None

        if hd is not None:
            self.hd = hd

    @property
    def openapi_types(self):
        types = {
            'hd': 'LiveOptionsEntry'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'hd': 'hd'
        }
        return attributes

    @property
    def hd(self):
        # type: () -> LiveOptionsEntry
        """Gets the hd of this LiveOptionsSummary.


        :return: The hd of this LiveOptionsSummary.
        :rtype: LiveOptionsEntry
        """
        return self._hd

    @hd.setter
    def hd(self, hd):
        # type: (LiveOptionsEntry) -> None
        """Sets the hd of this LiveOptionsSummary.


        :param hd: The hd of this LiveOptionsSummary.
        :type: LiveOptionsEntry
        """

        if hd is not None:
            if not isinstance(hd, LiveOptionsEntry):
                raise TypeError("Invalid type for `hd`, type has to be `LiveOptionsEntry`")

        self._hd = hd

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
        if not isinstance(other, LiveOptionsSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
