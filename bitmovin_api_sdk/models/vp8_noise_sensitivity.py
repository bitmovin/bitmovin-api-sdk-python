# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class Vp8NoiseSensitivity(Enum):
    OFF = "OFF"
    ON_Y_ONLY = "ON_Y_ONLY"
    ON_YUV = "ON_YUV"
    ON_YUV_AGGRESSIVE = "ON_YUV_AGGRESSIVE"
    ADAPTIVE = "ADAPTIVE"
