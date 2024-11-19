# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class LiveStandbyPoolEncodingStatus(Enum):
    TO_BE_CREATED = "TO_BE_CREATED"
    CREATING = "CREATING"
    PREPARING = "PREPARING"
    READY = "READY"
    TO_BE_DELETED = "TO_BE_DELETED"
    DELETING = "DELETING"
    ACQUIRED = "ACQUIRED"
    ERROR = "ERROR"
