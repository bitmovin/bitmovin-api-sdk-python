# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class ChromaLocation(Enum):
    UNSPECIFIED = "UNSPECIFIED"
    LEFT = "LEFT"
    CENTER = "CENTER"
    TOPLEFT = "TOPLEFT"
    TOP = "TOP"
    BOTTOMLEFT = "BOTTOMLEFT"
    BOTTOM = "BOTTOM"
