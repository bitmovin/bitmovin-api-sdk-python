# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class PccVerdict(Enum):
    PLAYED = "played"
    CLAIMED_BUT_NOT_VERIFIED = "claimed-but-not-verified"
    DECLARES_NO_SUPPORT = "declares-no-support"
    INCONSISTENT_CLAIM = "inconsistent-claim"
    INCONCLUSIVE = "inconclusive"
    UNMEASURED = "unmeasured"
    NOT_APPLICABLE = "not-applicable"
    INFRASTRUCTURE_FAULT = "infrastructure-fault"
    NEVER_REACHED = "never-reached"
