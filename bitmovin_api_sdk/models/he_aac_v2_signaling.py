# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class HeAacV2Signaling(Enum):
    DEFAULT = "DEFAULT"
    IMPLICIT = "IMPLICIT"
    EXPLICIT_SBR = "EXPLICIT_SBR"
    EXPLICIT_HIERACHICAL = "EXPLICIT_HIERACHICAL"
