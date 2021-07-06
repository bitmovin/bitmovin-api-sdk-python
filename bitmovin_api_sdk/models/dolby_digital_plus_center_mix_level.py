# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class DolbyDigitalPlusCenterMixLevel(Enum):
    PLUS_3_DB = "PLUS_3_DB"
    PLUS_1_5_DB = "PLUS_1_5_DB"
    ZERO_DB = "ZERO_DB"
    MINUS_1_5_DB = "MINUS_1_5_DB"
    MINUS_3_DB = "MINUS_3_DB"
    MINUS_4_5_DB = "MINUS_4_5_DB"
    MINUS_6_DB = "MINUS_6_DB"
    MINUS_INFINITY_DB = "MINUS_INFINITY_DB"
