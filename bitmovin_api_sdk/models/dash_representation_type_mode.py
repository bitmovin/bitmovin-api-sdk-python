# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class DashRepresentationTypeMode(Enum):
    TEMPLATE_REPRESENTATION = "TEMPLATE_REPRESENTATION"
    TEMPLATE_ADAPTATION_SET = "TEMPLATE_ADAPTATION_SET"
