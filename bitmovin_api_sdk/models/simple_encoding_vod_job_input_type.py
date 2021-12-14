# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class SimpleEncodingVodJobInputType(Enum):
    VIDEO = "VIDEO"
    AUDIO = "AUDIO"
    SUBTITLES = "SUBTITLES"
    CLOSED_CAPTIONS = "CLOSED_CAPTIONS"
