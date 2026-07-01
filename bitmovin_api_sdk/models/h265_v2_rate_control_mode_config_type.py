# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class H265V2RateControlModeConfigType(Enum):
    PERCEPTUAL_QUALITY_MODE = "PERCEPTUAL_QUALITY_MODE"
    CONSTANT_BITRATE_MODE = "CONSTANT_BITRATE_MODE"
