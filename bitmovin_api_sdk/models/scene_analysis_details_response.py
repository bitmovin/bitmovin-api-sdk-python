# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.metadata import Metadata
import pprint
import six


class SceneAnalysisDetailsResponse(object):
    @poscheck_model
    def __init__(self,
                 scenes=None,
                 description=None,
                 keywords=None,
                 ratings=None,
                 sensitive_topics=None,
                 iab_sensitive_topic_taxonomies=None,
                 metadata=None):
        # type: (list[Scene], string_types, list[string_types], list[Rating], list[string_types], list[string_types], Metadata) -> None

        self._scenes = list()
        self._description = None
        self._keywords = list()
        self._ratings = list()
        self._sensitive_topics = list()
        self._iab_sensitive_topic_taxonomies = list()
        self._metadata = None
        self.discriminator = None

        if scenes is not None:
            self.scenes = scenes
        if description is not None:
            self.description = description
        if keywords is not None:
            self.keywords = keywords
        if ratings is not None:
            self.ratings = ratings
        if sensitive_topics is not None:
            self.sensitive_topics = sensitive_topics
        if iab_sensitive_topic_taxonomies is not None:
            self.iab_sensitive_topic_taxonomies = iab_sensitive_topic_taxonomies
        if metadata is not None:
            self.metadata = metadata

    @property
    def openapi_types(self):
        types = {
            'scenes': 'list[Scene]',
            'description': 'string_types',
            'keywords': 'list[string_types]',
            'ratings': 'list[Rating]',
            'sensitive_topics': 'list[string_types]',
            'iab_sensitive_topic_taxonomies': 'list[string_types]',
            'metadata': 'Metadata'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'scenes': 'scenes',
            'description': 'description',
            'keywords': 'keywords',
            'ratings': 'ratings',
            'sensitive_topics': 'sensitiveTopics',
            'iab_sensitive_topic_taxonomies': 'iabSensitiveTopicTaxonomies',
            'metadata': 'metadata'
        }
        return attributes

    @property
    def scenes(self):
        # type: () -> list[Scene]
        """Gets the scenes of this SceneAnalysisDetailsResponse.


        :return: The scenes of this SceneAnalysisDetailsResponse.
        :rtype: list[Scene]
        """
        return self._scenes

    @scenes.setter
    def scenes(self, scenes):
        # type: (list) -> None
        """Sets the scenes of this SceneAnalysisDetailsResponse.


        :param scenes: The scenes of this SceneAnalysisDetailsResponse.
        :type: list[Scene]
        """

        if scenes is not None:
            if not isinstance(scenes, list):
                raise TypeError("Invalid type for `scenes`, type has to be `list[Scene]`")

        self._scenes = scenes

    @property
    def description(self):
        # type: () -> string_types
        """Gets the description of this SceneAnalysisDetailsResponse.


        :return: The description of this SceneAnalysisDetailsResponse.
        :rtype: string_types
        """
        return self._description

    @description.setter
    def description(self, description):
        # type: (string_types) -> None
        """Sets the description of this SceneAnalysisDetailsResponse.


        :param description: The description of this SceneAnalysisDetailsResponse.
        :type: string_types
        """

        if description is not None:
            if not isinstance(description, string_types):
                raise TypeError("Invalid type for `description`, type has to be `string_types`")

        self._description = description

    @property
    def keywords(self):
        # type: () -> list[string_types]
        """Gets the keywords of this SceneAnalysisDetailsResponse.


        :return: The keywords of this SceneAnalysisDetailsResponse.
        :rtype: list[string_types]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        # type: (list) -> None
        """Sets the keywords of this SceneAnalysisDetailsResponse.


        :param keywords: The keywords of this SceneAnalysisDetailsResponse.
        :type: list[string_types]
        """

        if keywords is not None:
            if not isinstance(keywords, list):
                raise TypeError("Invalid type for `keywords`, type has to be `list[string_types]`")

        self._keywords = keywords

    @property
    def ratings(self):
        # type: () -> list[Rating]
        """Gets the ratings of this SceneAnalysisDetailsResponse.


        :return: The ratings of this SceneAnalysisDetailsResponse.
        :rtype: list[Rating]
        """
        return self._ratings

    @ratings.setter
    def ratings(self, ratings):
        # type: (list) -> None
        """Sets the ratings of this SceneAnalysisDetailsResponse.


        :param ratings: The ratings of this SceneAnalysisDetailsResponse.
        :type: list[Rating]
        """

        if ratings is not None:
            if not isinstance(ratings, list):
                raise TypeError("Invalid type for `ratings`, type has to be `list[Rating]`")

        self._ratings = ratings

    @property
    def sensitive_topics(self):
        # type: () -> list[string_types]
        """Gets the sensitive_topics of this SceneAnalysisDetailsResponse.


        :return: The sensitive_topics of this SceneAnalysisDetailsResponse.
        :rtype: list[string_types]
        """
        return self._sensitive_topics

    @sensitive_topics.setter
    def sensitive_topics(self, sensitive_topics):
        # type: (list) -> None
        """Sets the sensitive_topics of this SceneAnalysisDetailsResponse.


        :param sensitive_topics: The sensitive_topics of this SceneAnalysisDetailsResponse.
        :type: list[string_types]
        """

        if sensitive_topics is not None:
            if not isinstance(sensitive_topics, list):
                raise TypeError("Invalid type for `sensitive_topics`, type has to be `list[string_types]`")

        self._sensitive_topics = sensitive_topics

    @property
    def iab_sensitive_topic_taxonomies(self):
        # type: () -> list[string_types]
        """Gets the iab_sensitive_topic_taxonomies of this SceneAnalysisDetailsResponse.


        :return: The iab_sensitive_topic_taxonomies of this SceneAnalysisDetailsResponse.
        :rtype: list[string_types]
        """
        return self._iab_sensitive_topic_taxonomies

    @iab_sensitive_topic_taxonomies.setter
    def iab_sensitive_topic_taxonomies(self, iab_sensitive_topic_taxonomies):
        # type: (list) -> None
        """Sets the iab_sensitive_topic_taxonomies of this SceneAnalysisDetailsResponse.


        :param iab_sensitive_topic_taxonomies: The iab_sensitive_topic_taxonomies of this SceneAnalysisDetailsResponse.
        :type: list[string_types]
        """

        if iab_sensitive_topic_taxonomies is not None:
            if not isinstance(iab_sensitive_topic_taxonomies, list):
                raise TypeError("Invalid type for `iab_sensitive_topic_taxonomies`, type has to be `list[string_types]`")

        self._iab_sensitive_topic_taxonomies = iab_sensitive_topic_taxonomies

    @property
    def metadata(self):
        # type: () -> Metadata
        """Gets the metadata of this SceneAnalysisDetailsResponse.


        :return: The metadata of this SceneAnalysisDetailsResponse.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        # type: (Metadata) -> None
        """Sets the metadata of this SceneAnalysisDetailsResponse.


        :param metadata: The metadata of this SceneAnalysisDetailsResponse.
        :type: Metadata
        """

        if metadata is not None:
            if not isinstance(metadata, Metadata):
                raise TypeError("Invalid type for `metadata`, type has to be `Metadata`")

        self._metadata = metadata

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
        if not isinstance(other, SceneAnalysisDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
