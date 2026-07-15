# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class H265V2PerceptualEncodingMode(Enum):
    OFF = "OFF"
    CU_DELTA_QP = "CU_DELTA_QP"
