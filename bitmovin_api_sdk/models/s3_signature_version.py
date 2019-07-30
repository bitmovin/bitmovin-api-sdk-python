# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class S3SignatureVersion(Enum):
    V2 = "S3_V2"
    V4 = "S3_V4"
