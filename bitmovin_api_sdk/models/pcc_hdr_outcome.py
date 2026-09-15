# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class PccHdrOutcome(Enum):
    HDR = "hdr"
    SDR = "sdr"
    CLAIMED = "claimed"
    DENIED = "denied"
    UNESTABLISHED = "unestablished"
    UNREPORTED = "unreported"
