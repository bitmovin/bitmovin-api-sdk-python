# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AudioVolumeFormat(Enum):
    U8 = "U8"
    S16 = "S16"
    S32 = "S32"
    U8P = "U8P"
    S16P = "S16P"
    S32P = "S32P"
    S64 = "S64"
    S64P = "S64P"
    FLT = "FLT"
    FLTP = "FLTP"
    NONE = "NONE"
    DBL = "DBL"
    DBLP = "DBLP"
