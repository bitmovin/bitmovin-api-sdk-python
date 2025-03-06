# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.ai_content_analysis_asset_description import AiContentAnalysisAssetDescription
from bitmovin_api_sdk.models.ai_content_analysis_automatic_ad_placement import AiContentAnalysisAutomaticAdPlacement
import pprint
import six


class AiContentAnalysisFeatures(object):
    @poscheck_model
    def __init__(self,
                 asset_description=None,
                 automatic_ad_placement=None):
        # type: (AiContentAnalysisAssetDescription, AiContentAnalysisAutomaticAdPlacement) -> None

        self._asset_description = None
        self._automatic_ad_placement = None
        self.discriminator = None

        if asset_description is not None:
            self.asset_description = asset_description
        if automatic_ad_placement is not None:
            self.automatic_ad_placement = automatic_ad_placement

    @property
    def openapi_types(self):
        types = {
            'asset_description': 'AiContentAnalysisAssetDescription',
            'automatic_ad_placement': 'AiContentAnalysisAutomaticAdPlacement'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'asset_description': 'assetDescription',
            'automatic_ad_placement': 'automaticAdPlacement'
        }
        return attributes

    @property
    def asset_description(self):
        # type: () -> AiContentAnalysisAssetDescription
        """Gets the asset_description of this AiContentAnalysisFeatures.

        AI content analysis will create an asset description file. 

        :return: The asset_description of this AiContentAnalysisFeatures.
        :rtype: AiContentAnalysisAssetDescription
        """
        return self._asset_description

    @asset_description.setter
    def asset_description(self, asset_description):
        # type: (AiContentAnalysisAssetDescription) -> None
        """Sets the asset_description of this AiContentAnalysisFeatures.

        AI content analysis will create an asset description file. 

        :param asset_description: The asset_description of this AiContentAnalysisFeatures.
        :type: AiContentAnalysisAssetDescription
        """

        if asset_description is not None:
            if not isinstance(asset_description, AiContentAnalysisAssetDescription):
                raise TypeError("Invalid type for `asset_description`, type has to be `AiContentAnalysisAssetDescription`")

        self._asset_description = asset_description

    @property
    def automatic_ad_placement(self):
        # type: () -> AiContentAnalysisAutomaticAdPlacement
        """Gets the automatic_ad_placement of this AiContentAnalysisFeatures.

        Ad markers placed on detected scene changes and configured positions. 

        :return: The automatic_ad_placement of this AiContentAnalysisFeatures.
        :rtype: AiContentAnalysisAutomaticAdPlacement
        """
        return self._automatic_ad_placement

    @automatic_ad_placement.setter
    def automatic_ad_placement(self, automatic_ad_placement):
        # type: (AiContentAnalysisAutomaticAdPlacement) -> None
        """Sets the automatic_ad_placement of this AiContentAnalysisFeatures.

        Ad markers placed on detected scene changes and configured positions. 

        :param automatic_ad_placement: The automatic_ad_placement of this AiContentAnalysisFeatures.
        :type: AiContentAnalysisAutomaticAdPlacement
        """

        if automatic_ad_placement is not None:
            if not isinstance(automatic_ad_placement, AiContentAnalysisAutomaticAdPlacement):
                raise TypeError("Invalid type for `automatic_ad_placement`, type has to be `AiContentAnalysisAutomaticAdPlacement`")

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
        if not isinstance(other, AiContentAnalysisFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
