# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class DolbyVisionProfile(Enum):
    DVHE_04 = "DVHE_04"
    DVHE_05 = "DVHE_05"
    DVHE_07 = "DVHE_07"
    HEV1_08 = "HEV1_08"
    AVC3_09 = "AVC3_09"
