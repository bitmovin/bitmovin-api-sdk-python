# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class EnhancedDeinterlaceAutoEnable(Enum):
    ALWAYS_ON = "ALWAYS_ON"
    META_DATA_BASED = "META_DATA_BASED"
