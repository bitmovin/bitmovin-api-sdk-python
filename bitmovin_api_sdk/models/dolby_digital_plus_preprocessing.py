# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dolby_digital_plus_dynamic_range_compression import DolbyDigitalPlusDynamicRangeCompression
from bitmovin_api_sdk.models.dolby_digital_plus_lfe_low_pass_filter import DolbyDigitalPlusLfeLowPassFilter
from bitmovin_api_sdk.models.dolby_digital_plus_ninety_degree_phase_shift import DolbyDigitalPlusNinetyDegreePhaseShift
from bitmovin_api_sdk.models.dolby_digital_plus_three_db_attenuation import DolbyDigitalPlusThreeDbAttenuation
import pprint
import six


class DolbyDigitalPlusPreprocessing(object):
    @poscheck_model
    def __init__(self,
                 dynamic_range_compression=None,
                 lfe_low_pass_filter=None,
                 ninety_degree_phase_shift=None,
                 three_db_attenuation=None):
        # type: (DolbyDigitalPlusDynamicRangeCompression, DolbyDigitalPlusLfeLowPassFilter, DolbyDigitalPlusNinetyDegreePhaseShift, DolbyDigitalPlusThreeDbAttenuation) -> None

        self._dynamic_range_compression = None
        self._lfe_low_pass_filter = None
        self._ninety_degree_phase_shift = None
        self._three_db_attenuation = None
        self.discriminator = None

        if dynamic_range_compression is not None:
            self.dynamic_range_compression = dynamic_range_compression
        if lfe_low_pass_filter is not None:
            self.lfe_low_pass_filter = lfe_low_pass_filter
        if ninety_degree_phase_shift is not None:
            self.ninety_degree_phase_shift = ninety_degree_phase_shift
        if three_db_attenuation is not None:
            self.three_db_attenuation = three_db_attenuation

    @property
    def openapi_types(self):
        types = {
            'dynamic_range_compression': 'DolbyDigitalPlusDynamicRangeCompression',
            'lfe_low_pass_filter': 'DolbyDigitalPlusLfeLowPassFilter',
            'ninety_degree_phase_shift': 'DolbyDigitalPlusNinetyDegreePhaseShift',
            'three_db_attenuation': 'DolbyDigitalPlusThreeDbAttenuation'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'dynamic_range_compression': 'dynamicRangeCompression',
            'lfe_low_pass_filter': 'lfeLowPassFilter',
            'ninety_degree_phase_shift': 'ninetyDegreePhaseShift',
            'three_db_attenuation': 'threeDbAttenuation'
        }
        return attributes

    @property
    def dynamic_range_compression(self):
        # type: () -> DolbyDigitalPlusDynamicRangeCompression
        """Gets the dynamic_range_compression of this DolbyDigitalPlusPreprocessing.

        It indicates a gain change to be applied in the Dolby Digital decoder in order to implement dynamic range compression.  The values typically indicate gain reductions (cut) during loud passages and gain increases (boost) during quiet passages based on desired compression characteristics. 

        :return: The dynamic_range_compression of this DolbyDigitalPlusPreprocessing.
        :rtype: DolbyDigitalPlusDynamicRangeCompression
        """
        return self._dynamic_range_compression

    @dynamic_range_compression.setter
    def dynamic_range_compression(self, dynamic_range_compression):
        # type: (DolbyDigitalPlusDynamicRangeCompression) -> None
        """Sets the dynamic_range_compression of this DolbyDigitalPlusPreprocessing.

        It indicates a gain change to be applied in the Dolby Digital decoder in order to implement dynamic range compression.  The values typically indicate gain reductions (cut) during loud passages and gain increases (boost) during quiet passages based on desired compression characteristics. 

        :param dynamic_range_compression: The dynamic_range_compression of this DolbyDigitalPlusPreprocessing.
        :type: DolbyDigitalPlusDynamicRangeCompression
        """

        if dynamic_range_compression is not None:
            if not isinstance(dynamic_range_compression, DolbyDigitalPlusDynamicRangeCompression):
                raise TypeError("Invalid type for `dynamic_range_compression`, type has to be `DolbyDigitalPlusDynamicRangeCompression`")

        self._dynamic_range_compression = dynamic_range_compression

    @property
    def lfe_low_pass_filter(self):
        # type: () -> DolbyDigitalPlusLfeLowPassFilter
        """Gets the lfe_low_pass_filter of this DolbyDigitalPlusPreprocessing.

        It applies a 120 Hz low-pass filter to the low-frequency effects (LFE) channel.  This is only allowed if the `channelLayout` contains a LFE channel. 

        :return: The lfe_low_pass_filter of this DolbyDigitalPlusPreprocessing.
        :rtype: DolbyDigitalPlusLfeLowPassFilter
        """
        return self._lfe_low_pass_filter

    @lfe_low_pass_filter.setter
    def lfe_low_pass_filter(self, lfe_low_pass_filter):
        # type: (DolbyDigitalPlusLfeLowPassFilter) -> None
        """Sets the lfe_low_pass_filter of this DolbyDigitalPlusPreprocessing.

        It applies a 120 Hz low-pass filter to the low-frequency effects (LFE) channel.  This is only allowed if the `channelLayout` contains a LFE channel. 

        :param lfe_low_pass_filter: The lfe_low_pass_filter of this DolbyDigitalPlusPreprocessing.
        :type: DolbyDigitalPlusLfeLowPassFilter
        """

        if lfe_low_pass_filter is not None:
            if not isinstance(lfe_low_pass_filter, DolbyDigitalPlusLfeLowPassFilter):
                raise TypeError("Invalid type for `lfe_low_pass_filter`, type has to be `DolbyDigitalPlusLfeLowPassFilter`")

        self._lfe_low_pass_filter = lfe_low_pass_filter

    @property
    def ninety_degree_phase_shift(self):
        # type: () -> DolbyDigitalPlusNinetyDegreePhaseShift
        """Gets the ninety_degree_phase_shift of this DolbyDigitalPlusPreprocessing.


        :return: The ninety_degree_phase_shift of this DolbyDigitalPlusPreprocessing.
        :rtype: DolbyDigitalPlusNinetyDegreePhaseShift
        """
        return self._ninety_degree_phase_shift

    @ninety_degree_phase_shift.setter
    def ninety_degree_phase_shift(self, ninety_degree_phase_shift):
        # type: (DolbyDigitalPlusNinetyDegreePhaseShift) -> None
        """Sets the ninety_degree_phase_shift of this DolbyDigitalPlusPreprocessing.


        :param ninety_degree_phase_shift: The ninety_degree_phase_shift of this DolbyDigitalPlusPreprocessing.
        :type: DolbyDigitalPlusNinetyDegreePhaseShift
        """

        if ninety_degree_phase_shift is not None:
            if not isinstance(ninety_degree_phase_shift, DolbyDigitalPlusNinetyDegreePhaseShift):
                raise TypeError("Invalid type for `ninety_degree_phase_shift`, type has to be `DolbyDigitalPlusNinetyDegreePhaseShift`")

        self._ninety_degree_phase_shift = ninety_degree_phase_shift

    @property
    def three_db_attenuation(self):
        # type: () -> DolbyDigitalPlusThreeDbAttenuation
        """Gets the three_db_attenuation of this DolbyDigitalPlusPreprocessing.


        :return: The three_db_attenuation of this DolbyDigitalPlusPreprocessing.
        :rtype: DolbyDigitalPlusThreeDbAttenuation
        """
        return self._three_db_attenuation

    @three_db_attenuation.setter
    def three_db_attenuation(self, three_db_attenuation):
        # type: (DolbyDigitalPlusThreeDbAttenuation) -> None
        """Sets the three_db_attenuation of this DolbyDigitalPlusPreprocessing.


        :param three_db_attenuation: The three_db_attenuation of this DolbyDigitalPlusPreprocessing.
        :type: DolbyDigitalPlusThreeDbAttenuation
        """

        if three_db_attenuation is not None:
            if not isinstance(three_db_attenuation, DolbyDigitalPlusThreeDbAttenuation):
                raise TypeError("Invalid type for `three_db_attenuation`, type has to be `DolbyDigitalPlusThreeDbAttenuation`")

        self._three_db_attenuation = three_db_attenuation

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
        if not isinstance(other, DolbyDigitalPlusPreprocessing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
