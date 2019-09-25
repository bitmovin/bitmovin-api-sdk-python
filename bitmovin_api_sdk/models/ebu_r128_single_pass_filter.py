# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.filter import Filter
import pprint
import six


class EbuR128SinglePassFilter(Filter):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 integrated_loudness=None,
                 loudness_range=None,
                 maximum_true_peak_level=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, float, float, float) -> None
        super(EbuR128SinglePassFilter, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_)

        self._integrated_loudness = None
        self._loudness_range = None
        self._maximum_true_peak_level = None
        self.discriminator = None

        if integrated_loudness is not None:
            self.integrated_loudness = integrated_loudness
        if loudness_range is not None:
            self.loudness_range = loudness_range
        if maximum_true_peak_level is not None:
            self.maximum_true_peak_level = maximum_true_peak_level

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(EbuR128SinglePassFilter, self), 'openapi_types'):
            types = getattr(super(EbuR128SinglePassFilter, self), 'openapi_types')

        types.update({
            'integrated_loudness': 'float',
            'loudness_range': 'float',
            'maximum_true_peak_level': 'float'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(EbuR128SinglePassFilter, self), 'attribute_map'):
            attributes = getattr(super(EbuR128SinglePassFilter, self), 'attribute_map')

        attributes.update({
            'integrated_loudness': 'integratedLoudness',
            'loudness_range': 'loudnessRange',
            'maximum_true_peak_level': 'maximumTruePeakLevel'
        })
        return attributes

    @property
    def integrated_loudness(self):
        # type: () -> float
        """Gets the integrated_loudness of this EbuR128SinglePassFilter.

        Set the targeted integrated loudness value. Range is from '-70.0' to '-5.0'. Default value is '-24.0'. Value is measured in LUFS (Loudness Units, referenced to Full Scale)

        :return: The integrated_loudness of this EbuR128SinglePassFilter.
        :rtype: float
        """
        return self._integrated_loudness

    @integrated_loudness.setter
    def integrated_loudness(self, integrated_loudness):
        # type: (float) -> None
        """Sets the integrated_loudness of this EbuR128SinglePassFilter.

        Set the targeted integrated loudness value. Range is from '-70.0' to '-5.0'. Default value is '-24.0'. Value is measured in LUFS (Loudness Units, referenced to Full Scale)

        :param integrated_loudness: The integrated_loudness of this EbuR128SinglePassFilter.
        :type: float
        """

        if integrated_loudness is not None:
            if not isinstance(integrated_loudness, (float, int)):
                raise TypeError("Invalid type for `integrated_loudness`, type has to be `float`")

        self._integrated_loudness = integrated_loudness

    @property
    def loudness_range(self):
        # type: () -> float
        """Gets the loudness_range of this EbuR128SinglePassFilter.

        Set the targeted loudness range target. Range is from '1.0' to '20.0'. Default value is '7.0'. Loudness range measures the variation of loudness on a macroscopic time-scale in units of LU (Loudness Units). For programmes shorter than 1 minute, the use of the measure Loudness Range is not recommended due to too few data points (Loudness Range is based on the Short-term-Loudness values (3-seconds-window)).

        :return: The loudness_range of this EbuR128SinglePassFilter.
        :rtype: float
        """
        return self._loudness_range

    @loudness_range.setter
    def loudness_range(self, loudness_range):
        # type: (float) -> None
        """Sets the loudness_range of this EbuR128SinglePassFilter.

        Set the targeted loudness range target. Range is from '1.0' to '20.0'. Default value is '7.0'. Loudness range measures the variation of loudness on a macroscopic time-scale in units of LU (Loudness Units). For programmes shorter than 1 minute, the use of the measure Loudness Range is not recommended due to too few data points (Loudness Range is based on the Short-term-Loudness values (3-seconds-window)).

        :param loudness_range: The loudness_range of this EbuR128SinglePassFilter.
        :type: float
        """

        if loudness_range is not None:
            if not isinstance(loudness_range, (float, int)):
                raise TypeError("Invalid type for `loudness_range`, type has to be `float`")

        self._loudness_range = loudness_range

    @property
    def maximum_true_peak_level(self):
        # type: () -> float
        """Gets the maximum_true_peak_level of this EbuR128SinglePassFilter.

        Set maximum true peak. Range is from '-9.0' to '0.0'. Default value is '-2.0'. Values are measured in dBTP (db True Peak)

        :return: The maximum_true_peak_level of this EbuR128SinglePassFilter.
        :rtype: float
        """
        return self._maximum_true_peak_level

    @maximum_true_peak_level.setter
    def maximum_true_peak_level(self, maximum_true_peak_level):
        # type: (float) -> None
        """Sets the maximum_true_peak_level of this EbuR128SinglePassFilter.

        Set maximum true peak. Range is from '-9.0' to '0.0'. Default value is '-2.0'. Values are measured in dBTP (db True Peak)

        :param maximum_true_peak_level: The maximum_true_peak_level of this EbuR128SinglePassFilter.
        :type: float
        """

        if maximum_true_peak_level is not None:
            if not isinstance(maximum_true_peak_level, (float, int)):
                raise TypeError("Invalid type for `maximum_true_peak_level`, type has to be `float`")

        self._maximum_true_peak_level = maximum_true_peak_level

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(EbuR128SinglePassFilter, self), "to_dict"):
            result = super(EbuR128SinglePassFilter, self).to_dict()
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
        if not isinstance(other, EbuR128SinglePassFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
