# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class ScenePacing(Enum):
    SLOW = "SLOW"
    MEASURED = "MEASURED"
    BRISK = "BRISK"
    FRANTIC = "FRANTIC"
    UNKNOWN = "UNKNOWN"
