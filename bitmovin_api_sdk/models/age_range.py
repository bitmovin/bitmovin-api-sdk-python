# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AgeRange(Enum):
    CHILD = "CHILD"
    TEEN = "TEEN"
    TWENTIES = "TWENTIES"
    THIRTIES = "THIRTIES"
    FORTIES = "FORTIES"
    FIFTIES = "FIFTIES"
    SIXTIES_PLUS = "SIXTIES_PLUS"
    UNKNOWN = "UNKNOWN"
