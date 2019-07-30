# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class ConditionOperator(Enum):
    EQUAL = "=="
    NOT_EQUAL = "!="
    LESS_THAN_OR_EQUAL = "<="
    LESS_THAN = "<"
    GREATER_THAN = ">"
    GREATER_THAN_OR_EQUAL = ">="
