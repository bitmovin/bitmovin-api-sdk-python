# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class H264Partition(Enum):
    NONE = "NONE"
    P8X8 = "P8X8"
    P4X4 = "P4X4"
    B8X8 = "B8X8"
    I8X8 = "I8X8"
    I4X4 = "I4X4"
    ALL = "ALL"
