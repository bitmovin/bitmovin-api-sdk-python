# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AutoRepresentation(object):
    @poscheck_model
    def __init__(self,
                 adopt_configuration_threshold=None):
        # type: (float) -> None

        self._adopt_configuration_threshold = None
        self.discriminator = None

        if adopt_configuration_threshold is not None:
            self.adopt_configuration_threshold = adopt_configuration_threshold

    @property
    def openapi_types(self):
        types = {
            'adopt_configuration_threshold': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'adopt_configuration_threshold': 'adoptConfigurationThreshold'
        }
        return attributes

    @property
    def adopt_configuration_threshold(self):
        # type: () -> float
        """Gets the adopt_configuration_threshold of this AutoRepresentation.

        This is the threshold that determines whether the settings of the lower or the upper template representation (codec configuration) should be used, when representations are added automatically. The value must be between 0 and 1. Values nearer 0 will favour the higher representation, values nearer 1 will favour the lower representation.

        :return: The adopt_configuration_threshold of this AutoRepresentation.
        :rtype: float
        """
        return self._adopt_configuration_threshold

    @adopt_configuration_threshold.setter
    def adopt_configuration_threshold(self, adopt_configuration_threshold):
        # type: (float) -> None
        """Sets the adopt_configuration_threshold of this AutoRepresentation.

        This is the threshold that determines whether the settings of the lower or the upper template representation (codec configuration) should be used, when representations are added automatically. The value must be between 0 and 1. Values nearer 0 will favour the higher representation, values nearer 1 will favour the lower representation.

        :param adopt_configuration_threshold: The adopt_configuration_threshold of this AutoRepresentation.
        :type: float
        """

        if adopt_configuration_threshold is not None:
            if not isinstance(adopt_configuration_threshold, (float, int)):
                raise TypeError("Invalid type for `adopt_configuration_threshold`, type has to be `float`")

        self._adopt_configuration_threshold = adopt_configuration_threshold

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
        if not isinstance(other, AutoRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
