# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.input_factor_bitrate import InputFactorBitrate
from bitmovin_api_sdk.models.input_factor_codec import InputFactorCodec
import pprint
import six


class InputFactor(object):
    @poscheck_model
    def __init__(self,
                 codec=None,
                 bitrate=None):
        # type: (InputFactorCodec, InputFactorBitrate) -> None

        self._codec = None
        self._bitrate = None
        self.discriminator = None

        if codec is not None:
            self.codec = codec
        if bitrate is not None:
            self.bitrate = bitrate

    @property
    def openapi_types(self):
        types = {
            'codec': 'InputFactorCodec',
            'bitrate': 'InputFactorBitrate'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'codec': 'codec',
            'bitrate': 'bitrate'
        }
        return attributes

    @property
    def codec(self):
        # type: () -> InputFactorCodec
        """Gets the codec of this InputFactor.


        :return: The codec of this InputFactor.
        :rtype: InputFactorCodec
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        # type: (InputFactorCodec) -> None
        """Sets the codec of this InputFactor.


        :param codec: The codec of this InputFactor.
        :type: InputFactorCodec
        """

        if codec is not None:
            if not isinstance(codec, InputFactorCodec):
                raise TypeError("Invalid type for `codec`, type has to be `InputFactorCodec`")

        self._codec = codec

    @property
    def bitrate(self):
        # type: () -> InputFactorBitrate
        """Gets the bitrate of this InputFactor.


        :return: The bitrate of this InputFactor.
        :rtype: InputFactorBitrate
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        # type: (InputFactorBitrate) -> None
        """Sets the bitrate of this InputFactor.


        :param bitrate: The bitrate of this InputFactor.
        :type: InputFactorBitrate
        """

        if bitrate is not None:
            if not isinstance(bitrate, InputFactorBitrate):
                raise TypeError("Invalid type for `bitrate`, type has to be `InputFactorBitrate`")

        self._bitrate = bitrate

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
        if not isinstance(other, InputFactor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
