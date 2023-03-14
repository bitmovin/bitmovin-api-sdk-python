# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AzureCloudRegion(Enum):
    AUSTRALIA_EAST = "AUSTRALIA_EAST"
    AUSTRALIA_SOUTHEAST = "AUSTRALIA_SOUTHEAST"
    EUROPE_NORTH = "EUROPE_NORTH"
    EUROPE_WEST = "EUROPE_WEST"
    GERMANY_WESTCENTRAL = "GERMANY_WESTCENTRAL"
    UAE_NORTH = "UAE_NORTH"
    US_EAST = "US_EAST"
    US_WEST2 = "US_WEST2"
