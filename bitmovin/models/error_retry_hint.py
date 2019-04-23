# coding: utf-8
from enum import Enum


class ErrorRetryHint(Enum):
    """
    allowed enum values
    """
    RETRY = "RETRY"
    NO_RETRY = "NO_RETRY"
    RETRY_IN_DIFFERENT_REGION = "RETRY_IN_DIFFERENT_REGION"
