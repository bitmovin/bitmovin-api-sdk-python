# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class SrtStatisticRecv(object):
    @poscheck_model
    def __init__(self,
                 bytes_=None,
                 bytes_dropped=None,
                 bytes_lost=None,
                 mbit_rate=None,
                 packets=None,
                 packets_belated=None,
                 packets_dropped=None,
                 packets_lost=None,
                 packets_retransmitted=None):
        # type: (int, int, int, float, int, int, int, int, int) -> None

        self._bytes = None
        self._bytes_dropped = None
        self._bytes_lost = None
        self._mbit_rate = None
        self._packets = None
        self._packets_belated = None
        self._packets_dropped = None
        self._packets_lost = None
        self._packets_retransmitted = None
        self.discriminator = None

        if bytes_ is not None:
            self.bytes = bytes_
        if bytes_dropped is not None:
            self.bytes_dropped = bytes_dropped
        if bytes_lost is not None:
            self.bytes_lost = bytes_lost
        if mbit_rate is not None:
            self.mbit_rate = mbit_rate
        if packets is not None:
            self.packets = packets
        if packets_belated is not None:
            self.packets_belated = packets_belated
        if packets_dropped is not None:
            self.packets_dropped = packets_dropped
        if packets_lost is not None:
            self.packets_lost = packets_lost
        if packets_retransmitted is not None:
            self.packets_retransmitted = packets_retransmitted

    @property
    def openapi_types(self):
        types = {
            'bytes': 'int',
            'bytes_dropped': 'int',
            'bytes_lost': 'int',
            'mbit_rate': 'float',
            'packets': 'int',
            'packets_belated': 'int',
            'packets_dropped': 'int',
            'packets_lost': 'int',
            'packets_retransmitted': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'bytes': 'bytes',
            'bytes_dropped': 'bytesDropped',
            'bytes_lost': 'bytesLost',
            'mbit_rate': 'mbitRate',
            'packets': 'packets',
            'packets_belated': 'packetsBelated',
            'packets_dropped': 'packetsDropped',
            'packets_lost': 'packetsLost',
            'packets_retransmitted': 'packetsRetransmitted'
        }
        return attributes

    @property
    def bytes(self):
        # type: () -> int
        """Gets the bytes of this SrtStatisticRecv.


        :return: The bytes of this SrtStatisticRecv.
        :rtype: int
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes_):
        # type: (int) -> None
        """Sets the bytes of this SrtStatisticRecv.


        :param bytes_: The bytes of this SrtStatisticRecv.
        :type: int
        """

        if bytes_ is not None:
            if not isinstance(bytes_, int):
                raise TypeError("Invalid type for `bytes`, type has to be `int`")

        self._bytes = bytes_

    @property
    def bytes_dropped(self):
        # type: () -> int
        """Gets the bytes_dropped of this SrtStatisticRecv.


        :return: The bytes_dropped of this SrtStatisticRecv.
        :rtype: int
        """
        return self._bytes_dropped

    @bytes_dropped.setter
    def bytes_dropped(self, bytes_dropped):
        # type: (int) -> None
        """Sets the bytes_dropped of this SrtStatisticRecv.


        :param bytes_dropped: The bytes_dropped of this SrtStatisticRecv.
        :type: int
        """

        if bytes_dropped is not None:
            if not isinstance(bytes_dropped, int):
                raise TypeError("Invalid type for `bytes_dropped`, type has to be `int`")

        self._bytes_dropped = bytes_dropped

    @property
    def bytes_lost(self):
        # type: () -> int
        """Gets the bytes_lost of this SrtStatisticRecv.


        :return: The bytes_lost of this SrtStatisticRecv.
        :rtype: int
        """
        return self._bytes_lost

    @bytes_lost.setter
    def bytes_lost(self, bytes_lost):
        # type: (int) -> None
        """Sets the bytes_lost of this SrtStatisticRecv.


        :param bytes_lost: The bytes_lost of this SrtStatisticRecv.
        :type: int
        """

        if bytes_lost is not None:
            if not isinstance(bytes_lost, int):
                raise TypeError("Invalid type for `bytes_lost`, type has to be `int`")

        self._bytes_lost = bytes_lost

    @property
    def mbit_rate(self):
        # type: () -> float
        """Gets the mbit_rate of this SrtStatisticRecv.


        :return: The mbit_rate of this SrtStatisticRecv.
        :rtype: float
        """
        return self._mbit_rate

    @mbit_rate.setter
    def mbit_rate(self, mbit_rate):
        # type: (float) -> None
        """Sets the mbit_rate of this SrtStatisticRecv.


        :param mbit_rate: The mbit_rate of this SrtStatisticRecv.
        :type: float
        """

        if mbit_rate is not None:
            if not isinstance(mbit_rate, (float, int)):
                raise TypeError("Invalid type for `mbit_rate`, type has to be `float`")

        self._mbit_rate = mbit_rate

    @property
    def packets(self):
        # type: () -> int
        """Gets the packets of this SrtStatisticRecv.


        :return: The packets of this SrtStatisticRecv.
        :rtype: int
        """
        return self._packets

    @packets.setter
    def packets(self, packets):
        # type: (int) -> None
        """Sets the packets of this SrtStatisticRecv.


        :param packets: The packets of this SrtStatisticRecv.
        :type: int
        """

        if packets is not None:
            if not isinstance(packets, int):
                raise TypeError("Invalid type for `packets`, type has to be `int`")

        self._packets = packets

    @property
    def packets_belated(self):
        # type: () -> int
        """Gets the packets_belated of this SrtStatisticRecv.


        :return: The packets_belated of this SrtStatisticRecv.
        :rtype: int
        """
        return self._packets_belated

    @packets_belated.setter
    def packets_belated(self, packets_belated):
        # type: (int) -> None
        """Sets the packets_belated of this SrtStatisticRecv.


        :param packets_belated: The packets_belated of this SrtStatisticRecv.
        :type: int
        """

        if packets_belated is not None:
            if not isinstance(packets_belated, int):
                raise TypeError("Invalid type for `packets_belated`, type has to be `int`")

        self._packets_belated = packets_belated

    @property
    def packets_dropped(self):
        # type: () -> int
        """Gets the packets_dropped of this SrtStatisticRecv.


        :return: The packets_dropped of this SrtStatisticRecv.
        :rtype: int
        """
        return self._packets_dropped

    @packets_dropped.setter
    def packets_dropped(self, packets_dropped):
        # type: (int) -> None
        """Sets the packets_dropped of this SrtStatisticRecv.


        :param packets_dropped: The packets_dropped of this SrtStatisticRecv.
        :type: int
        """

        if packets_dropped is not None:
            if not isinstance(packets_dropped, int):
                raise TypeError("Invalid type for `packets_dropped`, type has to be `int`")

        self._packets_dropped = packets_dropped

    @property
    def packets_lost(self):
        # type: () -> int
        """Gets the packets_lost of this SrtStatisticRecv.


        :return: The packets_lost of this SrtStatisticRecv.
        :rtype: int
        """
        return self._packets_lost

    @packets_lost.setter
    def packets_lost(self, packets_lost):
        # type: (int) -> None
        """Sets the packets_lost of this SrtStatisticRecv.


        :param packets_lost: The packets_lost of this SrtStatisticRecv.
        :type: int
        """

        if packets_lost is not None:
            if not isinstance(packets_lost, int):
                raise TypeError("Invalid type for `packets_lost`, type has to be `int`")

        self._packets_lost = packets_lost

    @property
    def packets_retransmitted(self):
        # type: () -> int
        """Gets the packets_retransmitted of this SrtStatisticRecv.


        :return: The packets_retransmitted of this SrtStatisticRecv.
        :rtype: int
        """
        return self._packets_retransmitted

    @packets_retransmitted.setter
    def packets_retransmitted(self, packets_retransmitted):
        # type: (int) -> None
        """Sets the packets_retransmitted of this SrtStatisticRecv.


        :param packets_retransmitted: The packets_retransmitted of this SrtStatisticRecv.
        :type: int
        """

        if packets_retransmitted is not None:
            if not isinstance(packets_retransmitted, int):
                raise TypeError("Invalid type for `packets_retransmitted`, type has to be `int`")

        self._packets_retransmitted = packets_retransmitted

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
        if not isinstance(other, SrtStatisticRecv):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
