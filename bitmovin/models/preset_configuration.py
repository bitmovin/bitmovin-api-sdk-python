# coding: utf-8
from enum import Enum


class PresetConfiguration(Enum):
    """
    allowed enum values
    """
    LIVE_HIGH_QUALITY = "LIVE_HIGH_QUALITY"
    LIVE_LOW_LATENCY = "LIVE_LOW_LATENCY"
    VOD_HIGH_QUALITY = "VOD_HIGH_QUALITY"
    VOD_HIGH_SPEED = "VOD_HIGH_SPEED"
