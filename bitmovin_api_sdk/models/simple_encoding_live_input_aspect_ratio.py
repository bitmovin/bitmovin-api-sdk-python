# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class SimpleEncodingLiveInputAspectRatio(Enum):
    WIDE_16_9 = "WIDE_16_9"
    WIDE_16_10 = "WIDE_16_10"
    VERTICAL_9_16 = "VERTICAL_9_16"
    STANDARD_4_3 = "STANDARD_4_3"
    ULTRA_WIDE_21_9 = "ULTRA_WIDE_21_9"
