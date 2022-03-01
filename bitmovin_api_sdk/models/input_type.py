# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class InputType(Enum):
    AKAMAI_NETSTORAGE = "AKAMAI_NETSTORAGE"
    ASPERA = "ASPERA"
    AZURE = "AZURE"
    REDUNDANT_RTMP = "REDUNDANT_RTMP"
    FTP = "FTP"
    GENERIC_S3 = "GENERIC_S3"
    GCS = "GCS"
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    LOCAL = "LOCAL"
    RTMP = "RTMP"
    S3 = "S3"
    S3_ROLE_BASED = "S3_ROLE_BASED"
    SFTP = "SFTP"
    TCP = "TCP"
    UDP = "UDP"
    UDP_MULTICAST = "UDP_MULTICAST"
    ZIXI = "ZIXI"
    SRT = "SRT"
    GCS_SERVICE_ACCOUNT = "GCS_SERVICE_ACCOUNT"
