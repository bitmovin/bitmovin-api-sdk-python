# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AnalyticsRuleMetric(Enum):
    AVG_VIDEO_STARTUPTIME = "AVG_VIDEO_STARTUPTIME"
    MEDIAN_VIDEO_STARTUPTIME = "MEDIAN_VIDEO_STARTUPTIME"
