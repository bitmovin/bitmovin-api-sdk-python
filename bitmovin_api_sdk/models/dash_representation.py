# coding: utf-8


from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint


class DashRepresentation(BitmovinResponse):

    discriminator_value_class_map = {
        'DRM_FMP4': 'DashFmp4DrmRepresentation',
        'FMP4': 'DashFmp4Representation',
        'WEBM': 'DashWebmRepresentation',
        'CMAF': 'DashCmafRepresentation',
        'CHUNKED_TEXT': 'DashChunkedTextRepresentation',
        'MP4': 'DashMp4Representation',
        'DRM_MP4': 'DashMp4DrmRepresentation',
        'PROGRESSIVE_WEBM': 'DashProgressiveWebmRepresentation',
        'VTT': 'DashVttRepresentation',
        'SPRITE': 'SpriteRepresentation',
        'IMSC': 'DashImscRepresentation',
        'CONTENT_PROTECTION': 'ContentProtection'
    }

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DashRepresentation, self), "to_dict"):
            result = super(DashRepresentation, self).to_dict()
        for k, v in iteritems(self.discriminator_value_class_map):
            if v == type(self).__name__:
                result['typeDiscriminator'] = k
                break
        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DashRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
