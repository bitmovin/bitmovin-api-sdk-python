# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class ScalingAlgorithm(Enum):
    FAST_BILINEAR = "FAST_BILINEAR"
    BILINEAR = "BILINEAR"
    BICUBIC = "BICUBIC"
    EXPERIMENTAL = "EXPERIMENTAL"
    NEAREST_NEIGHBOR = "NEAREST_NEIGHBOR"
    AVERAGING_AREA = "AVERAGING_AREA"
    BICUBIC_LUMA_BILINEAR_CHROMA = "BICUBIC_LUMA_BILINEAR_CHROMA"
    GAUSS = "GAUSS"
    SINC = "SINC"
    LANCZOS = "LANCZOS"
    SPLINE = "SPLINE"
