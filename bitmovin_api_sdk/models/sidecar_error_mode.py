# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class SidecarErrorMode(Enum):
    FAIL_ON_ERROR = "FAIL_ON_ERROR"
    CONTINUE_ON_ERROR = "CONTINUE_ON_ERROR"
