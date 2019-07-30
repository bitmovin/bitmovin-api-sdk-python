# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class TextFilterFont(Enum):
    DEJAVUSANS = "DEJAVUSANS"
    DEJAVUSERIF = "DEJAVUSERIF"
    DEJAVUSANSMONO = "DEJAVUSANSMONO"
    ROBOTOMONO = "ROBOTOMONO"
    ROBOTOBLACK = "ROBOTOBLACK"
    ROBOTO = "ROBOTO"
    ROBOTOCONDENSED = "ROBOTOCONDENSED"
