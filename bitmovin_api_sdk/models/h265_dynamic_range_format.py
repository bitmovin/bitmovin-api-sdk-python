# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class H265DynamicRangeFormat(Enum):
    DOLBY_VISION = "DOLBY_VISION"
    HDR10 = "HDR10"
    HLG = "HLG"
    SDR = "SDR"
