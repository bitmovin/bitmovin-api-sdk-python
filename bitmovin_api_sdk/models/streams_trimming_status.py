# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class StreamsTrimmingStatus(Enum):
    UNAVAILABLE = "UNAVAILABLE"
    AVAILABLE = "AVAILABLE"
    STARTED = "STARTED"
    ERROR = "ERROR"
    FINISHED = "FINISHED"
