# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AdaptationSetRole(Enum):
    ALTERNATE = "ALTERNATE"
    CAPTION = "CAPTION"
    COMMENTARY = "COMMENTARY"
    DUB = "DUB"
    MAIN = "MAIN"
    SUBTITLE = "SUBTITLE"
    SUPPLEMENTARY = "SUPPLEMENTARY"
