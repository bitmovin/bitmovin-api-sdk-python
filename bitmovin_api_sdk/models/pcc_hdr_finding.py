# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class PccHdrFinding(object):
    @poscheck_model
    def __init__(self,
                 device=None,
                 codec=None,
                 protection=None,
                 sentence=None):
        # type: (string_types, string_types, string_types, string_types) -> None

        self._device = None
        self._codec = None
        self._protection = None
        self._sentence = None
        self.discriminator = None

        if device is not None:
            self.device = device
        if codec is not None:
            self.codec = codec
        if protection is not None:
            self.protection = protection
        if sentence is not None:
            self.sentence = sentence

    @property
    def openapi_types(self):
        types = {
            'device': 'string_types',
            'codec': 'string_types',
            'protection': 'string_types',
            'sentence': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'device': 'device',
            'codec': 'codec',
            'protection': 'protection',
            'sentence': 'sentence'
        }
        return attributes

    @property
    def device(self):
        # type: () -> string_types
        """Gets the device of this PccHdrFinding.

        The device pool, under the name the rest of the report shows it by. (required)

        :return: The device of this PccHdrFinding.
        :rtype: string_types
        """
        return self._device

    @device.setter
    def device(self, device):
        # type: (string_types) -> None
        """Sets the device of this PccHdrFinding.

        The device pool, under the name the rest of the report shows it by. (required)

        :param device: The device of this PccHdrFinding.
        :type: string_types
        """

        if device is not None:
            if not isinstance(device, string_types):
                raise TypeError("Invalid type for `device`, type has to be `string_types`")

        self._device = device

    @property
    def codec(self):
        # type: () -> string_types
        """Gets the codec of this PccHdrFinding.


        :return: The codec of this PccHdrFinding.
        :rtype: string_types
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        # type: (string_types) -> None
        """Sets the codec of this PccHdrFinding.


        :param codec: The codec of this PccHdrFinding.
        :type: string_types
        """

        if codec is not None:
            if not isinstance(codec, string_types):
                raise TypeError("Invalid type for `codec`, type has to be `string_types`")

        self._codec = codec

    @property
    def protection(self):
        # type: () -> string_types
        """Gets the protection of this PccHdrFinding.


        :return: The protection of this PccHdrFinding.
        :rtype: string_types
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        # type: (string_types) -> None
        """Sets the protection of this PccHdrFinding.


        :param protection: The protection of this PccHdrFinding.
        :type: string_types
        """

        if protection is not None:
            if not isinstance(protection, string_types):
                raise TypeError("Invalid type for `protection`, type has to be `string_types`")

        self._protection = protection

    @property
    def sentence(self):
        # type: () -> string_types
        """Gets the sentence of this PccHdrFinding.

        What was found, in one paragraph. (required)

        :return: The sentence of this PccHdrFinding.
        :rtype: string_types
        """
        return self._sentence

    @sentence.setter
    def sentence(self, sentence):
        # type: (string_types) -> None
        """Sets the sentence of this PccHdrFinding.

        What was found, in one paragraph. (required)

        :param sentence: The sentence of this PccHdrFinding.
        :type: string_types
        """

        if sentence is not None:
            if not isinstance(sentence, string_types):
                raise TypeError("Invalid type for `sentence`, type has to be `string_types`")

        self._sentence = sentence

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
        if not isinstance(other, PccHdrFinding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
