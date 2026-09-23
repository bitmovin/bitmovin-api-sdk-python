# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AiSceneAnalysisLiveSourceGapReason(Enum):
    SOURCE_DISCONNECTED = "SOURCE_DISCONNECTED"
    PROCESSING_MEDIA_PRESSURE = "PROCESSING_MEDIA_PRESSURE"
    ANALYSIS_LAG = "ANALYSIS_LAG"
    WINDOW_BUILD_FAILED = "WINDOW_BUILD_FAILED"
    FINALIZATION_BACKLOG = "FINALIZATION_BACKLOG"
