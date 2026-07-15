# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.h265_v2_perceptual_encoding_mode import H265V2PerceptualEncodingMode
from bitmovin_api_sdk.models.h265_v2_rate_control_mode_config import H265V2RateControlModeConfig
from bitmovin_api_sdk.models.h265_v2_rate_control_mode_config_type import H265V2RateControlModeConfigType
import pprint
import six


class H265V2PerceptualQualityModeConfig(H265V2RateControlModeConfig):
    @poscheck_model
    def __init__(self,
                 type_=None,
                 perceptual_encoding_mode=None,
                 perceptual_strength=None,
                 perceptual_penalty_strength=None,
                 perceptual_penalty_knee=None,
                 perceptual_temporal_strength=None,
                 pixel_per_degree=None):
        # type: (H265V2RateControlModeConfigType, H265V2PerceptualEncodingMode, float, float, float, float, float) -> None
        super(H265V2PerceptualQualityModeConfig, self).__init__(type_=type_)

        self._perceptual_encoding_mode = None
        self._perceptual_strength = None
        self._perceptual_penalty_strength = None
        self._perceptual_penalty_knee = None
        self._perceptual_temporal_strength = None
        self._pixel_per_degree = None
        self.discriminator = None

        if perceptual_encoding_mode is not None:
            self.perceptual_encoding_mode = perceptual_encoding_mode
        if perceptual_strength is not None:
            self.perceptual_strength = perceptual_strength
        if perceptual_penalty_strength is not None:
            self.perceptual_penalty_strength = perceptual_penalty_strength
        if perceptual_penalty_knee is not None:
            self.perceptual_penalty_knee = perceptual_penalty_knee
        if perceptual_temporal_strength is not None:
            self.perceptual_temporal_strength = perceptual_temporal_strength
        if pixel_per_degree is not None:
            self.pixel_per_degree = pixel_per_degree

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(H265V2PerceptualQualityModeConfig, self), 'openapi_types'):
            types = getattr(super(H265V2PerceptualQualityModeConfig, self), 'openapi_types')

        types.update({
            'perceptual_encoding_mode': 'H265V2PerceptualEncodingMode',
            'perceptual_strength': 'float',
            'perceptual_penalty_strength': 'float',
            'perceptual_penalty_knee': 'float',
            'perceptual_temporal_strength': 'float',
            'pixel_per_degree': 'float'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(H265V2PerceptualQualityModeConfig, self), 'attribute_map'):
            attributes = getattr(super(H265V2PerceptualQualityModeConfig, self), 'attribute_map')

        attributes.update({
            'perceptual_encoding_mode': 'perceptualEncodingMode',
            'perceptual_strength': 'perceptualStrength',
            'perceptual_penalty_strength': 'perceptualPenaltyStrength',
            'perceptual_penalty_knee': 'perceptualPenaltyKnee',
            'perceptual_temporal_strength': 'perceptualTemporalStrength',
            'pixel_per_degree': 'pixelPerDegree'
        })
        return attributes

    @property
    def perceptual_encoding_mode(self):
        # type: () -> H265V2PerceptualEncodingMode
        """Gets the perceptual_encoding_mode of this H265V2PerceptualQualityModeConfig.

        HVS-based perceptual encoding mode.

        :return: The perceptual_encoding_mode of this H265V2PerceptualQualityModeConfig.
        :rtype: H265V2PerceptualEncodingMode
        """
        return self._perceptual_encoding_mode

    @perceptual_encoding_mode.setter
    def perceptual_encoding_mode(self, perceptual_encoding_mode):
        # type: (H265V2PerceptualEncodingMode) -> None
        """Sets the perceptual_encoding_mode of this H265V2PerceptualQualityModeConfig.

        HVS-based perceptual encoding mode.

        :param perceptual_encoding_mode: The perceptual_encoding_mode of this H265V2PerceptualQualityModeConfig.
        :type: H265V2PerceptualEncodingMode
        """

        if perceptual_encoding_mode is not None:
            if not isinstance(perceptual_encoding_mode, H265V2PerceptualEncodingMode):
                raise TypeError("Invalid type for `perceptual_encoding_mode`, type has to be `H265V2PerceptualEncodingMode`")

        self._perceptual_encoding_mode = perceptual_encoding_mode

    @property
    def perceptual_strength(self):
        # type: () -> float
        """Gets the perceptual_strength of this H265V2PerceptualQualityModeConfig.

        Overall strength of perceptual model (0.0-1.0).

        :return: The perceptual_strength of this H265V2PerceptualQualityModeConfig.
        :rtype: float
        """
        return self._perceptual_strength

    @perceptual_strength.setter
    def perceptual_strength(self, perceptual_strength):
        # type: (float) -> None
        """Sets the perceptual_strength of this H265V2PerceptualQualityModeConfig.

        Overall strength of perceptual model (0.0-1.0).

        :param perceptual_strength: The perceptual_strength of this H265V2PerceptualQualityModeConfig.
        :type: float
        """

        if perceptual_strength is not None:
            if not isinstance(perceptual_strength, (float, int)):
                raise TypeError("Invalid type for `perceptual_strength`, type has to be `float`")

        self._perceptual_strength = perceptual_strength

    @property
    def perceptual_penalty_strength(self):
        # type: () -> float
        """Gets the perceptual_penalty_strength of this H265V2PerceptualQualityModeConfig.

        Strength of penalties from perceptual model (0.0-1.0).

        :return: The perceptual_penalty_strength of this H265V2PerceptualQualityModeConfig.
        :rtype: float
        """
        return self._perceptual_penalty_strength

    @perceptual_penalty_strength.setter
    def perceptual_penalty_strength(self, perceptual_penalty_strength):
        # type: (float) -> None
        """Sets the perceptual_penalty_strength of this H265V2PerceptualQualityModeConfig.

        Strength of penalties from perceptual model (0.0-1.0).

        :param perceptual_penalty_strength: The perceptual_penalty_strength of this H265V2PerceptualQualityModeConfig.
        :type: float
        """

        if perceptual_penalty_strength is not None:
            if not isinstance(perceptual_penalty_strength, (float, int)):
                raise TypeError("Invalid type for `perceptual_penalty_strength`, type has to be `float`")

        self._perceptual_penalty_strength = perceptual_penalty_strength

    @property
    def perceptual_penalty_knee(self):
        # type: () -> float
        """Gets the perceptual_penalty_knee of this H265V2PerceptualQualityModeConfig.

        Knee point of penalty strength modulation (0.0-1.0).

        :return: The perceptual_penalty_knee of this H265V2PerceptualQualityModeConfig.
        :rtype: float
        """
        return self._perceptual_penalty_knee

    @perceptual_penalty_knee.setter
    def perceptual_penalty_knee(self, perceptual_penalty_knee):
        # type: (float) -> None
        """Sets the perceptual_penalty_knee of this H265V2PerceptualQualityModeConfig.

        Knee point of penalty strength modulation (0.0-1.0).

        :param perceptual_penalty_knee: The perceptual_penalty_knee of this H265V2PerceptualQualityModeConfig.
        :type: float
        """

        if perceptual_penalty_knee is not None:
            if not isinstance(perceptual_penalty_knee, (float, int)):
                raise TypeError("Invalid type for `perceptual_penalty_knee`, type has to be `float`")

        self._perceptual_penalty_knee = perceptual_penalty_knee

    @property
    def perceptual_temporal_strength(self):
        # type: () -> float
        """Gets the perceptual_temporal_strength of this H265V2PerceptualQualityModeConfig.

        Strength of temporal component of perceptual model (0.0-1.0).

        :return: The perceptual_temporal_strength of this H265V2PerceptualQualityModeConfig.
        :rtype: float
        """
        return self._perceptual_temporal_strength

    @perceptual_temporal_strength.setter
    def perceptual_temporal_strength(self, perceptual_temporal_strength):
        # type: (float) -> None
        """Sets the perceptual_temporal_strength of this H265V2PerceptualQualityModeConfig.

        Strength of temporal component of perceptual model (0.0-1.0).

        :param perceptual_temporal_strength: The perceptual_temporal_strength of this H265V2PerceptualQualityModeConfig.
        :type: float
        """

        if perceptual_temporal_strength is not None:
            if not isinstance(perceptual_temporal_strength, (float, int)):
                raise TypeError("Invalid type for `perceptual_temporal_strength`, type has to be `float`")

        self._perceptual_temporal_strength = perceptual_temporal_strength

    @property
    def pixel_per_degree(self):
        # type: () -> float
        """Gets the pixel_per_degree of this H265V2PerceptualQualityModeConfig.

        Pixels per degree (horizontal), i.e. width / FOV.

        :return: The pixel_per_degree of this H265V2PerceptualQualityModeConfig.
        :rtype: float
        """
        return self._pixel_per_degree

    @pixel_per_degree.setter
    def pixel_per_degree(self, pixel_per_degree):
        # type: (float) -> None
        """Sets the pixel_per_degree of this H265V2PerceptualQualityModeConfig.

        Pixels per degree (horizontal), i.e. width / FOV.

        :param pixel_per_degree: The pixel_per_degree of this H265V2PerceptualQualityModeConfig.
        :type: float
        """

        if pixel_per_degree is not None:
            if not isinstance(pixel_per_degree, (float, int)):
                raise TypeError("Invalid type for `pixel_per_degree`, type has to be `float`")

        self._pixel_per_degree = pixel_per_degree

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(H265V2PerceptualQualityModeConfig, self), "to_dict"):
            result = super(H265V2PerceptualQualityModeConfig, self).to_dict()
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
        if not isinstance(other, H265V2PerceptualQualityModeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
