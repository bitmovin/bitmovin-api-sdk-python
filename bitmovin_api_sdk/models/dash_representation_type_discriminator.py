# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class DashRepresentationTypeDiscriminator(Enum):
    DRM_FMP4 = "DRM_FMP4"
    FMP4 = "FMP4"
    WEBM = "WEBM"
    CMAF = "CMAF"
    CHUNKED_TEXT = "CHUNKED_TEXT"
    MP4 = "MP4"
    DRM_MP4 = "DRM_MP4"
    PROGRESSIVE_WEBM = "PROGRESSIVE_WEBM"
    VTT = "VTT"
    SPRITE = "SPRITE"
    IMSC = "IMSC"
    CONTENT_PROTECTION = "CONTENT_PROTECTION"
