# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class Cea608ChannelType(Enum):
    CC1 = "CC1"
    CC3 = "CC3"
