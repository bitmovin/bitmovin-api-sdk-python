# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class LiveEncodingEventName(Enum):
    FIRST_CONNECT = "FIRST_CONNECT"
    DISCONNECT = "DISCONNECT"
    RECONNECT = "RECONNECT"
    RESYNCING = "RESYNCING"
    IDLE = "IDLE"
    ERROR = "ERROR"
