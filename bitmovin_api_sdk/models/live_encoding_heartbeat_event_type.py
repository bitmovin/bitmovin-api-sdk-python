# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class LiveEncodingHeartbeatEventType(Enum):
    FIRST_CONNECT = "FIRST_CONNECT"
    DISCONNECT = "DISCONNECT"
    RECONNECT = "RECONNECT"
    WARNING = "WARNING"
    ERROR = "ERROR"
