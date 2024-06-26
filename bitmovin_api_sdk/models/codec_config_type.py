# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class CodecConfigType(Enum):
    AAC = "AAC"
    DTS = "DTS"
    DTSX = "DTSX"
    DTS_PASSTHROUGH = "DTS_PASSTHROUGH"
    AUDIO_PASSTHROUGH = "AUDIO_PASSTHROUGH"
    HE_AAC_V1 = "HE_AAC_V1"
    HE_AAC_V2 = "HE_AAC_V2"
    H264 = "H264"
    H265 = "H265"
    VP9 = "VP9"
    VP8 = "VP8"
    MP2 = "MP2"
    MP3 = "MP3"
    AC3 = "AC3"
    EAC3 = "EAC3"
    DD = "DD"
    DDPLUS = "DDPLUS"
    OPUS = "OPUS"
    VORBIS = "VORBIS"
    MJPEG = "MJPEG"
    AV1 = "AV1"
    DOLBY_ATMOS = "DOLBY_ATMOS"
    H262 = "H262"
    PCM = "PCM"
    WEBVTT = "WEBVTT"
    IMSC = "IMSC"
    DVB_SUBTITLE = "DVB_SUBTITLE"
