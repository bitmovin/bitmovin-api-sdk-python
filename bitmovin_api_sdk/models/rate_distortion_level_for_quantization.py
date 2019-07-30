# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class RateDistortionLevelForQuantization(Enum):
    DISABLED = "DISABLED"
    LEVELS = "LEVELS"
    LEVELS_AND_CODING_GROUPS = "LEVELS_AND_CODING_GROUPS"
