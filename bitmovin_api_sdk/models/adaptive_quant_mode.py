# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AdaptiveQuantMode(Enum):
    DISABLED = "DISABLED"
    VARIANCE = "VARIANCE"
    AUTO_VARIANCE = "AUTO_VARIANCE"
    AUTO_VARIANCE_DARK_SCENES = "AUTO_VARIANCE_DARK_SCENES"
