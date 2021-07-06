# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dolby_digital_dynamic_range_compression_mode import DolbyDigitalDynamicRangeCompressionMode
import pprint
import six


class DolbyDigitalDynamicRangeCompression(object):
    @poscheck_model
    def __init__(self,
                 line_mode=None,
                 rf_mode=None):
        # type: (DolbyDigitalDynamicRangeCompressionMode, DolbyDigitalDynamicRangeCompressionMode) -> None

        self._line_mode = None
        self._rf_mode = None
        self.discriminator = None

        if line_mode is not None:
            self.line_mode = line_mode
        if rf_mode is not None:
            self.rf_mode = rf_mode

    @property
    def openapi_types(self):
        types = {
            'line_mode': 'DolbyDigitalDynamicRangeCompressionMode',
            'rf_mode': 'DolbyDigitalDynamicRangeCompressionMode'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'line_mode': 'lineMode',
            'rf_mode': 'rfMode'
        }
        return attributes

    @property
    def line_mode(self):
        # type: () -> DolbyDigitalDynamicRangeCompressionMode
        """Gets the line_mode of this DolbyDigitalDynamicRangeCompression.

        Line mode is intended for use in products providing line‐level or speaker‐level outputs, and is applicable to the widest range of products. Products such as set‐top boxes, DVD players, DTVs, A/V surround decoders, and outboard Dolby Digital decoders typically use this mode.

        :return: The line_mode of this DolbyDigitalDynamicRangeCompression.
        :rtype: DolbyDigitalDynamicRangeCompressionMode
        """
        return self._line_mode

    @line_mode.setter
    def line_mode(self, line_mode):
        # type: (DolbyDigitalDynamicRangeCompressionMode) -> None
        """Sets the line_mode of this DolbyDigitalDynamicRangeCompression.

        Line mode is intended for use in products providing line‐level or speaker‐level outputs, and is applicable to the widest range of products. Products such as set‐top boxes, DVD players, DTVs, A/V surround decoders, and outboard Dolby Digital decoders typically use this mode.

        :param line_mode: The line_mode of this DolbyDigitalDynamicRangeCompression.
        :type: DolbyDigitalDynamicRangeCompressionMode
        """

        if line_mode is not None:
            if not isinstance(line_mode, DolbyDigitalDynamicRangeCompressionMode):
                raise TypeError("Invalid type for `line_mode`, type has to be `DolbyDigitalDynamicRangeCompressionMode`")

        self._line_mode = line_mode

    @property
    def rf_mode(self):
        # type: () -> DolbyDigitalDynamicRangeCompressionMode
        """Gets the rf_mode of this DolbyDigitalDynamicRangeCompression.

        RF mode is intended for products such as a low‐cost television receivers.

        :return: The rf_mode of this DolbyDigitalDynamicRangeCompression.
        :rtype: DolbyDigitalDynamicRangeCompressionMode
        """
        return self._rf_mode

    @rf_mode.setter
    def rf_mode(self, rf_mode):
        # type: (DolbyDigitalDynamicRangeCompressionMode) -> None
        """Sets the rf_mode of this DolbyDigitalDynamicRangeCompression.

        RF mode is intended for products such as a low‐cost television receivers.

        :param rf_mode: The rf_mode of this DolbyDigitalDynamicRangeCompression.
        :type: DolbyDigitalDynamicRangeCompressionMode
        """

        if rf_mode is not None:
            if not isinstance(rf_mode, DolbyDigitalDynamicRangeCompressionMode):
                raise TypeError("Invalid type for `rf_mode`, type has to be `DolbyDigitalDynamicRangeCompressionMode`")

        self._rf_mode = rf_mode

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
        if not isinstance(other, DolbyDigitalDynamicRangeCompression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
