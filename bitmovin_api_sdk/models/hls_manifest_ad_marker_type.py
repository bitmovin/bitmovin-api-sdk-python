# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class HlsManifestAdMarkerType(Enum):
    EXT_X_CUE_OUT_IN = "EXT_X_CUE_OUT_IN"
    EXT_OATCLS_SCTE35 = "EXT_OATCLS_SCTE35"
    EXT_X_SPLICEPOINT_SCTE35 = "EXT_X_SPLICEPOINT_SCTE35"
    EXT_X_DATERANGE = "EXT_X_DATERANGE"
    EXT_X_SCTE35 = "EXT_X_SCTE35"
