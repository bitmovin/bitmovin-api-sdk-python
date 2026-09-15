# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class PccCodecReach(object):
    @poscheck_model
    def __init__(self,
                 codec=None,
                 by_device_type=None):
        # type: (string_types, list[PccCodecDeviceTypeReach]) -> None

        self._codec = None
        self._by_device_type = list()
        self.discriminator = None

        if codec is not None:
            self.codec = codec
        if by_device_type is not None:
            self.by_device_type = by_device_type

    @property
    def openapi_types(self):
        types = {
            'codec': 'string_types',
            'by_device_type': 'list[PccCodecDeviceTypeReach]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'codec': 'codec',
            'by_device_type': 'byDeviceType'
        }
        return attributes

    @property
    def codec(self):
        # type: () -> string_types
        """Gets the codec of this PccCodecReach.


        :return: The codec of this PccCodecReach.
        :rtype: string_types
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        # type: (string_types) -> None
        """Sets the codec of this PccCodecReach.


        :param codec: The codec of this PccCodecReach.
        :type: string_types
        """

        if codec is not None:
            if not isinstance(codec, string_types):
                raise TypeError("Invalid type for `codec`, type has to be `string_types`")

        self._codec = codec

    @property
    def by_device_type(self):
        # type: () -> list[PccCodecDeviceTypeReach]
        """Gets the by_device_type of this PccCodecReach.


        :return: The by_device_type of this PccCodecReach.
        :rtype: list[PccCodecDeviceTypeReach]
        """
        return self._by_device_type

    @by_device_type.setter
    def by_device_type(self, by_device_type):
        # type: (list) -> None
        """Sets the by_device_type of this PccCodecReach.


        :param by_device_type: The by_device_type of this PccCodecReach.
        :type: list[PccCodecDeviceTypeReach]
        """

        if by_device_type is not None:
            if not isinstance(by_device_type, list):
                raise TypeError("Invalid type for `by_device_type`, type has to be `list[PccCodecDeviceTypeReach]`")

        self._by_device_type = by_device_type

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
        if not isinstance(other, PccCodecReach):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
