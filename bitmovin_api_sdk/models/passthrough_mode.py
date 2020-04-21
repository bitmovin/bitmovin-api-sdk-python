# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class PassthroughMode(Enum):
    VIDEO_STREAM = "VIDEO_STREAM"
    CAPTION_STREAM = "CAPTION_STREAM"
    VIDEO_CAPTION_STREAM = "VIDEO_CAPTION_STREAM"
