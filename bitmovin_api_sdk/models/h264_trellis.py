# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class H264Trellis(Enum):
    DISABLED = "DISABLED"
    ENABLED_FINAL_MB = "ENABLED_FINAL_MB"
    ENABLED_ALL = "ENABLED_ALL"
