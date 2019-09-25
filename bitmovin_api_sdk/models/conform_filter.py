# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.filter import Filter
import pprint
import six


class ConformFilter(Filter):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 target_fps=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, float) -> None
        super(ConformFilter, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_)

        self._target_fps = None
        self.discriminator = None

        if target_fps is not None:
            self.target_fps = target_fps

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(ConformFilter, self), 'openapi_types'):
            types = getattr(super(ConformFilter, self), 'openapi_types')

        types.update({
            'target_fps': 'float'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(ConformFilter, self), 'attribute_map'):
            attributes = getattr(super(ConformFilter, self), 'attribute_map')

        attributes.update({
            'target_fps': 'targetFps'
        })
        return attributes

    @property
    def target_fps(self):
        # type: () -> float
        """Gets the target_fps of this ConformFilter.

        The FPS the input should be changed to.

        :return: The target_fps of this ConformFilter.
        :rtype: float
        """
        return self._target_fps

    @target_fps.setter
    def target_fps(self, target_fps):
        # type: (float) -> None
        """Sets the target_fps of this ConformFilter.

        The FPS the input should be changed to.

        :param target_fps: The target_fps of this ConformFilter.
        :type: float
        """

        if target_fps is not None:
            if not isinstance(target_fps, (float, int)):
                raise TypeError("Invalid type for `target_fps`, type has to be `float`")

        self._target_fps = target_fps

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(ConformFilter, self), "to_dict"):
            result = super(ConformFilter, self).to_dict()
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
        if not isinstance(other, ConformFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
