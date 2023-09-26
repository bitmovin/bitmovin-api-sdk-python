# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class EncodingTemplate(Enum):
    H264 = "H264"
    H264_FIXED_RESOLUTIONS = "H264_FIXED_RESOLUTIONS"
    AV1 = "AV1"
