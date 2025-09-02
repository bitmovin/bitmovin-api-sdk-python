# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.ai_scene_analysis_automatic_ad_placement import AiSceneAnalysisAutomaticAdPlacement
import pprint
import six


class SceneAnalysisAdPlacementMetadataResponse(object):
    @poscheck_model
    def __init__(self,
                 placed_ads=None,
                 automatic_ad_placement=None):
        # type: (list[AdPosition], AiSceneAnalysisAutomaticAdPlacement) -> None

        self._placed_ads = list()
        self._automatic_ad_placement = None
        self.discriminator = None

        if placed_ads is not None:
            self.placed_ads = placed_ads
        if automatic_ad_placement is not None:
            self.automatic_ad_placement = automatic_ad_placement

    @property
    def openapi_types(self):
        types = {
            'placed_ads': 'list[AdPosition]',
            'automatic_ad_placement': 'AiSceneAnalysisAutomaticAdPlacement'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'placed_ads': 'placedAds',
            'automatic_ad_placement': 'automaticAdPlacement'
        }
        return attributes

    @property
    def placed_ads(self):
        # type: () -> list[AdPosition]
        """Gets the placed_ads of this SceneAnalysisAdPlacementMetadataResponse.


        :return: The placed_ads of this SceneAnalysisAdPlacementMetadataResponse.
        :rtype: list[AdPosition]
        """
        return self._placed_ads

    @placed_ads.setter
    def placed_ads(self, placed_ads):
        # type: (list) -> None
        """Sets the placed_ads of this SceneAnalysisAdPlacementMetadataResponse.


        :param placed_ads: The placed_ads of this SceneAnalysisAdPlacementMetadataResponse.
        :type: list[AdPosition]
        """

        if placed_ads is not None:
            if not isinstance(placed_ads, list):
                raise TypeError("Invalid type for `placed_ads`, type has to be `list[AdPosition]`")

        self._placed_ads = placed_ads

    @property
    def automatic_ad_placement(self):
        # type: () -> AiSceneAnalysisAutomaticAdPlacement
        """Gets the automatic_ad_placement of this SceneAnalysisAdPlacementMetadataResponse.


        :return: The automatic_ad_placement of this SceneAnalysisAdPlacementMetadataResponse.
        :rtype: AiSceneAnalysisAutomaticAdPlacement
        """
        return self._automatic_ad_placement

    @automatic_ad_placement.setter
    def automatic_ad_placement(self, automatic_ad_placement):
        # type: (AiSceneAnalysisAutomaticAdPlacement) -> None
        """Sets the automatic_ad_placement of this SceneAnalysisAdPlacementMetadataResponse.


        :param automatic_ad_placement: The automatic_ad_placement of this SceneAnalysisAdPlacementMetadataResponse.
        :type: AiSceneAnalysisAutomaticAdPlacement
        """

        if automatic_ad_placement is not None:
            if not isinstance(automatic_ad_placement, AiSceneAnalysisAutomaticAdPlacement):
                raise TypeError("Invalid type for `automatic_ad_placement`, type has to be `AiSceneAnalysisAutomaticAdPlacement`")

        self._automatic_ad_placement = automatic_ad_placement

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                if len(value) == 0:
                    continue
                result[self.attribute_map.get(attr)] = [y.value if isinstance(y, Enum) else y for y in [x.to_dict() if hasattr(x, "to_dict") else x for x in value]]
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = {k: (v.to_dict() if hasattr(v, "to_dict") else v) for (k, v) in value.items()}
            else:
                result[self.attribute_map.get(attr)] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SceneAnalysisAdPlacementMetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
