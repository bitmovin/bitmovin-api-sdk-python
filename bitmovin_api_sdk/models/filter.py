# coding: utf-8


from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint


class Filter(BitmovinResource):

    discriminator_value_class_map = {
        'CROP': 'CropFilter',
        'CONFORM': 'ConformFilter',
        'WATERMARK': 'WatermarkFilter',
        'ENHANCED_WATERMARK': 'EnhancedWatermarkFilter',
        'ROTATE': 'RotateFilter',
        'DEINTERLACE': 'DeinterlaceFilter',
        'ENHANCED_DEINTERLACE': 'EnhancedDeinterlaceFilter',
        'AUDIO_MIX': 'AudioMixFilter',
        'DENOISE_HQDN3D': 'DenoiseHqdn3dFilter',
        'TEXT': 'TextFilter',
        'UNSHARP': 'UnsharpFilter',
        'SCALE': 'ScaleFilter',
        'INTERLACE': 'InterlaceFilter',
        'AUDIO_VOLUME': 'AudioVolumeFilter',
        'EBU_R128_SINGLE_PASS': 'EbuR128SinglePassFilter'
    }

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Filter, self), "to_dict"):
            result = super(Filter, self).to_dict()
        for k, v in iteritems(self.discriminator_value_class_map):
            if v == type(self).__name__:
                result['type'] = k
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
        if not isinstance(other, Filter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
