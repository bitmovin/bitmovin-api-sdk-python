# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AnalyticsQueryOperator(Enum):
    IN = "IN"
    EQ = "EQ"
    NE = "NE"
    LT = "LT"
    LTE = "LTE"
    GT = "GT"
    GTE = "GTE"
    CONTAINS = "CONTAINS"
    NOTCONTAINS = "NOTCONTAINS"
