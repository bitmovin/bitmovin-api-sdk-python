# coding: utf-8
from enum import Enum


class AkamaiMslStreamFormat(Enum):
    """
    allowed enum values
    """
    DASH = "DASH"
    HLS = "HLS"
    CMAF = "CMAF"
