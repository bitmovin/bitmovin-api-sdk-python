# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class DtsXChannelLayout(Enum):
    CL_5_1 = "5.1"
    CL_5_1_4 = "5.1.4"
