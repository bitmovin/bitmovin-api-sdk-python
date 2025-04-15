# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class IABTaxonomy(object):
    @poscheck_model
    def __init__(self,
                 version=None,
                 content_taxonomies=None,
                 ad_opportunity_taxonomies=None,
                 sensitive_topic_taxonomies=None):
        # type: (string_types, list[string_types], list[string_types], list[string_types]) -> None

        self._version = None
        self._content_taxonomies = list()
        self._ad_opportunity_taxonomies = list()
        self._sensitive_topic_taxonomies = list()
        self.discriminator = None

        if version is not None:
            self.version = version
        if content_taxonomies is not None:
            self.content_taxonomies = content_taxonomies
        if ad_opportunity_taxonomies is not None:
            self.ad_opportunity_taxonomies = ad_opportunity_taxonomies
        if sensitive_topic_taxonomies is not None:
            self.sensitive_topic_taxonomies = sensitive_topic_taxonomies

    @property
    def openapi_types(self):
        types = {
            'version': 'string_types',
            'content_taxonomies': 'list[string_types]',
            'ad_opportunity_taxonomies': 'list[string_types]',
            'sensitive_topic_taxonomies': 'list[string_types]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'version': 'version',
            'content_taxonomies': 'contentTaxonomies',
            'ad_opportunity_taxonomies': 'adOpportunityTaxonomies',
            'sensitive_topic_taxonomies': 'sensitiveTopicTaxonomies'
        }
        return attributes

    @property
    def version(self):
        # type: () -> string_types
        """Gets the version of this IABTaxonomy.


        :return: The version of this IABTaxonomy.
        :rtype: string_types
        """
        return self._version

    @version.setter
    def version(self, version):
        # type: (string_types) -> None
        """Sets the version of this IABTaxonomy.


        :param version: The version of this IABTaxonomy.
        :type: string_types
        """

        if version is not None:
            if not isinstance(version, string_types):
                raise TypeError("Invalid type for `version`, type has to be `string_types`")

        self._version = version

    @property
    def content_taxonomies(self):
        # type: () -> list[string_types]
        """Gets the content_taxonomies of this IABTaxonomy.


        :return: The content_taxonomies of this IABTaxonomy.
        :rtype: list[string_types]
        """
        return self._content_taxonomies

    @content_taxonomies.setter
    def content_taxonomies(self, content_taxonomies):
        # type: (list) -> None
        """Sets the content_taxonomies of this IABTaxonomy.


        :param content_taxonomies: The content_taxonomies of this IABTaxonomy.
        :type: list[string_types]
        """

        if content_taxonomies is not None:
            if not isinstance(content_taxonomies, list):
                raise TypeError("Invalid type for `content_taxonomies`, type has to be `list[string_types]`")

        self._content_taxonomies = content_taxonomies

    @property
    def ad_opportunity_taxonomies(self):
        # type: () -> list[string_types]
        """Gets the ad_opportunity_taxonomies of this IABTaxonomy.


        :return: The ad_opportunity_taxonomies of this IABTaxonomy.
        :rtype: list[string_types]
        """
        return self._ad_opportunity_taxonomies

    @ad_opportunity_taxonomies.setter
    def ad_opportunity_taxonomies(self, ad_opportunity_taxonomies):
        # type: (list) -> None
        """Sets the ad_opportunity_taxonomies of this IABTaxonomy.


        :param ad_opportunity_taxonomies: The ad_opportunity_taxonomies of this IABTaxonomy.
        :type: list[string_types]
        """

        if ad_opportunity_taxonomies is not None:
            if not isinstance(ad_opportunity_taxonomies, list):
                raise TypeError("Invalid type for `ad_opportunity_taxonomies`, type has to be `list[string_types]`")

        self._ad_opportunity_taxonomies = ad_opportunity_taxonomies

    @property
    def sensitive_topic_taxonomies(self):
        # type: () -> list[string_types]
        """Gets the sensitive_topic_taxonomies of this IABTaxonomy.


        :return: The sensitive_topic_taxonomies of this IABTaxonomy.
        :rtype: list[string_types]
        """
        return self._sensitive_topic_taxonomies

    @sensitive_topic_taxonomies.setter
    def sensitive_topic_taxonomies(self, sensitive_topic_taxonomies):
        # type: (list) -> None
        """Sets the sensitive_topic_taxonomies of this IABTaxonomy.


        :param sensitive_topic_taxonomies: The sensitive_topic_taxonomies of this IABTaxonomy.
        :type: list[string_types]
        """

        if sensitive_topic_taxonomies is not None:
            if not isinstance(sensitive_topic_taxonomies, list):
                raise TypeError("Invalid type for `sensitive_topic_taxonomies`, type has to be `list[string_types]`")

        self._sensitive_topic_taxonomies = sensitive_topic_taxonomies

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
        if not isinstance(other, IABTaxonomy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
