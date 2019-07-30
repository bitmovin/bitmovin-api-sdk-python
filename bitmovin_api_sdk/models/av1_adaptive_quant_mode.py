# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class Av1AdaptiveQuantMode(Enum):
    OFF = "OFF"
    VARIANCE = "VARIANCE"
    COMPLEXITY = "COMPLEXITY"
    CYCLIC_REFRESH = "CYCLIC_REFRESH"
    DELTA_QUANT = "DELTA_QUANT"
