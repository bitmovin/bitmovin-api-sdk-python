# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.web_vtt_styling_mode import WebVttStylingMode
import pprint
import six


class WebVttStyling(object):
    @poscheck_model
    def __init__(self,
                 mode=None):
        # type: (WebVttStylingMode) -> None

        self._mode = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode

    @property
    def openapi_types(self):
        types = {
            'mode': 'WebVttStylingMode'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'mode': 'mode'
        }
        return attributes

    @property
    def mode(self):
        # type: () -> WebVttStylingMode
        """Gets the mode of this WebVttStyling.


        :return: The mode of this WebVttStyling.
        :rtype: WebVttStylingMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        # type: (WebVttStylingMode) -> None
        """Sets the mode of this WebVttStyling.


        :param mode: The mode of this WebVttStyling.
        :type: WebVttStylingMode
        """

        if mode is not None:
            if not isinstance(mode, WebVttStylingMode):
                raise TypeError("Invalid type for `mode`, type has to be `WebVttStylingMode`")

        self._mode = mode

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
        if not isinstance(other, WebVttStyling):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
