# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class TuIntraDepth(Enum):
    D1 = "1"
    D2 = "2"
    D3 = "3"
    D4 = "4"
