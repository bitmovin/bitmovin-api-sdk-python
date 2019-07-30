# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class H264SubMe(Enum):
    FULLPEL = "FULLPEL"
    SAD = "SAD"
    SATD = "SATD"
    QPEL3 = "QPEL3"
    QPEL4 = "QPEL4"
    QPEL5 = "QPEL5"
    RD_IP = "RD_IP"
    RD_ALL = "RD_ALL"
    RD_REF_IP = "RD_REF_IP"
    RD_REF_ALL = "RD_REF_ALL"
