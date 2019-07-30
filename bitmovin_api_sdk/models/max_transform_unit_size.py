# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class MaxTransformUnitSize(Enum):
    MTU_4x4 = "MTU_4x4"
    MTU_8x8 = "MTU_8x8"
    MTU_16x16 = "MTU_16x16"
    MTU_32x32 = "MTU_32x32"
