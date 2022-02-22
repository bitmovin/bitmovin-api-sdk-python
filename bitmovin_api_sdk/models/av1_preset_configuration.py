# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class Av1PresetConfiguration(Enum):
    VOD_QUALITY = "VOD_QUALITY"
    VOD_STANDARD = "VOD_STANDARD"
    VOD_SPEED = "VOD_SPEED"
