# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class MediaConfigBitrate(Enum):
    MCB_160000 = "160000"
    MCB_192000 = "192000"
    MCB_224000 = "224000"
    MCB_256000 = "256000"
    MCB_288000 = "288000"
    MCB_320000 = "320000"
    MCB_384000 = "384000"
    MCB_448000 = "448000"
