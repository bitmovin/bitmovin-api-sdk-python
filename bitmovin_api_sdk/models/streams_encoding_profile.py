# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class StreamsEncodingProfile(Enum):
    PER_TITLE = "PER_TITLE"
    FIXED_RESOLUTIONS = "FIXED_RESOLUTIONS"
