# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class SceneType(Enum):
    LOGO_IDENT = "LOGO_IDENT"
    OPENING_CREDITS = "OPENING_CREDITS"
    RECAP = "RECAP"
    PREVIEW_THIS_TITLE = "PREVIEW_THIS_TITLE"
    PROMOTION_OTHER_TITLE = "PROMOTION_OTHER_TITLE"
    BREAK_BUMPER = "BREAK_BUMPER"
    END_CREDITS = "END_CREDITS"
    ADS = "ADS"
    MAIN_CONTENT = "MAIN_CONTENT"
    UNKNOWN = "UNKNOWN"
