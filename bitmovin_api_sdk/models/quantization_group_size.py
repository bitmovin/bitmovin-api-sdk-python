# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class QuantizationGroupSize(Enum):
    QGS_8x8 = "QGS_8x8"
    QGS_16x16 = "QGS_16x16"
    QGS_32x32 = "QGS_32x32"
    QGS_64x64 = "QGS_64x64"
