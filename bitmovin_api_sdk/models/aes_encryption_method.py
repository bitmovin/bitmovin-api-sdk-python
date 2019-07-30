# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AesEncryptionMethod(Enum):
    SAMPLE_AES = "SAMPLE_AES"
    AES_128 = "AES_128"
