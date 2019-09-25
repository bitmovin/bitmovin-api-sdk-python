# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.time_span import TimeSpan
import pprint
import six


class PsnrQualityMetric(object):
    @poscheck_model
    def __init__(self,
                 time_span=None,
                 psnr=None):
        # type: (TimeSpan, float) -> None

        self._time_span = None
        self._psnr = None
        self.discriminator = None

        if time_span is not None:
            self.time_span = time_span
        if psnr is not None:
            self.psnr = psnr

    @property
    def openapi_types(self):
        types = {
            'time_span': 'TimeSpan',
            'psnr': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'time_span': 'timeSpan',
            'psnr': 'psnr'
        }
        return attributes

    @property
    def time_span(self):
        # type: () -> TimeSpan
        """Gets the time_span of this PsnrQualityMetric.


        :return: The time_span of this PsnrQualityMetric.
        :rtype: TimeSpan
        """
        return self._time_span

    @time_span.setter
    def time_span(self, time_span):
        # type: (TimeSpan) -> None
        """Sets the time_span of this PsnrQualityMetric.


        :param time_span: The time_span of this PsnrQualityMetric.
        :type: TimeSpan
        """

        if time_span is not None:
            if not isinstance(time_span, TimeSpan):
                raise TypeError("Invalid type for `time_span`, type has to be `TimeSpan`")

        self._time_span = time_span

    @property
    def psnr(self):
        # type: () -> float
        """Gets the psnr of this PsnrQualityMetric.

        Peak signal-to-noise ratio (required)

        :return: The psnr of this PsnrQualityMetric.
        :rtype: float
        """
        return self._psnr

    @psnr.setter
    def psnr(self, psnr):
        # type: (float) -> None
        """Sets the psnr of this PsnrQualityMetric.

        Peak signal-to-noise ratio (required)

        :param psnr: The psnr of this PsnrQualityMetric.
        :type: float
        """

        if psnr is not None:
            if not isinstance(psnr, (float, int)):
                raise TypeError("Invalid type for `psnr`, type has to be `float`")

        self._psnr = psnr

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
        if not isinstance(other, PsnrQualityMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
