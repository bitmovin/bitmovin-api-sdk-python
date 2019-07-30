# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class RaiUnit(Enum):
    NONE = "NONE"
    ALL_PES_PACKETS = "ALL_PES_PACKETS"
    ACQUISITION_POINT_PACKETS = "ACQUISITION_POINT_PACKETS"
    ACCORDING_TO_INPUT = "ACCORDING_TO_INPUT"
