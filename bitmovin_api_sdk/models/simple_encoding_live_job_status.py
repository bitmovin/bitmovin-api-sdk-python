# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class SimpleEncodingLiveJobStatus(Enum):
    CREATED = "CREATED"
    EXECUTING = "EXECUTING"
    FAILURE = "FAILURE"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"
    ERROR = "ERROR"
    CANCELED = "CANCELED"
