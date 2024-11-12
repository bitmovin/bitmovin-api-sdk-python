# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AkamaiCloudRegion(Enum):
    BR_GRU = "BR_GRU"
    ES_MAD = "ES_MAD"
    FR_PAR = "FR_PAR"
    ID_CGK = "ID_CGK"
    IN_MAA = "IN_MAA"
    IT_MIL = "IT_MIL"
    JP_OSA = "JP_OSA"
    NL_AMS = "NL_AMS"
    SE_STO = "SE_STO"
    US_LAX = "US_LAX"
    US_MIA = "US_MIA"
    US_ORD = "US_ORD"
    US_SEA = "US_SEA"
