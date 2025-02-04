# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class ProgramDateTimePlacementMode(Enum):
    ONCE_PER_PLAYLIST = "ONCE_PER_PLAYLIST"
    SEGMENTS_INTERVAL = "SEGMENTS_INTERVAL"
    SECONDS_INTERVAL = "SECONDS_INTERVAL"
