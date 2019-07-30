# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class IvSize(Enum):
    IV_8_BYTES = "8_BYTES"
    IV_16_BYTES = "16_BYTES"
