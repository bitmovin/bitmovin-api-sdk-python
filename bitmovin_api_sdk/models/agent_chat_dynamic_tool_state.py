# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AgentChatDynamicToolState(Enum):
    INPUT_STREAMING = "input-streaming"
    INPUT_AVAILABLE = "input-available"
    OUTPUT_AVAILABLE = "output-available"
    OUTPUT_ERROR = "output-error"
