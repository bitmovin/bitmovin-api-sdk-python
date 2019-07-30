# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class PerTitleFixedResolutionAndBitrateConfigurationMode(Enum):
    LAST_CALCULATED_BITRATE = "LAST_CALCULATED_BITRATE"
    MINIMUM = "MINIMUM"
    MAXIMUM = "MAXIMUM"
    AVERAGE = "AVERAGE"
