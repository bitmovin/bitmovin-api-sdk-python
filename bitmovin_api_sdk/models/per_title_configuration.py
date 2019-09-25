# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.auto_representation import AutoRepresentation
from bitmovin_api_sdk.models.per_title_fixed_resolution_and_bitrate_configuration import PerTitleFixedResolutionAndBitrateConfiguration
import pprint
import six


class PerTitleConfiguration(object):
    @poscheck_model
    def __init__(self,
                 min_bitrate=None,
                 max_bitrate=None,
                 min_bitrate_step_size=None,
                 max_bitrate_step_size=None,
                 auto_representations=None,
                 complexity_factor=None,
                 fixed_resolution_and_bitrate_configuration=None):
        # type: (int, int, float, float, AutoRepresentation, float, PerTitleFixedResolutionAndBitrateConfiguration) -> None

        self._min_bitrate = None
        self._max_bitrate = None
        self._min_bitrate_step_size = None
        self._max_bitrate_step_size = None
        self._auto_representations = None
        self._complexity_factor = None
        self._fixed_resolution_and_bitrate_configuration = None
        self.discriminator = None

        if min_bitrate is not None:
            self.min_bitrate = min_bitrate
        if max_bitrate is not None:
            self.max_bitrate = max_bitrate
        if min_bitrate_step_size is not None:
            self.min_bitrate_step_size = min_bitrate_step_size
        if max_bitrate_step_size is not None:
            self.max_bitrate_step_size = max_bitrate_step_size
        if auto_representations is not None:
            self.auto_representations = auto_representations
        if complexity_factor is not None:
            self.complexity_factor = complexity_factor
        if fixed_resolution_and_bitrate_configuration is not None:
            self.fixed_resolution_and_bitrate_configuration = fixed_resolution_and_bitrate_configuration

    @property
    def openapi_types(self):
        types = {
            'min_bitrate': 'int',
            'max_bitrate': 'int',
            'min_bitrate_step_size': 'float',
            'max_bitrate_step_size': 'float',
            'auto_representations': 'AutoRepresentation',
            'complexity_factor': 'float',
            'fixed_resolution_and_bitrate_configuration': 'PerTitleFixedResolutionAndBitrateConfiguration'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'min_bitrate': 'minBitrate',
            'max_bitrate': 'maxBitrate',
            'min_bitrate_step_size': 'minBitrateStepSize',
            'max_bitrate_step_size': 'maxBitrateStepSize',
            'auto_representations': 'autoRepresentations',
            'complexity_factor': 'complexityFactor',
            'fixed_resolution_and_bitrate_configuration': 'fixedResolutionAndBitrateConfiguration'
        }
        return attributes

    @property
    def min_bitrate(self):
        # type: () -> int
        """Gets the min_bitrate of this PerTitleConfiguration.

        The minimum bitrate that will be used by the Per-Title algorithm.

        :return: The min_bitrate of this PerTitleConfiguration.
        :rtype: int
        """
        return self._min_bitrate

    @min_bitrate.setter
    def min_bitrate(self, min_bitrate):
        # type: (int) -> None
        """Sets the min_bitrate of this PerTitleConfiguration.

        The minimum bitrate that will be used by the Per-Title algorithm.

        :param min_bitrate: The min_bitrate of this PerTitleConfiguration.
        :type: int
        """

        if min_bitrate is not None:
            if not isinstance(min_bitrate, int):
                raise TypeError("Invalid type for `min_bitrate`, type has to be `int`")

        self._min_bitrate = min_bitrate

    @property
    def max_bitrate(self):
        # type: () -> int
        """Gets the max_bitrate of this PerTitleConfiguration.

        The maximum bitrate that will be used by the Per-Title algorithm. It will not generate any rendition with a higher bitrate.

        :return: The max_bitrate of this PerTitleConfiguration.
        :rtype: int
        """
        return self._max_bitrate

    @max_bitrate.setter
    def max_bitrate(self, max_bitrate):
        # type: (int) -> None
        """Sets the max_bitrate of this PerTitleConfiguration.

        The maximum bitrate that will be used by the Per-Title algorithm. It will not generate any rendition with a higher bitrate.

        :param max_bitrate: The max_bitrate of this PerTitleConfiguration.
        :type: int
        """

        if max_bitrate is not None:
            if not isinstance(max_bitrate, int):
                raise TypeError("Invalid type for `max_bitrate`, type has to be `int`")

        self._max_bitrate = max_bitrate

    @property
    def min_bitrate_step_size(self):
        # type: () -> float
        """Gets the min_bitrate_step_size of this PerTitleConfiguration.

        The minimum ratio between the bitrates of generated renditions, e.g. if the first bitrate is 240,000, a minimum ratio of 1.5 will require the next higher bitrate to be at least 360,000

        :return: The min_bitrate_step_size of this PerTitleConfiguration.
        :rtype: float
        """
        return self._min_bitrate_step_size

    @min_bitrate_step_size.setter
    def min_bitrate_step_size(self, min_bitrate_step_size):
        # type: (float) -> None
        """Sets the min_bitrate_step_size of this PerTitleConfiguration.

        The minimum ratio between the bitrates of generated renditions, e.g. if the first bitrate is 240,000, a minimum ratio of 1.5 will require the next higher bitrate to be at least 360,000

        :param min_bitrate_step_size: The min_bitrate_step_size of this PerTitleConfiguration.
        :type: float
        """

        if min_bitrate_step_size is not None:
            if not isinstance(min_bitrate_step_size, (float, int)):
                raise TypeError("Invalid type for `min_bitrate_step_size`, type has to be `float`")

        self._min_bitrate_step_size = min_bitrate_step_size

    @property
    def max_bitrate_step_size(self):
        # type: () -> float
        """Gets the max_bitrate_step_size of this PerTitleConfiguration.

        The maximum ratio between the bitrates of neighbouring renditions, e.g., if the first bitrate is 240,000, a maximum ratio of 1.5 will require the next higher bitrate to be at most 360,000

        :return: The max_bitrate_step_size of this PerTitleConfiguration.
        :rtype: float
        """
        return self._max_bitrate_step_size

    @max_bitrate_step_size.setter
    def max_bitrate_step_size(self, max_bitrate_step_size):
        # type: (float) -> None
        """Sets the max_bitrate_step_size of this PerTitleConfiguration.

        The maximum ratio between the bitrates of neighbouring renditions, e.g., if the first bitrate is 240,000, a maximum ratio of 1.5 will require the next higher bitrate to be at most 360,000

        :param max_bitrate_step_size: The max_bitrate_step_size of this PerTitleConfiguration.
        :type: float
        """

        if max_bitrate_step_size is not None:
            if not isinstance(max_bitrate_step_size, (float, int)):
                raise TypeError("Invalid type for `max_bitrate_step_size`, type has to be `float`")

        self._max_bitrate_step_size = max_bitrate_step_size

    @property
    def auto_representations(self):
        # type: () -> AutoRepresentation
        """Gets the auto_representations of this PerTitleConfiguration.


        :return: The auto_representations of this PerTitleConfiguration.
        :rtype: AutoRepresentation
        """
        return self._auto_representations

    @auto_representations.setter
    def auto_representations(self, auto_representations):
        # type: (AutoRepresentation) -> None
        """Sets the auto_representations of this PerTitleConfiguration.


        :param auto_representations: The auto_representations of this PerTitleConfiguration.
        :type: AutoRepresentation
        """

        if auto_representations is not None:
            if not isinstance(auto_representations, AutoRepresentation):
                raise TypeError("Invalid type for `auto_representations`, type has to be `AutoRepresentation`")

        self._auto_representations = auto_representations

    @property
    def complexity_factor(self):
        # type: () -> float
        """Gets the complexity_factor of this PerTitleConfiguration.

        Will modify the assumed complexity for the Per-Title algorithm (> 0.0). Values higher than 1 will increase complexity and thus select smaller resolutions for given bitrates. This will also result in a higher bitrate for the top rendition. Values lower than 1 will decrease assumed complexity and thus select higher resolutions for given bitrates and also decrease the bitrate of the top rendition

        :return: The complexity_factor of this PerTitleConfiguration.
        :rtype: float
        """
        return self._complexity_factor

    @complexity_factor.setter
    def complexity_factor(self, complexity_factor):
        # type: (float) -> None
        """Sets the complexity_factor of this PerTitleConfiguration.

        Will modify the assumed complexity for the Per-Title algorithm (> 0.0). Values higher than 1 will increase complexity and thus select smaller resolutions for given bitrates. This will also result in a higher bitrate for the top rendition. Values lower than 1 will decrease assumed complexity and thus select higher resolutions for given bitrates and also decrease the bitrate of the top rendition

        :param complexity_factor: The complexity_factor of this PerTitleConfiguration.
        :type: float
        """

        if complexity_factor is not None:
            if complexity_factor is not None and complexity_factor <= 0:
                raise ValueError("Invalid value for `complexity_factor`, must be a value greater than `0`")
            if not isinstance(complexity_factor, (float, int)):
                raise TypeError("Invalid type for `complexity_factor`, type has to be `float`")

        self._complexity_factor = complexity_factor

    @property
    def fixed_resolution_and_bitrate_configuration(self):
        # type: () -> PerTitleFixedResolutionAndBitrateConfiguration
        """Gets the fixed_resolution_and_bitrate_configuration of this PerTitleConfiguration.

        Additional configuration for fixed resolution and bitrate templates

        :return: The fixed_resolution_and_bitrate_configuration of this PerTitleConfiguration.
        :rtype: PerTitleFixedResolutionAndBitrateConfiguration
        """
        return self._fixed_resolution_and_bitrate_configuration

    @fixed_resolution_and_bitrate_configuration.setter
    def fixed_resolution_and_bitrate_configuration(self, fixed_resolution_and_bitrate_configuration):
        # type: (PerTitleFixedResolutionAndBitrateConfiguration) -> None
        """Sets the fixed_resolution_and_bitrate_configuration of this PerTitleConfiguration.

        Additional configuration for fixed resolution and bitrate templates

        :param fixed_resolution_and_bitrate_configuration: The fixed_resolution_and_bitrate_configuration of this PerTitleConfiguration.
        :type: PerTitleFixedResolutionAndBitrateConfiguration
        """

        if fixed_resolution_and_bitrate_configuration is not None:
            if not isinstance(fixed_resolution_and_bitrate_configuration, PerTitleFixedResolutionAndBitrateConfiguration):
                raise TypeError("Invalid type for `fixed_resolution_and_bitrate_configuration`, type has to be `PerTitleFixedResolutionAndBitrateConfiguration`")

        self._fixed_resolution_and_bitrate_configuration = fixed_resolution_and_bitrate_configuration

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
        if not isinstance(other, PerTitleConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
