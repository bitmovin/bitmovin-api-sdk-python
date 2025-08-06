# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.ai_scene_analysis_asset_description import AiSceneAnalysisAssetDescription
from bitmovin_api_sdk.models.ai_scene_analysis_automatic_ad_placement import AiSceneAnalysisAutomaticAdPlacement
from bitmovin_api_sdk.models.ai_scene_analysis_output_language_codes import AiSceneAnalysisOutputLanguageCodes
import pprint
import six


class AiSceneAnalysisFeatures(object):
    @poscheck_model
    def __init__(self,
                 asset_description=None,
                 automatic_ad_placement=None,
                 output_language_codes=None):
        # type: (AiSceneAnalysisAssetDescription, AiSceneAnalysisAutomaticAdPlacement, AiSceneAnalysisOutputLanguageCodes) -> None

        self._asset_description = None
        self._automatic_ad_placement = None
        self._output_language_codes = None
        self.discriminator = None

        if asset_description is not None:
            self.asset_description = asset_description
        if automatic_ad_placement is not None:
            self.automatic_ad_placement = automatic_ad_placement
        if output_language_codes is not None:
            self.output_language_codes = output_language_codes

    @property
    def openapi_types(self):
        types = {
            'asset_description': 'AiSceneAnalysisAssetDescription',
            'automatic_ad_placement': 'AiSceneAnalysisAutomaticAdPlacement',
            'output_language_codes': 'AiSceneAnalysisOutputLanguageCodes'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'asset_description': 'assetDescription',
            'automatic_ad_placement': 'automaticAdPlacement',
            'output_language_codes': 'outputLanguageCodes'
        }
        return attributes

    @property
    def asset_description(self):
        # type: () -> AiSceneAnalysisAssetDescription
        """Gets the asset_description of this AiSceneAnalysisFeatures.

        AI scene analysis will create an asset description file. 

        :return: The asset_description of this AiSceneAnalysisFeatures.
        :rtype: AiSceneAnalysisAssetDescription
        """
        return self._asset_description

    @asset_description.setter
    def asset_description(self, asset_description):
        # type: (AiSceneAnalysisAssetDescription) -> None
        """Sets the asset_description of this AiSceneAnalysisFeatures.

        AI scene analysis will create an asset description file. 

        :param asset_description: The asset_description of this AiSceneAnalysisFeatures.
        :type: AiSceneAnalysisAssetDescription
        """

        if asset_description is not None:
            if not isinstance(asset_description, AiSceneAnalysisAssetDescription):
                raise TypeError("Invalid type for `asset_description`, type has to be `AiSceneAnalysisAssetDescription`")

        self._asset_description = asset_description

    @property
    def automatic_ad_placement(self):
        # type: () -> AiSceneAnalysisAutomaticAdPlacement
        """Gets the automatic_ad_placement of this AiSceneAnalysisFeatures.

        Ad markers placed on detected scene changes and configured positions. 

        :return: The automatic_ad_placement of this AiSceneAnalysisFeatures.
        :rtype: AiSceneAnalysisAutomaticAdPlacement
        """
        return self._automatic_ad_placement

    @automatic_ad_placement.setter
    def automatic_ad_placement(self, automatic_ad_placement):
        # type: (AiSceneAnalysisAutomaticAdPlacement) -> None
        """Sets the automatic_ad_placement of this AiSceneAnalysisFeatures.

        Ad markers placed on detected scene changes and configured positions. 

        :param automatic_ad_placement: The automatic_ad_placement of this AiSceneAnalysisFeatures.
        :type: AiSceneAnalysisAutomaticAdPlacement
        """

        if automatic_ad_placement is not None:
            if not isinstance(automatic_ad_placement, AiSceneAnalysisAutomaticAdPlacement):
                raise TypeError("Invalid type for `automatic_ad_placement`, type has to be `AiSceneAnalysisAutomaticAdPlacement`")

        self._automatic_ad_placement = automatic_ad_placement

    @property
    def output_language_codes(self):
        # type: () -> AiSceneAnalysisOutputLanguageCodes
        """Gets the output_language_codes of this AiSceneAnalysisFeatures.

        AI scene analysis will create translated asset description files for the language codes. 

        :return: The output_language_codes of this AiSceneAnalysisFeatures.
        :rtype: AiSceneAnalysisOutputLanguageCodes
        """
        return self._output_language_codes

    @output_language_codes.setter
    def output_language_codes(self, output_language_codes):
        # type: (AiSceneAnalysisOutputLanguageCodes) -> None
        """Sets the output_language_codes of this AiSceneAnalysisFeatures.

        AI scene analysis will create translated asset description files for the language codes. 

        :param output_language_codes: The output_language_codes of this AiSceneAnalysisFeatures.
        :type: AiSceneAnalysisOutputLanguageCodes
        """

        if output_language_codes is not None:
            if not isinstance(output_language_codes, AiSceneAnalysisOutputLanguageCodes):
                raise TypeError("Invalid type for `output_language_codes`, type has to be `AiSceneAnalysisOutputLanguageCodes`")

        self._output_language_codes = output_language_codes

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
        if not isinstance(other, AiSceneAnalysisFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
