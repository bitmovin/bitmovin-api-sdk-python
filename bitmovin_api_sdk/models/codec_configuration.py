# coding: utf-8


from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint


class CodecConfiguration(BitmovinResource):

    discriminator_value_class_map = {
        'AAC': 'AacAudioConfiguration',
        'DTS_PASSTHROUGH': 'DtsPassthroughAudioConfiguration',
        'HE_AAC_V1': 'HeAacV1AudioConfiguration',
        'HE_AAC_V2': 'HeAacV2AudioConfiguration',
        'H264': 'H264VideoConfiguration',
        'H265': 'H265VideoConfiguration',
        'VP9': 'Vp9VideoConfiguration',
        'VP8': 'Vp8VideoConfiguration',
        'MP2': 'Mp2AudioConfiguration',
        'MP3': 'Mp3AudioConfiguration',
        'AC3': 'Ac3AudioConfiguration',
        'EAC3': 'Eac3AudioConfiguration',
        'OPUS': 'OpusAudioConfiguration',
        'VORBIS': 'VorbisAudioConfiguration',
        'MJPEG': 'MjpegVideoConfiguration',
        'AV1': 'Av1VideoConfiguration',
        'DOLBY_ATMOS': 'DolbyAtmosAudioConfiguration',
        'H262': 'H262VideoConfiguration',
        'PCM': 'PcmAudioConfiguration',
        'WEBVTT': 'WebVttConfiguration'
    }

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(CodecConfiguration, self), "to_dict"):
            result = super(CodecConfiguration, self).to_dict()
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
        if not isinstance(other, CodecConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
