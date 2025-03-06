# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.ai_content_analysis_features import AiContentAnalysisFeatures
from bitmovin_api_sdk.models.ai_service import AiService
import pprint
import six


class AiContentAnalysis(object):
    @poscheck_model
    def __init__(self,
                 ai_service=None,
                 features=None):
        # type: (AiService, AiContentAnalysisFeatures) -> None

        self._ai_service = None
        self._features = None
        self.discriminator = None

        if ai_service is not None:
            self.ai_service = ai_service
        if features is not None:
            self.features = features

    @property
    def openapi_types(self):
        types = {
            'ai_service': 'AiService',
            'features': 'AiContentAnalysisFeatures'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'ai_service': 'aiService',
            'features': 'features'
        }
        return attributes

    @property
    def ai_service(self):
        # type: () -> AiService
        """Gets the ai_service of this AiContentAnalysis.

        AI service settings

        :return: The ai_service of this AiContentAnalysis.
        :rtype: AiService
        """
        return self._ai_service

    @ai_service.setter
    def ai_service(self, ai_service):
        # type: (AiService) -> None
        """Sets the ai_service of this AiContentAnalysis.

        AI service settings

        :param ai_service: The ai_service of this AiContentAnalysis.
        :type: AiService
        """

        if ai_service is not None:
            if not isinstance(ai_service, AiService):
                raise TypeError("Invalid type for `ai_service`, type has to be `AiService`")

        self._ai_service = ai_service

    @property
    def features(self):
        # type: () -> AiContentAnalysisFeatures
        """Gets the features of this AiContentAnalysis.

        Features of the AI content analysis

        :return: The features of this AiContentAnalysis.
        :rtype: AiContentAnalysisFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        # type: (AiContentAnalysisFeatures) -> None
        """Sets the features of this AiContentAnalysis.

        Features of the AI content analysis

        :param features: The features of this AiContentAnalysis.
        :type: AiContentAnalysisFeatures
        """

        if features is not None:
            if not isinstance(features, AiContentAnalysisFeatures):
                raise TypeError("Invalid type for `features`, type has to be `AiContentAnalysisFeatures`")

        self._features = features

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
        if not isinstance(other, AiContentAnalysis):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
