# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class MaxCtuSize(Enum):
    S16 = "16"
    S32 = "32"
    S64 = "64"
