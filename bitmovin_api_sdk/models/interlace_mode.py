# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class InterlaceMode(Enum):
    TOP = "TOP"
    BOTTOM = "BOTTOM"
    DROP_EVEN = "DROP_EVEN"
    DROP_ODD = "DROP_ODD"
    PAD = "PAD"
    INTERLACE_X2 = "INTERLACE_X2"
    MERGE = "MERGE"
    MERGE_X2 = "MERGE_X2"
