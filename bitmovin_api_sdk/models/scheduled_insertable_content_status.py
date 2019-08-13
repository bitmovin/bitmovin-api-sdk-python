# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class ScheduledInsertableContentStatus(Enum):
    CREATED = "CREATED"
    SCHEDULED = "SCHEDULED"
    TO_BE_DESCHEDULED = "TO_BE_DESCHEDULED"
    DESCHEDULED = "DESCHEDULED"
    ERROR = "ERROR"
