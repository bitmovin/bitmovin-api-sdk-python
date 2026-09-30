# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class Av1DynamicRangeFormat(Enum):
    DOLBY_VISION_PROFILE_10_0 = "DOLBY_VISION_PROFILE_10_0"
    DOLBY_VISION_PROFILE_10_1 = "DOLBY_VISION_PROFILE_10_1"
    HDR10 = "HDR10"
    SDR = "SDR"
