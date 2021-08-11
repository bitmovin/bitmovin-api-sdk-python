# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class OttLoudnessMode(Enum):
    DTSX_OTT_LOUDNESS_DETECT = "DTSX_OTT_LOUDNESS_DETECT"
    DTSX_OTT_LOUDNESS_INPUT = "DTSX_OTT_LOUDNESS_INPUT"
    DTSX_OTT_LOUDNESS_TARGET = "DTSX_OTT_LOUDNESS_TARGET"
