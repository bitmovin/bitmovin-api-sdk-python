# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class PcmSampleFormat(Enum):
    S16LE = "S16LE"
    S24LE = "S24LE"
