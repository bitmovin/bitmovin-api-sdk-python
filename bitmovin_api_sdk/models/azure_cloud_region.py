# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AzureCloudRegion(Enum):
    US_WEST2 = "AUSTRALIA_EAST"
    US_EAST = "AUSTRALIA_SOUTHEAST"
    EUROPE_NORTH = "EUROPE_NORTH"
    EUROPE_WEST = "EUROPE_WEST"
    GERMANY_WESTCENTRAL = "GERMANY_WESTCENTRAL"
    AUSTRALIA_EAST = "UAE_NORTH"
    AUSTRALIA_SOUTHEAST = "US_EAST"
    UAE_NORTH = "US_WEST2"
