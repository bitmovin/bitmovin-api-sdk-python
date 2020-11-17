# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class PrewarmedEncoderDiskSize(Enum):
    GB_500 = "500"
    GB_1000 = "1000"
    GB_2000 = "2000"
