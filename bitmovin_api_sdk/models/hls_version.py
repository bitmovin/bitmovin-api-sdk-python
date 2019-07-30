# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class HlsVersion(Enum):
    HLS_V3 = "3"
    HLS_V4 = "4"
    HLS_V5 = "5"
    HLS_V6 = "6"
    HLS_V7 = "7"
    HLS_V8 = "8"
