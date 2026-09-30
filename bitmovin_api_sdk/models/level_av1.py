# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class LevelAv1(Enum):
    L2_0 = "2.0"
    L2_1 = "2.1"
    L3_0 = "3.0"
    L3_1 = "3.1"
    L4_0 = "4.0"
    L4_1 = "4.1"
    L5_0 = "5.0"
    L5_1 = "5.1"
    L5_2 = "5.2"
    L5_3 = "5.3"
    L6_0 = "6.0"
    L6_1 = "6.1"
    L6_2 = "6.2"
    L6_3 = "6.3"
