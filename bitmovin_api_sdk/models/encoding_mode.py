# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class EncodingMode(Enum):
    STANDARD = "STANDARD"
    SINGLE_PASS = "SINGLE_PASS"
    TWO_PASS = "TWO_PASS"
    THREE_PASS = "THREE_PASS"
