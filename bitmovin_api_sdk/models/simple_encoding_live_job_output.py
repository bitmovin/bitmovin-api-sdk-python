# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.simple_encoding_live_max_resolution import SimpleEncodingLiveMaxResolution
import pprint
import six


class SimpleEncodingLiveJobOutput(object):
    @poscheck_model
    def __init__(self,
                 max_resolution=None):
        # type: (SimpleEncodingLiveMaxResolution) -> None

        self._max_resolution = None
        self.discriminator = 'type'

        if max_resolution is not None:
            self.max_resolution = max_resolution

    @property
    def openapi_types(self):
        types = {
            'max_resolution': 'SimpleEncodingLiveMaxResolution'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'max_resolution': 'maxResolution'
        }
        return attributes

    discriminator_value_class_map = {
        'URL': 'SimpleEncodingLiveJobUrlOutput',
        'CDN': 'SimpleEncodingLiveJobCdnOutput'
    }

    @property
    def max_resolution(self):
        # type: () -> SimpleEncodingLiveMaxResolution
        """Gets the max_resolution of this SimpleEncodingLiveJobOutput.

        The maximum output resolution to be generated

        :return: The max_resolution of this SimpleEncodingLiveJobOutput.
        :rtype: SimpleEncodingLiveMaxResolution
        """
        return self._max_resolution

    @max_resolution.setter
    def max_resolution(self, max_resolution):
        # type: (SimpleEncodingLiveMaxResolution) -> None
        """Sets the max_resolution of this SimpleEncodingLiveJobOutput.

        The maximum output resolution to be generated

        :param max_resolution: The max_resolution of this SimpleEncodingLiveJobOutput.
        :type: SimpleEncodingLiveMaxResolution
        """

        if max_resolution is not None:
            if not isinstance(max_resolution, SimpleEncodingLiveMaxResolution):
                raise TypeError("Invalid type for `max_resolution`, type has to be `SimpleEncodingLiveMaxResolution`")

        self._max_resolution = max_resolution

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for k, v in iteritems(self.discriminator_value_class_map):
            if v == type(self).__name__:
                result['type'] = k
                break
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
        if not isinstance(other, SimpleEncodingLiveJobOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
