# coding: utf-8


from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint


class InputStream(BitmovinResource):

    discriminator_value_class_map = {
        'INGEST': 'IngestInputStream',
        'CONCATENATION': 'ConcatenationInputStream',
        'TRIMMING_TIME_BASED': 'TimeBasedTrimmingInputStream',
        'TRIMMING_TIME_CODE_TRACK': 'TimecodeTrackTrimmingInputStream',
        'TRIMMING_H264_PICTURE_TIMING': 'H264PictureTimingTrimmingInputStream',
        'AUDIO_MIX': 'AudioMixInputStream',
        'SIDECAR_DOLBY_VISION_METADATA': 'DolbyVisionMetadataIngestInputStream',
        'CAPTION_CEA608': 'Cea608CaptionInputStream',
        'CAPTION_CEA708': 'Cea708CaptionInputStream',
        'FILE': 'FileInputStream',
        'DVB_SUBTITLE': 'DvbSubtitleInputStream',
        'DVB_TELETEXT': 'DvbTeletextInputStream',
        'DOLBY_ATMOS': 'DolbyAtmosIngestInputStream'
    }

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(InputStream, self), "to_dict"):
            result = super(InputStream, self).to_dict()
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
        if not isinstance(other, InputStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
