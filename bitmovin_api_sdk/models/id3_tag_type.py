# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class Id3TagType(Enum):
    RAW = "RAW"
    FRAME_ID = "FRAME_ID"
    PLAIN_TEXT = "PLAIN_TEXT"
