# coding: utf-8
from enum import Enum


class SidecarErrorMode(Enum):
    """
    allowed enum values
    """
    FAIL_ON_ERROR = "FAIL_ON_ERROR"
    CONTINUE_ON_ERROR = "CONTINUE_ON_ERROR"
