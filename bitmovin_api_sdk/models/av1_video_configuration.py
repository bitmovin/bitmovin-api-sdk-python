# coding: utf-8


from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.color_config import ColorConfig
from bitmovin_api_sdk.models.display_aspect_ratio import DisplayAspectRatio
from bitmovin_api_sdk.models.encoding_mode import EncodingMode
from bitmovin_api_sdk.models.pixel_format import PixelFormat
from bitmovin_api_sdk.models.video_configuration import VideoConfiguration
import pprint


class Av1VideoConfiguration(VideoConfiguration):

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Av1VideoConfiguration, self), "to_dict"):
            result = super(Av1VideoConfiguration, self).to_dict()
        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Av1VideoConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
