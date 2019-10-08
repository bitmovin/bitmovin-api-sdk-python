# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class DrmType(Enum):
    WIDEVINE = "WIDEVINE"
    PLAYREADY = "PLAYREADY"
    PRIMETIME = "PRIMETIME"
    FAIRPLAY = "FAIRPLAY"
    MARLIN = "MARLIN"
    CLEARKEY = "CLEARKEY"
    AES = "AES"
    CENC = "CENC"
    SPEKE = "SPEKE"
