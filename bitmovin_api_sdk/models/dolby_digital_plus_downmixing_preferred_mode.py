# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class DolbyDigitalPlusDownmixingPreferredMode(Enum):
    LO_RO = "LO_RO"
    LT_RT = "LT_RT"
    PRO_LOGIC_II = "PRO_LOGIC_II"
