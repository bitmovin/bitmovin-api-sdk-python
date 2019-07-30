# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class OpusChannelLayout(Enum):
    NONE = "NONE"
    MONO = "MONO"
    CL_STEREO = "STEREO"
    CL_SURROUND = "SURROUND"
    CL_QUAD = "QUAD"
    CL_4_1 = "4.1"
    CL_5_0_BACK = "5.0_BACK"
    XCL_5_1_BACK = "5.1_BACK"
    CL_6_1 = "6.1"
    CL_7_1 = "7.1"
