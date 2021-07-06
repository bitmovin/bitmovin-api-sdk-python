# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dolby_digital_dynamic_range_compression import DolbyDigitalDynamicRangeCompression
from bitmovin_api_sdk.models.dolby_digital_lfe_low_pass_filter import DolbyDigitalLfeLowPassFilter
from bitmovin_api_sdk.models.dolby_digital_ninety_degree_phase_shift import DolbyDigitalNinetyDegreePhaseShift
from bitmovin_api_sdk.models.dolby_digital_three_db_attenuation import DolbyDigitalThreeDbAttenuation
import pprint
import six


class DolbyDigitalPreprocessing(object):
    @poscheck_model
    def __init__(self,
                 dynamic_range_compression=None,
                 lfe_low_pass_filter=None,
                 ninety_degree_phase_shift=None,
                 three_db_attenuation=None):
        # type: (DolbyDigitalDynamicRangeCompression, DolbyDigitalLfeLowPassFilter, DolbyDigitalNinetyDegreePhaseShift, DolbyDigitalThreeDbAttenuation) -> None

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
            'dynamic_range_compression': 'DolbyDigitalDynamicRangeCompression',
            'lfe_low_pass_filter': 'DolbyDigitalLfeLowPassFilter',
            'ninety_degree_phase_shift': 'DolbyDigitalNinetyDegreePhaseShift',
            'three_db_attenuation': 'DolbyDigitalThreeDbAttenuation'
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
        # type: () -> DolbyDigitalDynamicRangeCompression
        """Gets the dynamic_range_compression of this DolbyDigitalPreprocessing.

        It indicates a gain change to be applied in the Dolby Digital decoder in order to implement dynamic range compression.  The values typically indicate gain reductions (cut) during loud passages and gain increases (boost) during quiet passages based on desired compression characteristics. 

        :return: The dynamic_range_compression of this DolbyDigitalPreprocessing.
        :rtype: DolbyDigitalDynamicRangeCompression
        """
        return self._dynamic_range_compression

    @dynamic_range_compression.setter
    def dynamic_range_compression(self, dynamic_range_compression):
        # type: (DolbyDigitalDynamicRangeCompression) -> None
        """Sets the dynamic_range_compression of this DolbyDigitalPreprocessing.

        It indicates a gain change to be applied in the Dolby Digital decoder in order to implement dynamic range compression.  The values typically indicate gain reductions (cut) during loud passages and gain increases (boost) during quiet passages based on desired compression characteristics. 

        :param dynamic_range_compression: The dynamic_range_compression of this DolbyDigitalPreprocessing.
        :type: DolbyDigitalDynamicRangeCompression
        """

        if dynamic_range_compression is not None:
            if not isinstance(dynamic_range_compression, DolbyDigitalDynamicRangeCompression):
                raise TypeError("Invalid type for `dynamic_range_compression`, type has to be `DolbyDigitalDynamicRangeCompression`")

        self._dynamic_range_compression = dynamic_range_compression

    @property
    def lfe_low_pass_filter(self):
        # type: () -> DolbyDigitalLfeLowPassFilter
        """Gets the lfe_low_pass_filter of this DolbyDigitalPreprocessing.

        It applies a 120 Hz low-pass filter to the low-frequency effects (LFE) channel.  This is only allowed if the `channelLayout` contains a LFE channel. 

        :return: The lfe_low_pass_filter of this DolbyDigitalPreprocessing.
        :rtype: DolbyDigitalLfeLowPassFilter
        """
        return self._lfe_low_pass_filter

    @lfe_low_pass_filter.setter
    def lfe_low_pass_filter(self, lfe_low_pass_filter):
        # type: (DolbyDigitalLfeLowPassFilter) -> None
        """Sets the lfe_low_pass_filter of this DolbyDigitalPreprocessing.

        It applies a 120 Hz low-pass filter to the low-frequency effects (LFE) channel.  This is only allowed if the `channelLayout` contains a LFE channel. 

        :param lfe_low_pass_filter: The lfe_low_pass_filter of this DolbyDigitalPreprocessing.
        :type: DolbyDigitalLfeLowPassFilter
        """

        if lfe_low_pass_filter is not None:
            if not isinstance(lfe_low_pass_filter, DolbyDigitalLfeLowPassFilter):
                raise TypeError("Invalid type for `lfe_low_pass_filter`, type has to be `DolbyDigitalLfeLowPassFilter`")

        self._lfe_low_pass_filter = lfe_low_pass_filter

    @property
    def ninety_degree_phase_shift(self):
        # type: () -> DolbyDigitalNinetyDegreePhaseShift
        """Gets the ninety_degree_phase_shift of this DolbyDigitalPreprocessing.


        :return: The ninety_degree_phase_shift of this DolbyDigitalPreprocessing.
        :rtype: DolbyDigitalNinetyDegreePhaseShift
        """
        return self._ninety_degree_phase_shift

    @ninety_degree_phase_shift.setter
    def ninety_degree_phase_shift(self, ninety_degree_phase_shift):
        # type: (DolbyDigitalNinetyDegreePhaseShift) -> None
        """Sets the ninety_degree_phase_shift of this DolbyDigitalPreprocessing.


        :param ninety_degree_phase_shift: The ninety_degree_phase_shift of this DolbyDigitalPreprocessing.
        :type: DolbyDigitalNinetyDegreePhaseShift
        """

        if ninety_degree_phase_shift is not None:
            if not isinstance(ninety_degree_phase_shift, DolbyDigitalNinetyDegreePhaseShift):
                raise TypeError("Invalid type for `ninety_degree_phase_shift`, type has to be `DolbyDigitalNinetyDegreePhaseShift`")

        self._ninety_degree_phase_shift = ninety_degree_phase_shift

    @property
    def three_db_attenuation(self):
        # type: () -> DolbyDigitalThreeDbAttenuation
        """Gets the three_db_attenuation of this DolbyDigitalPreprocessing.


        :return: The three_db_attenuation of this DolbyDigitalPreprocessing.
        :rtype: DolbyDigitalThreeDbAttenuation
        """
        return self._three_db_attenuation

    @three_db_attenuation.setter
    def three_db_attenuation(self, three_db_attenuation):
        # type: (DolbyDigitalThreeDbAttenuation) -> None
        """Sets the three_db_attenuation of this DolbyDigitalPreprocessing.


        :param three_db_attenuation: The three_db_attenuation of this DolbyDigitalPreprocessing.
        :type: DolbyDigitalThreeDbAttenuation
        """

        if three_db_attenuation is not None:
            if not isinstance(three_db_attenuation, DolbyDigitalThreeDbAttenuation):
                raise TypeError("Invalid type for `three_db_attenuation`, type has to be `DolbyDigitalThreeDbAttenuation`")

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
        if not isinstance(other, DolbyDigitalPreprocessing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
