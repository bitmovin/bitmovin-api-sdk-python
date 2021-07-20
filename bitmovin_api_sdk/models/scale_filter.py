# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.filter import Filter
from bitmovin_api_sdk.models.scaling_algorithm import ScalingAlgorithm
import pprint
import six


class ScaleFilter(Filter):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 width=None,
                 height=None,
                 scaling_algorithm=None,
                 sample_aspect_ratio_numerator=None,
                 sample_aspect_ratio_denominator=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, int, ScalingAlgorithm, int, int) -> None
        super(ScaleFilter, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._width = None
        self._height = None
        self._scaling_algorithm = None
        self._sample_aspect_ratio_numerator = None
        self._sample_aspect_ratio_denominator = None
        self.discriminator = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if scaling_algorithm is not None:
            self.scaling_algorithm = scaling_algorithm
        if sample_aspect_ratio_numerator is not None:
            self.sample_aspect_ratio_numerator = sample_aspect_ratio_numerator
        if sample_aspect_ratio_denominator is not None:
            self.sample_aspect_ratio_denominator = sample_aspect_ratio_denominator

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(ScaleFilter, self), 'openapi_types'):
            types = getattr(super(ScaleFilter, self), 'openapi_types')

        types.update({
            'width': 'int',
            'height': 'int',
            'scaling_algorithm': 'ScalingAlgorithm',
            'sample_aspect_ratio_numerator': 'int',
            'sample_aspect_ratio_denominator': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(ScaleFilter, self), 'attribute_map'):
            attributes = getattr(super(ScaleFilter, self), 'attribute_map')

        attributes.update({
            'width': 'width',
            'height': 'height',
            'scaling_algorithm': 'scalingAlgorithm',
            'sample_aspect_ratio_numerator': 'sampleAspectRatioNumerator',
            'sample_aspect_ratio_denominator': 'sampleAspectRatioDenominator'
        })
        return attributes

    @property
    def width(self):
        # type: () -> int
        """Gets the width of this ScaleFilter.

        The width of the output frame in pixels. If not set it will be based on the configured height by maintaining the original aspect ratio. If height is also not set, the original source dimensions will be applied.

        :return: The width of this ScaleFilter.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        # type: (int) -> None
        """Sets the width of this ScaleFilter.

        The width of the output frame in pixels. If not set it will be based on the configured height by maintaining the original aspect ratio. If height is also not set, the original source dimensions will be applied.

        :param width: The width of this ScaleFilter.
        :type: int
        """

        if width is not None:
            if not isinstance(width, int):
                raise TypeError("Invalid type for `width`, type has to be `int`")

        self._width = width

    @property
    def height(self):
        # type: () -> int
        """Gets the height of this ScaleFilter.

        The height of the output frame in pixels. If not set it will be based on the configured width by maintaining the original aspect ratio. If width is also not set, the original source dimensions will be applied.

        :return: The height of this ScaleFilter.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        # type: (int) -> None
        """Sets the height of this ScaleFilter.

        The height of the output frame in pixels. If not set it will be based on the configured width by maintaining the original aspect ratio. If width is also not set, the original source dimensions will be applied.

        :param height: The height of this ScaleFilter.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

        self._height = height

    @property
    def scaling_algorithm(self):
        # type: () -> ScalingAlgorithm
        """Gets the scaling_algorithm of this ScaleFilter.


        :return: The scaling_algorithm of this ScaleFilter.
        :rtype: ScalingAlgorithm
        """
        return self._scaling_algorithm

    @scaling_algorithm.setter
    def scaling_algorithm(self, scaling_algorithm):
        # type: (ScalingAlgorithm) -> None
        """Sets the scaling_algorithm of this ScaleFilter.


        :param scaling_algorithm: The scaling_algorithm of this ScaleFilter.
        :type: ScalingAlgorithm
        """

        if scaling_algorithm is not None:
            if not isinstance(scaling_algorithm, ScalingAlgorithm):
                raise TypeError("Invalid type for `scaling_algorithm`, type has to be `ScalingAlgorithm`")

        self._scaling_algorithm = scaling_algorithm

    @property
    def sample_aspect_ratio_numerator(self):
        # type: () -> int
        """Gets the sample_aspect_ratio_numerator of this ScaleFilter.

        The numerator of the sample aspect ratio (also known as pixel aspect ratio). Must be set if sampleAspectRatioDenominator is set.

        :return: The sample_aspect_ratio_numerator of this ScaleFilter.
        :rtype: int
        """
        return self._sample_aspect_ratio_numerator

    @sample_aspect_ratio_numerator.setter
    def sample_aspect_ratio_numerator(self, sample_aspect_ratio_numerator):
        # type: (int) -> None
        """Sets the sample_aspect_ratio_numerator of this ScaleFilter.

        The numerator of the sample aspect ratio (also known as pixel aspect ratio). Must be set if sampleAspectRatioDenominator is set.

        :param sample_aspect_ratio_numerator: The sample_aspect_ratio_numerator of this ScaleFilter.
        :type: int
        """

        if sample_aspect_ratio_numerator is not None:
            if not isinstance(sample_aspect_ratio_numerator, int):
                raise TypeError("Invalid type for `sample_aspect_ratio_numerator`, type has to be `int`")

        self._sample_aspect_ratio_numerator = sample_aspect_ratio_numerator

    @property
    def sample_aspect_ratio_denominator(self):
        # type: () -> int
        """Gets the sample_aspect_ratio_denominator of this ScaleFilter.

        The denominator of the sample aspect ratio (also known as pixel aspect ratio). Must be set if sampleAspectRatioNumerator is set.

        :return: The sample_aspect_ratio_denominator of this ScaleFilter.
        :rtype: int
        """
        return self._sample_aspect_ratio_denominator

    @sample_aspect_ratio_denominator.setter
    def sample_aspect_ratio_denominator(self, sample_aspect_ratio_denominator):
        # type: (int) -> None
        """Sets the sample_aspect_ratio_denominator of this ScaleFilter.

        The denominator of the sample aspect ratio (also known as pixel aspect ratio). Must be set if sampleAspectRatioNumerator is set.

        :param sample_aspect_ratio_denominator: The sample_aspect_ratio_denominator of this ScaleFilter.
        :type: int
        """

        if sample_aspect_ratio_denominator is not None:
            if not isinstance(sample_aspect_ratio_denominator, int):
                raise TypeError("Invalid type for `sample_aspect_ratio_denominator`, type has to be `int`")

        self._sample_aspect_ratio_denominator = sample_aspect_ratio_denominator

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(ScaleFilter, self), "to_dict"):
            result = super(ScaleFilter, self).to_dict()
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
        if not isinstance(other, ScaleFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
