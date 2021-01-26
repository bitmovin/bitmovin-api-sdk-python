# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class RetryHint(Enum):
    RETRY = "RETRY"
    RETRY_IN_DIFFERENT_REGION = "RETRY_IN_DIFFERENT_REGION"
    NO_RETRY = "NO_RETRY"
    UNDEFINED = "UNDEFINED"
