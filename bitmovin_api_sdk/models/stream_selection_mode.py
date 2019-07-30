# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class StreamSelectionMode(Enum):
    AUTO = "AUTO"
    POSITION_ABSOLUTE = "POSITION_ABSOLUTE"
    VIDEO_RELATIVE = "VIDEO_RELATIVE"
    AUDIO_RELATIVE = "AUDIO_RELATIVE"
    SUBTITLE_RELATIVE = "SUBTITLE_RELATIVE"
