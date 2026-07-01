# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class H265V2PresetConfiguration(Enum):
    VOD_QUALITY = "VOD_QUALITY"
    VOD_HIGH_QUALITY = "VOD_HIGH_QUALITY"
