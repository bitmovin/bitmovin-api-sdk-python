# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class DolbyDigitalPlusLoudnessControlRegulationType(Enum):
    EBU_R128 = "EBU_R128"
    ATSC_A85_FIXED = "ATSC_A85_FIXED"
    ATSC_A85_AGILE = "ATSC_A85_AGILE"
    MANUAL = "MANUAL"
