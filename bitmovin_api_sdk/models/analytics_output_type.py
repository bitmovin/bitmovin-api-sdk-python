# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AnalyticsOutputType(Enum):
    S3_ROLE_BASED = "S3_ROLE_BASED"
    GCS_SERVICE_ACCOUNT = "GCS_SERVICE_ACCOUNT"
    AZURE = "AZURE"
