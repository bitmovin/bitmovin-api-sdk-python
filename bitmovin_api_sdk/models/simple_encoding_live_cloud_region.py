# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class SimpleEncodingLiveCloudRegion(Enum):
    NORTH_AMERICA = "NORTH_AMERICA"
    SOUTH_AMERICA = "SOUTH_AMERICA"
    EUROPE = "EUROPE"
    AFRICA = "AFRICA"
    ASIA = "ASIA"
    AUSTRALIA = "AUSTRALIA"
