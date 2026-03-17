# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class S3StorageClass(Enum):
    GLACIER_IR = "GLACIER_IR"
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"
    ONEZONE_IA = "ONEZONE_IA"
    REDUCED_REDUNDANCY = "REDUCED_REDUNDANCY"
    STANDARD = "STANDARD"
    STANDARD_IA = "STANDARD_IA"
