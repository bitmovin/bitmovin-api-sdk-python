# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class Vp9AqMode(Enum):
    NONE = "NONE"
    VARIANCE = "VARIANCE"
    COMPLEXITY = "COMPLEXITY"
    CYCLIC = "CYCLIC"
