# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class MinCodingUnitSize(Enum):
    MCU_8x8 = "MCU_8x8"
    MCU_16x16 = "MCU_16x16"
    MCU_32x32 = "MCU_32x32"
