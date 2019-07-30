# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class PictureFieldParity(Enum):
    AUTO = "AUTO"
    TOP_FIELD_FIRST = "TOP_FIELD_FIRST"
    BOTTOM_FIELD_FIRST = "BOTTOM_FIELD_FIRST"
