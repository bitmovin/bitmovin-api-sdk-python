# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AvailabilityStartTimeMode(Enum):
    ON_FIRST_SEGMENT = "ON_FIRST_SEGMENT"
    ON_STREAM_INGEST = "ON_STREAM_INGEST"
