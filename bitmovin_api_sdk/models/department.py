# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class Department(Enum):
    ACTING = "ACTING"
    ANIMATION = "ANIMATION"
    CASTING = "CASTING"
    CINEMATOGRAPHY = "CINEMATOGRAPHY"
    COSTUME_DESIGN = "COSTUME_DESIGN"
    DIRECTING = "DIRECTING"
    FILM_EDITING = "FILM_EDITING"
    MAKEUP_AND_HAIRSTYLING = "MAKEUP_AND_HAIRSTYLING"
    MUSIC = "MUSIC"
    PRODUCTION = "PRODUCTION"
    PRODUCTION_DESIGN = "PRODUCTION_DESIGN"
    SOUND = "SOUND"
    VISUAL_EFFECTS = "VISUAL_EFFECTS"
    WRITING = "WRITING"
    UNKNOWN = "UNKNOWN"
