# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AnalyticsVideoStartFailedReason(Enum):
    PAGE_CLOSED = "PAGE_CLOSED"
    PLAYER_ERROR = "PLAYER_ERROR"
    TIMEOUT = "TIMEOUT"
    UNKNOWN = "UNKNOWN"
