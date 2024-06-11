# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class FilterType(Enum):
    CROP = "CROP"
    CONFORM = "CONFORM"
    WATERMARK = "WATERMARK"
    ENHANCED_WATERMARK = "ENHANCED_WATERMARK"
    ROTATE = "ROTATE"
    DEINTERLACE = "DEINTERLACE"
    ENHANCED_DEINTERLACE = "ENHANCED_DEINTERLACE"
    AUDIO_MIX = "AUDIO_MIX"
    DENOISE_HQDN3D = "DENOISE_HQDN3D"
    TEXT = "TEXT"
    UNSHARP = "UNSHARP"
    SCALE = "SCALE"
    INTERLACE = "INTERLACE"
    AUDIO_VOLUME = "AUDIO_VOLUME"
    EBU_R128_SINGLE_PASS = "EBU_R128_SINGLE_PASS"
    AZURE_SPEECH_TO_CAPTIONS = "AZURE_SPEECH_TO_CAPTIONS"
