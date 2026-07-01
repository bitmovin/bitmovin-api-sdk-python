# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.h265_v2_rate_control_mode_config import H265V2RateControlModeConfig
from bitmovin_api_sdk.models.h265_v2_rate_control_mode_config_type import H265V2RateControlModeConfigType
import pprint
import six


class H265V2PerceptualQualityModeConfig(H265V2RateControlModeConfig):
    @poscheck_model
    def __init__(self,
                 type_=None,
                 percept=None,
                 perc_str=None,
                 perc_penalty_str=None,
                 perc_penalty_knee=None,
                 perc_temporal_str=None,
                 pixel_per_degree=None):
        # type: (H265V2RateControlModeConfigType, int, float, float, float, float, float) -> None
        super(H265V2PerceptualQualityModeConfig, self).__init__(type_=type_)

        self._percept = None
        self._perc_str = None
        self._perc_penalty_str = None
        self._perc_penalty_knee = None
        self._perc_temporal_str = None
        self._pixel_per_degree = None
        self.discriminator = None

        if percept is not None:
            self.percept = percept
        if perc_str is not None:
            self.perc_str = perc_str
        if perc_penalty_str is not None:
            self.perc_penalty_str = perc_penalty_str
        if perc_penalty_knee is not None:
            self.perc_penalty_knee = perc_penalty_knee
        if perc_temporal_str is not None:
            self.perc_temporal_str = perc_temporal_str
        if pixel_per_degree is not None:
            self.pixel_per_degree = pixel_per_degree

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(H265V2PerceptualQualityModeConfig, self), 'openapi_types'):
            types = getattr(super(H265V2PerceptualQualityModeConfig, self), 'openapi_types')

        types.update({
            'percept': 'int',
            'perc_str': 'float',
            'perc_penalty_str': 'float',
            'perc_penalty_knee': 'float',
            'perc_temporal_str': 'float',
            'pixel_per_degree': 'float'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(H265V2PerceptualQualityModeConfig, self), 'attribute_map'):
            attributes = getattr(super(H265V2PerceptualQualityModeConfig, self), 'attribute_map')

        attributes.update({
            'percept': 'percept',
            'perc_str': 'percStr',
            'perc_penalty_str': 'percPenaltyStr',
            'perc_penalty_knee': 'percPenaltyKnee',
            'perc_temporal_str': 'percTemporalStr',
            'pixel_per_degree': 'pixelPerDegree'
        })
        return attributes

    @property
    def percept(self):
        # type: () -> int
        """Gets the percept of this H265V2PerceptualQualityModeConfig.

        HVS-based perceptual encoding mode (0:off 1:cudqp 2:+quant).

        :return: The percept of this H265V2PerceptualQualityModeConfig.
        :rtype: int
        """
        return self._percept

    @percept.setter
    def percept(self, percept):
        # type: (int) -> None
        """Sets the percept of this H265V2PerceptualQualityModeConfig.

        HVS-based perceptual encoding mode (0:off 1:cudqp 2:+quant).

        :param percept: The percept of this H265V2PerceptualQualityModeConfig.
        :type: int
        """

        if percept is not None:
            if not isinstance(percept, int):
                raise TypeError("Invalid type for `percept`, type has to be `int`")

        self._percept = percept

    @property
    def perc_str(self):
        # type: () -> float
        """Gets the perc_str of this H265V2PerceptualQualityModeConfig.

        Overall strength of perceptual model (0.0-1.0).

        :return: The perc_str of this H265V2PerceptualQualityModeConfig.
        :rtype: float
        """
        return self._perc_str

    @perc_str.setter
    def perc_str(self, perc_str):
        # type: (float) -> None
        """Sets the perc_str of this H265V2PerceptualQualityModeConfig.

        Overall strength of perceptual model (0.0-1.0).

        :param perc_str: The perc_str of this H265V2PerceptualQualityModeConfig.
        :type: float
        """

        if perc_str is not None:
            if not isinstance(perc_str, (float, int)):
                raise TypeError("Invalid type for `perc_str`, type has to be `float`")

        self._perc_str = perc_str

    @property
    def perc_penalty_str(self):
        # type: () -> float
        """Gets the perc_penalty_str of this H265V2PerceptualQualityModeConfig.

        Strength of penalties from perceptual model (0.0-1.0).

        :return: The perc_penalty_str of this H265V2PerceptualQualityModeConfig.
        :rtype: float
        """
        return self._perc_penalty_str

    @perc_penalty_str.setter
    def perc_penalty_str(self, perc_penalty_str):
        # type: (float) -> None
        """Sets the perc_penalty_str of this H265V2PerceptualQualityModeConfig.

        Strength of penalties from perceptual model (0.0-1.0).

        :param perc_penalty_str: The perc_penalty_str of this H265V2PerceptualQualityModeConfig.
        :type: float
        """

        if perc_penalty_str is not None:
            if not isinstance(perc_penalty_str, (float, int)):
                raise TypeError("Invalid type for `perc_penalty_str`, type has to be `float`")

        self._perc_penalty_str = perc_penalty_str

    @property
    def perc_penalty_knee(self):
        # type: () -> float
        """Gets the perc_penalty_knee of this H265V2PerceptualQualityModeConfig.

        Knee point of penalty strength modulation (0.0-1.0).

        :return: The perc_penalty_knee of this H265V2PerceptualQualityModeConfig.
        :rtype: float
        """
        return self._perc_penalty_knee

    @perc_penalty_knee.setter
    def perc_penalty_knee(self, perc_penalty_knee):
        # type: (float) -> None
        """Sets the perc_penalty_knee of this H265V2PerceptualQualityModeConfig.

        Knee point of penalty strength modulation (0.0-1.0).

        :param perc_penalty_knee: The perc_penalty_knee of this H265V2PerceptualQualityModeConfig.
        :type: float
        """

        if perc_penalty_knee is not None:
            if not isinstance(perc_penalty_knee, (float, int)):
                raise TypeError("Invalid type for `perc_penalty_knee`, type has to be `float`")

        self._perc_penalty_knee = perc_penalty_knee

    @property
    def perc_temporal_str(self):
        # type: () -> float
        """Gets the perc_temporal_str of this H265V2PerceptualQualityModeConfig.

        Strength of temporal component of perceptual model (0.0-1.0).

        :return: The perc_temporal_str of this H265V2PerceptualQualityModeConfig.
        :rtype: float
        """
        return self._perc_temporal_str

    @perc_temporal_str.setter
    def perc_temporal_str(self, perc_temporal_str):
        # type: (float) -> None
        """Sets the perc_temporal_str of this H265V2PerceptualQualityModeConfig.

        Strength of temporal component of perceptual model (0.0-1.0).

        :param perc_temporal_str: The perc_temporal_str of this H265V2PerceptualQualityModeConfig.
        :type: float
        """

        if perc_temporal_str is not None:
            if not isinstance(perc_temporal_str, (float, int)):
                raise TypeError("Invalid type for `perc_temporal_str`, type has to be `float`")

        self._perc_temporal_str = perc_temporal_str

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
