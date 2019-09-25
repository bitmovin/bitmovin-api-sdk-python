# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class SrtStatisticLink(object):
    @poscheck_model
    def __init__(self,
                 bandwidth=None,
                 max_bandwidth=None,
                 rtt=None):
        # type: (float, float, float) -> None

        self._bandwidth = None
        self._max_bandwidth = None
        self._rtt = None
        self.discriminator = None

        if bandwidth is not None:
            self.bandwidth = bandwidth
        if max_bandwidth is not None:
            self.max_bandwidth = max_bandwidth
        if rtt is not None:
            self.rtt = rtt

    @property
    def openapi_types(self):
        types = {
            'bandwidth': 'float',
            'max_bandwidth': 'float',
            'rtt': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'bandwidth': 'bandwidth',
            'max_bandwidth': 'maxBandwidth',
            'rtt': 'rtt'
        }
        return attributes

    @property
    def bandwidth(self):
        # type: () -> float
        """Gets the bandwidth of this SrtStatisticLink.


        :return: The bandwidth of this SrtStatisticLink.
        :rtype: float
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        # type: (float) -> None
        """Sets the bandwidth of this SrtStatisticLink.


        :param bandwidth: The bandwidth of this SrtStatisticLink.
        :type: float
        """

        if bandwidth is not None:
            if not isinstance(bandwidth, (float, int)):
                raise TypeError("Invalid type for `bandwidth`, type has to be `float`")

        self._bandwidth = bandwidth

    @property
    def max_bandwidth(self):
        # type: () -> float
        """Gets the max_bandwidth of this SrtStatisticLink.


        :return: The max_bandwidth of this SrtStatisticLink.
        :rtype: float
        """
        return self._max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        # type: (float) -> None
        """Sets the max_bandwidth of this SrtStatisticLink.


        :param max_bandwidth: The max_bandwidth of this SrtStatisticLink.
        :type: float
        """

        if max_bandwidth is not None:
            if not isinstance(max_bandwidth, (float, int)):
                raise TypeError("Invalid type for `max_bandwidth`, type has to be `float`")

        self._max_bandwidth = max_bandwidth

    @property
    def rtt(self):
        # type: () -> float
        """Gets the rtt of this SrtStatisticLink.


        :return: The rtt of this SrtStatisticLink.
        :rtype: float
        """
        return self._rtt

    @rtt.setter
    def rtt(self, rtt):
        # type: (float) -> None
        """Sets the rtt of this SrtStatisticLink.


        :param rtt: The rtt of this SrtStatisticLink.
        :type: float
        """

        if rtt is not None:
            if not isinstance(rtt, (float, int)):
                raise TypeError("Invalid type for `rtt`, type has to be `float`")

        self._rtt = rtt

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
        if not isinstance(other, SrtStatisticLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
