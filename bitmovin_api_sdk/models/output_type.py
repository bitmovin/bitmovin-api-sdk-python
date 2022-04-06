# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class OutputType(Enum):
    AKAMAI_NETSTORAGE = "AKAMAI_NETSTORAGE"
    AZURE = "AZURE"
    GENERIC_S3 = "GENERIC_S3"
    GCS = "GCS"
    FTP = "FTP"
    LOCAL = "LOCAL"
    S3 = "S3"
    S3_ROLE_BASED = "S3_ROLE_BASED"
    SFTP = "SFTP"
    AKAMAI_MSL = "AKAMAI_MSL"
    LIVE_MEDIA_INGEST = "LIVE_MEDIA_INGEST"
    GCS_SERVICE_ACCOUNT = "GCS_SERVICE_ACCOUNT"
    CDN = "CDN"
