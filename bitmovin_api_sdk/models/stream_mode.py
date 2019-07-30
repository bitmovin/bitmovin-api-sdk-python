# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class StreamMode(Enum):
    STANDARD = "STANDARD"
    PER_TITLE_TEMPLATE = "PER_TITLE_TEMPLATE"
    PER_TITLE_TEMPLATE_FIXED_RESOLUTION = "PER_TITLE_TEMPLATE_FIXED_RESOLUTION"
    PER_TITLE_TEMPLATE_FIXED_RESOLUTION_AND_BITRATE = "PER_TITLE_TEMPLATE_FIXED_RESOLUTION_AND_BITRATE"
    PER_TITLE_RESULT = "PER_TITLE_RESULT"
