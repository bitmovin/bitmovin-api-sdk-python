# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AzureCloudRegion(Enum):
    ASIA_EAST = "ASIA_EAST"
    ASIA_SOUTHEAST = "ASIA_SOUTHEAST"
    AUSTRALIA_EAST = "AUSTRALIA_EAST"
    AUSTRALIA_SOUTHEAST = "AUSTRALIA_SOUTHEAST"
    BRAZIL_SOUTH = "BRAZIL_SOUTH"
    CANADA_CENTRAL = "CANADA_CENTRAL"
    EUROPE_NORTH = "EUROPE_NORTH"
    EUROPE_WEST = "EUROPE_WEST"
    FRANCE_CENTRAL = "FRANCE_CENTRAL"
    GERMANY_WESTCENTRAL = "GERMANY_WESTCENTRAL"
    INDIA_CENTRAL = "INDIA_CENTRAL"
    INDIA_SOUTH = "INDIA_SOUTH"
    JAPAN_EAST = "JAPAN_EAST"
    JAPAN_WEST = "JAPAN_WEST"
    KOREA_CENTRAL = "KOREA_CENTRAL"
    UAE_NORTH = "UAE_NORTH"
    US_CENTRAL = "US_CENTRAL"
    US_EAST = "US_EAST"
    US_EAST2 = "US_EAST2"
    US_WEST = "US_WEST"
    US_WEST2 = "US_WEST2"
    US_SOUTH_CENTRAL = "US_SOUTH_CENTRAL"
    US_NORTH_CENTRAL = "US_NORTH_CENTRAL"
    UK_SOUTH = "UK_SOUTH"
