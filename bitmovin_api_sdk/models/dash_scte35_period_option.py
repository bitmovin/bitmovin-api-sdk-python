# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class DashScte35PeriodOption(Enum):
    SINGLE_PERIOD = "SINGLE_PERIOD"
    MULTI_PERIOD = "MULTI_PERIOD"
