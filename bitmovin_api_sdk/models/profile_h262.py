# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class ProfileH262(Enum):
    MPEG2_422 = "MPEG2_422"
