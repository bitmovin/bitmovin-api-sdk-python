# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class LiveEncodingStatus(Enum):
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
    WAITING_FOR_FIRST_CONNECT = "WAITING_FOR_FIRST_CONNECT"
    ERROR = "ERROR"
    NOT_AVAILABLE = "NOT_AVAILABLE"
    FINISHED = "FINISHED"
