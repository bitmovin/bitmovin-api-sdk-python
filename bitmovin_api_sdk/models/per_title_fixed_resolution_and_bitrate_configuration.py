# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.per_title_fixed_resolution_and_bitrate_configuration_mode import PerTitleFixedResolutionAndBitrateConfigurationMode
import pprint
import six


class PerTitleFixedResolutionAndBitrateConfiguration(object):
    @poscheck_model
    def __init__(self,
                 forced_rendition_above_highest_fixed_representation=None,
                 forced_rendition_above_highest_fixed_representation_factor=None,
                 forced_rendition_above_highest_fixed_representation_calculation_mode=None):
        # type: (int, float, PerTitleFixedResolutionAndBitrateConfigurationMode) -> None

        self._forced_rendition_above_highest_fixed_representation = None
        self._forced_rendition_above_highest_fixed_representation_factor = None
        self._forced_rendition_above_highest_fixed_representation_calculation_mode = None
        self.discriminator = None

        if forced_rendition_above_highest_fixed_representation is not None:
            self.forced_rendition_above_highest_fixed_representation = forced_rendition_above_highest_fixed_representation
        if forced_rendition_above_highest_fixed_representation_factor is not None:
            self.forced_rendition_above_highest_fixed_representation_factor = forced_rendition_above_highest_fixed_representation_factor
        if forced_rendition_above_highest_fixed_representation_calculation_mode is not None:
            self.forced_rendition_above_highest_fixed_representation_calculation_mode = forced_rendition_above_highest_fixed_representation_calculation_mode

    @property
    def openapi_types(self):
        types = {
            'forced_rendition_above_highest_fixed_representation': 'int',
            'forced_rendition_above_highest_fixed_representation_factor': 'float',
            'forced_rendition_above_highest_fixed_representation_calculation_mode': 'PerTitleFixedResolutionAndBitrateConfigurationMode'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'forced_rendition_above_highest_fixed_representation': 'forcedRenditionAboveHighestFixedRepresentation',
            'forced_rendition_above_highest_fixed_representation_factor': 'forcedRenditionAboveHighestFixedRepresentationFactor',
            'forced_rendition_above_highest_fixed_representation_calculation_mode': 'forcedRenditionAboveHighestFixedRepresentationCalculationMode'
        }
        return attributes

    @property
    def forced_rendition_above_highest_fixed_representation(self):
        # type: () -> int
        """Gets the forced_rendition_above_highest_fixed_representation of this PerTitleFixedResolutionAndBitrateConfiguration.

        Number of forced renditions above the highest fixed representation (e.g. FIXED_RESOLUTION_AND_BITRATE). Forced renditions will be added, also if the Per-Title algorithm chooses the user defined force rendition to be the highest one.

        :return: The forced_rendition_above_highest_fixed_representation of this PerTitleFixedResolutionAndBitrateConfiguration.
        :rtype: int
        """
        return self._forced_rendition_above_highest_fixed_representation

    @forced_rendition_above_highest_fixed_representation.setter
    def forced_rendition_above_highest_fixed_representation(self, forced_rendition_above_highest_fixed_representation):
        # type: (int) -> None
        """Sets the forced_rendition_above_highest_fixed_representation of this PerTitleFixedResolutionAndBitrateConfiguration.

        Number of forced renditions above the highest fixed representation (e.g. FIXED_RESOLUTION_AND_BITRATE). Forced renditions will be added, also if the Per-Title algorithm chooses the user defined force rendition to be the highest one.

        :param forced_rendition_above_highest_fixed_representation: The forced_rendition_above_highest_fixed_representation of this PerTitleFixedResolutionAndBitrateConfiguration.
        :type: int
        """

        if forced_rendition_above_highest_fixed_representation is not None:
            if forced_rendition_above_highest_fixed_representation is not None and forced_rendition_above_highest_fixed_representation < 1:
                raise ValueError("Invalid value for `forced_rendition_above_highest_fixed_representation`, must be a value greater than or equal to `1`")
            if not isinstance(forced_rendition_above_highest_fixed_representation, int):
                raise TypeError("Invalid type for `forced_rendition_above_highest_fixed_representation`, type has to be `int`")

        self._forced_rendition_above_highest_fixed_representation = forced_rendition_above_highest_fixed_representation

    @property
    def forced_rendition_above_highest_fixed_representation_factor(self):
        # type: () -> float
        """Gets the forced_rendition_above_highest_fixed_representation_factor of this PerTitleFixedResolutionAndBitrateConfiguration.

        The factor to calculate the bitrate that will be chosen based on the bitrate of the last FIXED_RESOLUTION.

        :return: The forced_rendition_above_highest_fixed_representation_factor of this PerTitleFixedResolutionAndBitrateConfiguration.
        :rtype: float
        """
        return self._forced_rendition_above_highest_fixed_representation_factor

    @forced_rendition_above_highest_fixed_representation_factor.setter
    def forced_rendition_above_highest_fixed_representation_factor(self, forced_rendition_above_highest_fixed_representation_factor):
        # type: (float) -> None
        """Sets the forced_rendition_above_highest_fixed_representation_factor of this PerTitleFixedResolutionAndBitrateConfiguration.

        The factor to calculate the bitrate that will be chosen based on the bitrate of the last FIXED_RESOLUTION.

        :param forced_rendition_above_highest_fixed_representation_factor: The forced_rendition_above_highest_fixed_representation_factor of this PerTitleFixedResolutionAndBitrateConfiguration.
        :type: float
        """

        if forced_rendition_above_highest_fixed_representation_factor is not None:
            if not isinstance(forced_rendition_above_highest_fixed_representation_factor, (float, int)):
                raise TypeError("Invalid type for `forced_rendition_above_highest_fixed_representation_factor`, type has to be `float`")

        self._forced_rendition_above_highest_fixed_representation_factor = forced_rendition_above_highest_fixed_representation_factor

    @property
    def forced_rendition_above_highest_fixed_representation_calculation_mode(self):
        # type: () -> PerTitleFixedResolutionAndBitrateConfigurationMode
        """Gets the forced_rendition_above_highest_fixed_representation_calculation_mode of this PerTitleFixedResolutionAndBitrateConfiguration.

        Mode to calculate the bitrate of the next representation

        :return: The forced_rendition_above_highest_fixed_representation_calculation_mode of this PerTitleFixedResolutionAndBitrateConfiguration.
        :rtype: PerTitleFixedResolutionAndBitrateConfigurationMode
        """
        return self._forced_rendition_above_highest_fixed_representation_calculation_mode

    @forced_rendition_above_highest_fixed_representation_calculation_mode.setter
    def forced_rendition_above_highest_fixed_representation_calculation_mode(self, forced_rendition_above_highest_fixed_representation_calculation_mode):
        # type: (PerTitleFixedResolutionAndBitrateConfigurationMode) -> None
        """Sets the forced_rendition_above_highest_fixed_representation_calculation_mode of this PerTitleFixedResolutionAndBitrateConfiguration.

        Mode to calculate the bitrate of the next representation

        :param forced_rendition_above_highest_fixed_representation_calculation_mode: The forced_rendition_above_highest_fixed_representation_calculation_mode of this PerTitleFixedResolutionAndBitrateConfiguration.
        :type: PerTitleFixedResolutionAndBitrateConfigurationMode
        """

        if forced_rendition_above_highest_fixed_representation_calculation_mode is not None:
            if not isinstance(forced_rendition_above_highest_fixed_representation_calculation_mode, PerTitleFixedResolutionAndBitrateConfigurationMode):
                raise TypeError("Invalid type for `forced_rendition_above_highest_fixed_representation_calculation_mode`, type has to be `PerTitleFixedResolutionAndBitrateConfigurationMode`")

        self._forced_rendition_above_highest_fixed_representation_calculation_mode = forced_rendition_above_highest_fixed_representation_calculation_mode

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
        if not isinstance(other, PerTitleFixedResolutionAndBitrateConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
