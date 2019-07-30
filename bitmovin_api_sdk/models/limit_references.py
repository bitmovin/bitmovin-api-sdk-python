# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class LimitReferences(Enum):
    DISABLED = "DISABLED"
    DEPTH = "DEPTH"
    CU = "CU"
    DEPTH_AND_CU = "DEPTH_AND_CU"
