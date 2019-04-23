# coding: utf-8
from enum import Enum


class AnalyticsExportStatus(Enum):
    """
    allowed enum values
    """
    STARTED = "STARTED"
    FINISHED = "FINISHED"
    QUEUED = "QUEUED"
    ERROR = "ERROR"
