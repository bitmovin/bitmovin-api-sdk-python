# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class InputColorPrimaries(Enum):
    UNSPECIFIED = "UNSPECIFIED"
    BT709 = "BT709"
    BT470M = "BT470M"
    BT470BG = "BT470BG"
    SMPTE170M = "SMPTE170M"
    SMPTE240M = "SMPTE240M"
    FILM = "FILM"
    BT2020 = "BT2020"
    SMPTE428 = "SMPTE428"
    SMPTEST428_1 = "SMPTEST428_1"
    SMPTE431 = "SMPTE431"
    SMPTE432 = "SMPTE432"
    JEDEC_P22 = "JEDEC_P22"
