# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class FragmentedMp4MuxingManifestType(Enum):
    SMOOTH = "SMOOTH"
    DASH_ON_DEMAND = "DASH_ON_DEMAND"
    HLS_BYTE_RANGES = "HLS_BYTE_RANGES"
    NONE = "NONE"
    HLS_BYTE_RANGES_AND_IFRAME_PLAYLIST = "HLS_BYTE_RANGES_AND_IFRAME_PLAYLIST"
