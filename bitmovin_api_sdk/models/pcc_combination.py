# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class PccCombination(object):
    @poscheck_model
    def __init__(self,
                 codec=None,
                 protection=None,
                 label=None,
                 hdr=None):
        # type: (string_types, string_types, string_types, bool) -> None

        self._codec = None
        self._protection = None
        self._label = None
        self._hdr = None
        self.discriminator = None

        if codec is not None:
            self.codec = codec
        if protection is not None:
            self.protection = protection
        if label is not None:
            self.label = label
        if hdr is not None:
            self.hdr = hdr

    @property
    def openapi_types(self):
        types = {
            'codec': 'string_types',
            'protection': 'string_types',
            'label': 'string_types',
            'hdr': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'codec': 'codec',
            'protection': 'protection',
            'label': 'label',
            'hdr': 'hdr'
        }
        return attributes

    @property
    def codec(self):
        # type: () -> string_types
        """Gets the codec of this PccCombination.

        The codec, as the shared contract spells it. (required)

        :return: The codec of this PccCombination.
        :rtype: string_types
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        # type: (string_types) -> None
        """Sets the codec of this PccCombination.

        The codec, as the shared contract spells it. (required)

        :param codec: The codec of this PccCombination.
        :type: string_types
        """

        if codec is not None:
            if not isinstance(codec, string_types):
                raise TypeError("Invalid type for `codec`, type has to be `string_types`")

        self._codec = codec

    @property
    def protection(self):
        # type: () -> string_types
        """Gets the protection of this PccCombination.

        The content protection, as the shared contract spells it. (required)

        :return: The protection of this PccCombination.
        :rtype: string_types
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        # type: (string_types) -> None
        """Sets the protection of this PccCombination.

        The content protection, as the shared contract spells it. (required)

        :param protection: The protection of this PccCombination.
        :type: string_types
        """

        if protection is not None:
            if not isinstance(protection, string_types):
                raise TypeError("Invalid type for `protection`, type has to be `string_types`")

        self._protection = protection

    @property
    def label(self):
        # type: () -> string_types
        """Gets the label of this PccCombination.

        The column heading, spelled the way a reader reads it rather than the way the catalogue spells it. (required)

        :return: The label of this PccCombination.
        :rtype: string_types
        """
        return self._label

    @label.setter
    def label(self, label):
        # type: (string_types) -> None
        """Sets the label of this PccCombination.

        The column heading, spelled the way a reader reads it rather than the way the catalogue spells it. (required)

        :param label: The label of this PccCombination.
        :type: string_types
        """

        if label is not None:
            if not isinstance(label, string_types):
                raise TypeError("Invalid type for `label`, type has to be `string_types`")

        self._label = label

    @property
    def hdr(self):
        # type: () -> bool
        """Gets the hdr of this PccCombination.

        Whether this column's stream is HDR. Read it here rather than out of the codec name: not every HDR codec spells `hdr10`, and the Dolby Vision ones never do. (required)

        :return: The hdr of this PccCombination.
        :rtype: bool
        """
        return self._hdr

    @hdr.setter
    def hdr(self, hdr):
        # type: (bool) -> None
        """Sets the hdr of this PccCombination.

        Whether this column's stream is HDR. Read it here rather than out of the codec name: not every HDR codec spells `hdr10`, and the Dolby Vision ones never do. (required)

        :param hdr: The hdr of this PccCombination.
        :type: bool
        """

        if hdr is not None:
            if not isinstance(hdr, bool):
                raise TypeError("Invalid type for `hdr`, type has to be `bool`")

        self._hdr = hdr

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
        if not isinstance(other, PccCombination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
