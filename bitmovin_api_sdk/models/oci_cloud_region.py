# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class OciCloudRegion(Enum):
    EU_FRANKFURT_1 = "EU_FRANKFURT_1"
    US_ASHBURN_1 = "US_ASHBURN_1"
