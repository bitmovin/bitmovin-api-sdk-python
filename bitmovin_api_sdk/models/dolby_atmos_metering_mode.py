# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class DolbyAtmosMeteringMode(Enum):
    ITU_R_BS_1770_1 = "ITU-R BS.1770-1"
    ITU_R_BS_1770_2 = "ITU-R BS.1770-2"
    ITU_R_BS_1770_3 = "ITU-R BS.1770-3"
    ITU_R_BS_1770_4 = "ITU-R BS.1770-4"
    LEQ_A = "Leq (A)"
