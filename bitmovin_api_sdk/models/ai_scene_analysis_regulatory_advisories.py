# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AiSceneAnalysisRegulatoryAdvisories(object):
    @poscheck_model
    def __init__(self,
                 topics=None):
        # type: (list[RegulatoryAdvisoryTopic]) -> None

        self._topics = list()
        self.discriminator = None

        if topics is not None:
            self.topics = topics

    @property
    def openapi_types(self):
        types = {
            'topics': 'list[RegulatoryAdvisoryTopic]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'topics': 'topics'
        }
        return attributes

    @property
    def topics(self):
        # type: () -> list[RegulatoryAdvisoryTopic]
        """Gets the topics of this AiSceneAnalysisRegulatoryAdvisories.

        The regulatory advisory topics to screen the asset for. At least one topic must be set. (required)

        :return: The topics of this AiSceneAnalysisRegulatoryAdvisories.
        :rtype: list[RegulatoryAdvisoryTopic]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        # type: (list) -> None
        """Sets the topics of this AiSceneAnalysisRegulatoryAdvisories.

        The regulatory advisory topics to screen the asset for. At least one topic must be set. (required)

        :param topics: The topics of this AiSceneAnalysisRegulatoryAdvisories.
        :type: list[RegulatoryAdvisoryTopic]
        """

        if topics is not None:
            if not isinstance(topics, list):
                raise TypeError("Invalid type for `topics`, type has to be `list[RegulatoryAdvisoryTopic]`")

        self._topics = topics

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
        if not isinstance(other, AiSceneAnalysisRegulatoryAdvisories):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
