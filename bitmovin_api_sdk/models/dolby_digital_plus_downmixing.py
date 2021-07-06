# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dolby_digital_plus_center_mix_level import DolbyDigitalPlusCenterMixLevel
from bitmovin_api_sdk.models.dolby_digital_plus_downmixing_preferred_mode import DolbyDigitalPlusDownmixingPreferredMode
from bitmovin_api_sdk.models.dolby_digital_plus_surround_mix_level import DolbyDigitalPlusSurroundMixLevel
import pprint
import six


class DolbyDigitalPlusDownmixing(object):
    @poscheck_model
    def __init__(self,
                 lo_ro_center_mix_level=None,
                 lt_rt_center_mix_level=None,
                 lo_ro_surround_mix_level=None,
                 lt_rt_surround_mix_level=None,
                 preferred_mode=None):
        # type: (DolbyDigitalPlusCenterMixLevel, DolbyDigitalPlusCenterMixLevel, DolbyDigitalPlusSurroundMixLevel, DolbyDigitalPlusSurroundMixLevel, DolbyDigitalPlusDownmixingPreferredMode) -> None

        self._lo_ro_center_mix_level = None
        self._lt_rt_center_mix_level = None
        self._lo_ro_surround_mix_level = None
        self._lt_rt_surround_mix_level = None
        self._preferred_mode = None
        self.discriminator = None

        if lo_ro_center_mix_level is not None:
            self.lo_ro_center_mix_level = lo_ro_center_mix_level
        if lt_rt_center_mix_level is not None:
            self.lt_rt_center_mix_level = lt_rt_center_mix_level
        if lo_ro_surround_mix_level is not None:
            self.lo_ro_surround_mix_level = lo_ro_surround_mix_level
        if lt_rt_surround_mix_level is not None:
            self.lt_rt_surround_mix_level = lt_rt_surround_mix_level
        if preferred_mode is not None:
            self.preferred_mode = preferred_mode

    @property
    def openapi_types(self):
        types = {
            'lo_ro_center_mix_level': 'DolbyDigitalPlusCenterMixLevel',
            'lt_rt_center_mix_level': 'DolbyDigitalPlusCenterMixLevel',
            'lo_ro_surround_mix_level': 'DolbyDigitalPlusSurroundMixLevel',
            'lt_rt_surround_mix_level': 'DolbyDigitalPlusSurroundMixLevel',
            'preferred_mode': 'DolbyDigitalPlusDownmixingPreferredMode'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'lo_ro_center_mix_level': 'loRoCenterMixLevel',
            'lt_rt_center_mix_level': 'ltRtCenterMixLevel',
            'lo_ro_surround_mix_level': 'loRoSurroundMixLevel',
            'lt_rt_surround_mix_level': 'ltRtSurroundMixLevel',
            'preferred_mode': 'preferredMode'
        }
        return attributes

    @property
    def lo_ro_center_mix_level(self):
        # type: () -> DolbyDigitalPlusCenterMixLevel
        """Gets the lo_ro_center_mix_level of this DolbyDigitalPlusDownmixing.

        The level shift applied to the C channel when adding to the L and R outputs as a result of downmixing to one Lo/Ro output.

        :return: The lo_ro_center_mix_level of this DolbyDigitalPlusDownmixing.
        :rtype: DolbyDigitalPlusCenterMixLevel
        """
        return self._lo_ro_center_mix_level

    @lo_ro_center_mix_level.setter
    def lo_ro_center_mix_level(self, lo_ro_center_mix_level):
        # type: (DolbyDigitalPlusCenterMixLevel) -> None
        """Sets the lo_ro_center_mix_level of this DolbyDigitalPlusDownmixing.

        The level shift applied to the C channel when adding to the L and R outputs as a result of downmixing to one Lo/Ro output.

        :param lo_ro_center_mix_level: The lo_ro_center_mix_level of this DolbyDigitalPlusDownmixing.
        :type: DolbyDigitalPlusCenterMixLevel
        """

        if lo_ro_center_mix_level is not None:
            if not isinstance(lo_ro_center_mix_level, DolbyDigitalPlusCenterMixLevel):
                raise TypeError("Invalid type for `lo_ro_center_mix_level`, type has to be `DolbyDigitalPlusCenterMixLevel`")

        self._lo_ro_center_mix_level = lo_ro_center_mix_level

    @property
    def lt_rt_center_mix_level(self):
        # type: () -> DolbyDigitalPlusCenterMixLevel
        """Gets the lt_rt_center_mix_level of this DolbyDigitalPlusDownmixing.

        The level shift applied to the C channel when adding to the L and R outputs as a result of downmixing to one Lt/Rt output.

        :return: The lt_rt_center_mix_level of this DolbyDigitalPlusDownmixing.
        :rtype: DolbyDigitalPlusCenterMixLevel
        """
        return self._lt_rt_center_mix_level

    @lt_rt_center_mix_level.setter
    def lt_rt_center_mix_level(self, lt_rt_center_mix_level):
        # type: (DolbyDigitalPlusCenterMixLevel) -> None
        """Sets the lt_rt_center_mix_level of this DolbyDigitalPlusDownmixing.

        The level shift applied to the C channel when adding to the L and R outputs as a result of downmixing to one Lt/Rt output.

        :param lt_rt_center_mix_level: The lt_rt_center_mix_level of this DolbyDigitalPlusDownmixing.
        :type: DolbyDigitalPlusCenterMixLevel
        """

        if lt_rt_center_mix_level is not None:
            if not isinstance(lt_rt_center_mix_level, DolbyDigitalPlusCenterMixLevel):
                raise TypeError("Invalid type for `lt_rt_center_mix_level`, type has to be `DolbyDigitalPlusCenterMixLevel`")

        self._lt_rt_center_mix_level = lt_rt_center_mix_level

    @property
    def lo_ro_surround_mix_level(self):
        # type: () -> DolbyDigitalPlusSurroundMixLevel
        """Gets the lo_ro_surround_mix_level of this DolbyDigitalPlusDownmixing.

        The level shift applied to the surround channels when downmixing to one Lo/Ro output.

        :return: The lo_ro_surround_mix_level of this DolbyDigitalPlusDownmixing.
        :rtype: DolbyDigitalPlusSurroundMixLevel
        """
        return self._lo_ro_surround_mix_level

    @lo_ro_surround_mix_level.setter
    def lo_ro_surround_mix_level(self, lo_ro_surround_mix_level):
        # type: (DolbyDigitalPlusSurroundMixLevel) -> None
        """Sets the lo_ro_surround_mix_level of this DolbyDigitalPlusDownmixing.

        The level shift applied to the surround channels when downmixing to one Lo/Ro output.

        :param lo_ro_surround_mix_level: The lo_ro_surround_mix_level of this DolbyDigitalPlusDownmixing.
        :type: DolbyDigitalPlusSurroundMixLevel
        """

        if lo_ro_surround_mix_level is not None:
            if not isinstance(lo_ro_surround_mix_level, DolbyDigitalPlusSurroundMixLevel):
                raise TypeError("Invalid type for `lo_ro_surround_mix_level`, type has to be `DolbyDigitalPlusSurroundMixLevel`")

        self._lo_ro_surround_mix_level = lo_ro_surround_mix_level

    @property
    def lt_rt_surround_mix_level(self):
        # type: () -> DolbyDigitalPlusSurroundMixLevel
        """Gets the lt_rt_surround_mix_level of this DolbyDigitalPlusDownmixing.

        The level shift applied to the surround channels when downmixing to one Lt/Rt output.

        :return: The lt_rt_surround_mix_level of this DolbyDigitalPlusDownmixing.
        :rtype: DolbyDigitalPlusSurroundMixLevel
        """
        return self._lt_rt_surround_mix_level

    @lt_rt_surround_mix_level.setter
    def lt_rt_surround_mix_level(self, lt_rt_surround_mix_level):
        # type: (DolbyDigitalPlusSurroundMixLevel) -> None
        """Sets the lt_rt_surround_mix_level of this DolbyDigitalPlusDownmixing.

        The level shift applied to the surround channels when downmixing to one Lt/Rt output.

        :param lt_rt_surround_mix_level: The lt_rt_surround_mix_level of this DolbyDigitalPlusDownmixing.
        :type: DolbyDigitalPlusSurroundMixLevel
        """

        if lt_rt_surround_mix_level is not None:
            if not isinstance(lt_rt_surround_mix_level, DolbyDigitalPlusSurroundMixLevel):
                raise TypeError("Invalid type for `lt_rt_surround_mix_level`, type has to be `DolbyDigitalPlusSurroundMixLevel`")

        self._lt_rt_surround_mix_level = lt_rt_surround_mix_level

    @property
    def preferred_mode(self):
        # type: () -> DolbyDigitalPlusDownmixingPreferredMode
        """Gets the preferred_mode of this DolbyDigitalPlusDownmixing.


        :return: The preferred_mode of this DolbyDigitalPlusDownmixing.
        :rtype: DolbyDigitalPlusDownmixingPreferredMode
        """
        return self._preferred_mode

    @preferred_mode.setter
    def preferred_mode(self, preferred_mode):
        # type: (DolbyDigitalPlusDownmixingPreferredMode) -> None
        """Sets the preferred_mode of this DolbyDigitalPlusDownmixing.


        :param preferred_mode: The preferred_mode of this DolbyDigitalPlusDownmixing.
        :type: DolbyDigitalPlusDownmixingPreferredMode
        """

        if preferred_mode is not None:
            if not isinstance(preferred_mode, DolbyDigitalPlusDownmixingPreferredMode):
                raise TypeError("Invalid type for `preferred_mode`, type has to be `DolbyDigitalPlusDownmixingPreferredMode`")

        self._preferred_mode = preferred_mode

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
        if not isinstance(other, DolbyDigitalPlusDownmixing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
