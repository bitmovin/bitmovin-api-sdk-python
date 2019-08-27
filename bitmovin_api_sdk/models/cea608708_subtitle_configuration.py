# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class Cea608708SubtitleConfiguration(object):
    @poscheck_model
    def __init__(self,
                 passthrough_activated=None):
        # type: (bool) -> None

        self._passthrough_activated = None
        self.discriminator = None

        if passthrough_activated is not None:
            self.passthrough_activated = passthrough_activated

    @property
    def openapi_types(self):
        types = {
            'passthrough_activated': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'passthrough_activated': 'passthroughActivated'
        }
        return attributes

    @property
    def passthrough_activated(self):
        # type: () -> bool
        """Gets the passthrough_activated of this Cea608708SubtitleConfiguration.

        If enabled, CEA 608 an CEA 708 subtitles will be copied from the input video stream to the output video stream. Note: This does not work, if the output framerate is different than the input framerate (except doubling the framerate with deinterlacing per field)

        :return: The passthrough_activated of this Cea608708SubtitleConfiguration.
        :rtype: bool
        """
        return self._passthrough_activated

    @passthrough_activated.setter
    def passthrough_activated(self, passthrough_activated):
        # type: (bool) -> None
        """Sets the passthrough_activated of this Cea608708SubtitleConfiguration.

        If enabled, CEA 608 an CEA 708 subtitles will be copied from the input video stream to the output video stream. Note: This does not work, if the output framerate is different than the input framerate (except doubling the framerate with deinterlacing per field)

        :param passthrough_activated: The passthrough_activated of this Cea608708SubtitleConfiguration.
        :type: bool
        """

        if passthrough_activated is not None:
            if not isinstance(passthrough_activated, bool):
                raise TypeError("Invalid type for `passthrough_activated`, type has to be `bool`")

        self._passthrough_activated = passthrough_activated

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
                result[self.attribute_map.get(attr)] = [x.to_dict() if hasattr(x, "to_dict") else x for x in value]
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
        if not isinstance(other, Cea608708SubtitleConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
